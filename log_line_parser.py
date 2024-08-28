import os

# Generate field indexes based on the log format file which can be default or custom
def load_log_format(format_filename):

     # Error handling: File Not Found
    if not os.path.exists(format_filename):
        raise FileNotFoundError(f"File '{format_filename}' not found.")
    with open(format_filename, mode='r') as file:
        line = file.readline().strip()
        fields = line.split()  # Split the line into individual fields based on spaces
        field_index_map = {field: index for index, field in enumerate(fields)}
    return field_index_map

# Extract dstport and protocol from the log line
def extract_dstport_and_protocol(line, dstport_index, protocol_index):
    fields = line.split()
    return fields[dstport_index], fields[protocol_index]

