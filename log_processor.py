from collections import Counter
from log_line_parser import extract_dstport_and_protocol
import os

# Parse the log file to get tag counts and port, protocol combination counts
def process_log_file(log_filename, tag_mapping, field_index_map, protocol_number_mapping):
    tag_counter = Counter()
    port_proto_comb_counter = Counter()
    dstport_index, protocol_index = field_index_map['dstport'], field_index_map['protocol']
    
    # Error handling: File Not Found
    if not os.path.exists(log_filename):
        raise FileNotFoundError(f"File '{log_filename}' not found.")
    # Open log file with read mode
    with open(log_filename, mode='r') as log_file:
        for line in log_file:
            # Extract dstport and protocol from log line
            dstport, protocol_number = extract_dstport_and_protocol(line, dstport_index, protocol_index)
            # Retrieve the protocol based on the protocol number
            protocol = protocol_number_mapping[protocol_number]
            if (dstport, protocol) in tag_mapping:
                tag = tag_mapping[(dstport, protocol)]
                # Increment tag counter
                tag_counter[tag] += 1
            else:
                # If the combination of (dstport, protocol) is not in tag_mapping
                tag_counter['Untagged'] += 1
            # Increment port protocol combination counter
            port_proto_comb_counter[(dstport, protocol)] += 1

    return tag_counter, port_proto_comb_counter