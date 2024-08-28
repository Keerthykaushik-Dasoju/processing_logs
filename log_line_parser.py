def load_log_format(format_filename):
    with open(format_filename, mode='r') as file:
        line = file.readline().strip()
        fields = line.split()  # Split the line into individual fields based on spaces
        field_index_map = {field: index for index, field in enumerate(fields)}
    return field_index_map

def extract_dstport_and_protocol(line, dstport_index, protocol_index):
    fields = line.split()
    return fields[dstport_index], fields[protocol_index]

