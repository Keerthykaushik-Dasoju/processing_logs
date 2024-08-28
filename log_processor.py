from collections import Counter
from log_line_parser import extract_dstport_and_protocol

def process_log_file(log_filename, tag_mapping, field_index_map, protocol_number_mapping):
    tag_counter = Counter()
    port_proto_comb_counter = Counter()
    dstport_index, protocol_index = field_index_map['dstport'], field_index_map['protocol']
    with open(log_filename, mode='r') as log_file:
        for line in log_file:
            dstport, protocol_number = extract_dstport_and_protocol(line, dstport_index, protocol_index)
            protocol = protocol_number_mapping[protocol_number]
            if (dstport, protocol) in tag_mapping:
                tag = tag_mapping[(dstport, protocol)]
                tag_counter[tag] += 1
            else:
                tag_counter['Untagged'] += 1
            port_proto_comb_counter[(dstport, protocol)] += 1

    return tag_counter, port_proto_comb_counter