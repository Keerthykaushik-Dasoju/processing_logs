import sys
from csv_reader import read_tag_mapping, read_protocol_number_mapping
from log_processor import process_log_file
from log_line_parser import load_log_format
from write_to_output_file import write_results_to_file

def main(custom_log_format=None):
    
    try:

        # Read the CSV file and create the tag mapping
        tag_mapping = read_tag_mapping('data/tag_mapping.csv')

        # Read the CSV file and create the protocol number mapping
        protocol_number_mapping = read_protocol_number_mapping('data/protocol_number_mapping.csv')

        # Use default log format unless a custom log format is provided
        log_format_file = custom_log_format if custom_log_format else 'data/default_log_format.txt'

        # Retrive the field to index map from the log format file
        field_index_map = load_log_format(log_format_file)

        # Process the log file and count tags
        tag_counts, port_proto_comb_counts = process_log_file('data/log_file.log', tag_mapping, field_index_map, protocol_number_mapping)

        # Writing result to an output file
        write_results_to_file(tag_counts, port_proto_comb_counts)
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Accept an optional custom log format file as a command-line argument
    custom_log_format = sys.argv[1] if len(sys.argv) > 1 else None
    main(custom_log_format)
