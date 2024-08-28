from csv_reader import read_tag_mapping, read_protocol_number_mapping
from log_processor import process_log_file
from log_line_parser import load_log_format
from write_to_output_file import write_results_to_file

def main(custom_log_format=None):
    # Read the CSV file and create the tag mapping
    tag_mapping = read_tag_mapping('tag_mapping.csv')

    # Read the CSV file and create the protocol number mapping
    protocol_number_mapping = read_protocol_number_mapping('protocol_number_mapping.csv')

    # Use default log format unless a custom log format is provided
    log_format_file = custom_log_format if custom_log_format else 'default_log_format.txt'

    # Retrive the field to index map from the log format file
    field_index_map = load_log_format(log_format_file)

    # Process the log file and count tags
    tag_counts, port_proto_comb_counts = process_log_file('log_file.log', tag_mapping, field_index_map, protocol_number_mapping)

    # Writing result to an output file
    write_results_to_file(tag_counts, port_proto_comb_counts)

if __name__ == "__main__":
    main()
