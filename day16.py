import sys
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

    ans = 0
    for key in packets:
        ans += packets[key]["version"]
    return ans


if __name__ == "__main__":
    print(main())
