import csv, os

# Read the lookup table and create a dictionary for tag mapping. This method is very flexible to any new fields or replacing current fields
def read_tag_mapping(csv_filename):
    tag_mapping = {}

    # Error handling: File Not Found
    if not os.path.exists(csv_filename):
        raise FileNotFoundError(f"File '{csv_filename}' not found.")
    # Open csv file with read mode
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader) # For skipping the header

        # Determine the index of the tag column
        tag_index = headers.index('tag')
        
        for row in reader:
            # Create a list of all values except the tag
            key = []
            for index, value in enumerate(row):
                if index != tag_index:
                    if value.isalpha():
                        value = value.lower()
                    key.append(value)
            tag = row[tag_index]
            tag_mapping[tuple(key)] = tag
    
    return tag_mapping

# Read the protocol number mapping csv file and generating a dictionary for the mapping between protocol number and protocol
def read_protocol_number_mapping(csv_filename):
    protocol_number_mapping = {}

    # Error handling: File Not Found
    if not os.path.exists(csv_filename):
        raise FileNotFoundError(f"File '{csv_filename}' not found.")
    
    # Open csv file with read mode
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            protocol, number = row
            protocol_number_mapping[number] = protocol
    return protocol_number_mapping
