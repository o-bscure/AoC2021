import sys
from functools import reduce
def main():
    data = open("data16.txt").readline().strip()
    data = bin(int(data, 16)).zfill(4*len(data))[2:]
    return(parse(data))

def parse(data):
    i = 0
    packets = {}
    def p(parent):
        nonlocal data
        nonlocal i
        meta_id = len(packets)
        packet_version = int(data[i:i+3], 2)
        packet_type = int(data[i+3:i+6], 2)
        i += 6
        if packet_type == 4:
            packet_value_str = ""
            last_group = False
            while not last_group:
                group_type = int(data[i], 2)
                group_value = data[i+1:i+5]
                packet_value_str += group_value
                if group_type == 0:
                    last_group = True
                i += 5
            packet_value = int(packet_value_str, 2)
            packets[meta_id] = {
                                "parent": parent,
                                "version": packet_version,
                                "type": packet_type,
                                "value": packet_value,
                                }
        else:
            length_type_id = int(data[i], 2)
            i += 1
            if length_type_id == 0:
                sub_length = int(data[i:i+15], 2)
                packets[meta_id] = {
                                    "parent": parent,
                                    "version": packet_version,
                                    "type": packet_type,
                                    "value": sub_length,
                                    }
                i += 15
                sub_index_edge = sub_length + i
                while i < sub_index_edge:
                    p(meta_id)
            else:
                sub_count = int(data[i:i+11], 2)
                packets[meta_id] = {
                                    "parent": parent,
                                    "version": packet_version,
                                    "type": packet_type,
                                    "value": sub_count,
                                    }
                i += 11
                for _ in range(sub_count):
                    p(meta_id)

    while i < len(data) and data[i:] != "0"*len(data[i:]):
        p(-1)

    children = {}
    for key in packets:
        parent_key = packets[key]['parent']
        if parent_key in children:
            children[parent_key].append(key)
        else:
            children[parent_key] = [key]

    type_id_fns = {
        0: lambda x: sum(x),
        1: lambda x: reduce(lambda a,b: a*b,x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: 1 if x[0]>x[1] else 0,
        6: lambda x: 1 if x[0]<x[1] else 0,
        7: lambda x: 1 if x[0]==x[1] else 0,
    }
    def evaluate(packet_key):
        if packet_key not in children:
            return packets[packet_key]['value']

        nonlocal type_id_fns
        child_values = []
        for child_key in children[packet_key]:
            child_values.append(evaluate(child_key))
        type_id = packets[packet_key]['type']
        return type_id_fns[type_id](child_values)

    return evaluate(0)


if __name__ == "__main__":
    print(main())
