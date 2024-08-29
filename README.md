# Processing Logs

## Overview

**Processing Logs** is a Python-based project designed to process log files, map dstport and protocols to tags, and analyze port-protocol combinations. The project is structured to handle different log formats. Python was preferred due to its simple and intuitive syntax, along with powerful built-in libraries like 'csv' for file handling and 'collections' for efficient data processing, making it ideal for tasks involving log and CSV manipulation. Given the 10MB log file size, Python’s performance is more than sufficient for this project.
    
## Project Structure

   ```bash
    .
    ├── data                                        # Data files directory
    │   ├── default_log_format.txt                  # Default log format file
    │   ├── custom_log_format.txt                   # Custom log format file (optional)
    │   ├── protocol_number_mapping.csv             # CSV file with protocol-to-number mapping
    │   ├── tag_mapping.csv                         # CSV file with tag mapping
    │   ├── output.txt                              # Output file containing final results
    │   └── log_file.log                            # Sample log file to be processed
    ├── src                                         # Src directory containing code files
    │   ├── main.py                                 # Main script to run the project
    │   ├── csv_reader.py                           # Handles CSV file reading and processing
    │   ├── log_processor.py                        # Processes log files and counts occurrences
    │   ├── log_line_parser.py                      # Extracts fields from log lines
    │   └── write_to_output_file.py                 # Writes results to an output file
    ├── tests                                       # Tests directory containing unittest files
    │   ├── tests_csv_reader.py                     # Unit tests for csv reader
    │   ├── tests_log_processor.py                  # Unit tests for log processor
    │   ├── tests_log_line_parser.py                # Unit tests for log line parser
    │   └── tests_write_to_output_file.py           # Unit tests for write to output file
    └── README.md                                   # Project documentation
   ```

## Prerequisites

Before running the project, ensure to have "Python 3.x" installed

## Instructions to Setup and Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Keerthykaushik-Dasoju/processing_logs.git
   cd processing_logs

2. **Run the Project**

    You can run the project using the default log format or specify a custom log format.

    Using Default Log Format

    ```bash
    For Mac and Linux
    python src/main.py

    For Windows
    python .\src\main.py
    ```

    Using Custom Log Format (update custom_log_format.txt with the format you want to use)

    ```bash
    For Mac and Linux
    python src/main.py data/custom_log_format.txt

    For Windows
    python .\src\main.py .\data\custom_log_format.txt
    ```

3. **View the Results**

    The results will be written to an output file ("output.txt") in the data directory. This output file will contain tag counts and port-prototcol combinations count

4. **Run Unittests**

    Run the unit tests from the project root using

   ```bash
    python -m unittest discover tests
    ```

## Tests

1. **Default Log Format:** The project was tested using a log file with the default log format to ensure correct processing and output generation.

2. **Custom Log Format:** The project was tested with a log file using a custom log format by modifying and reducing the number of columns, confirming the flexibility and adaptability of the code.

3. **Error Handling:** The project was tested by providing incorrect file names to verify that the error handling mechanisms work as expected, gracefully managing missing or misnamed files.ber of columns

## Assumptions

1. **Case Insensitivity for Protocols:** The protocol values in the lookup table are treated as case-insensitive. This means that entries such as TCP, Tcp, and tCp are all considered equivalent to tcp.

2. **Case Sensitivity for Tags:** The tag values in the lookup table are treated as case-sensitive. For example, sc_P1 and SV_P1 are recognized as two distinct tags.

3. **Consistent Log Format:** It is assumed that all log entries in the log file adhere to the same format throughout.

## Analysis on my code

1. **Flexible Log Format Handling:** The project is designed to work with any type of log format. If you have a custom log format, simply add it to the custom_log_format.txt file in the Data directory.

2. **Reusable Tag Mapping Code:** The tag mapping code in csv_reader.py is designed to be reusable, even if the structure of the lookup table changes. Currently, the lookup table includes columns for dstport, protocol, and tag, with dstport and protocol mapped to the tag. The code is flexible enough to handle additional columns, as long as the last column remains the tag.

3. **Protocol Number Mapping:** The protocol_number_mapping.csv file is used to map assigned protocol numbers to their corresponding protocol names. While the file currently includes the most commonly used protocols, more can be added in the future without requiring any changes to the existing code.

4. **Scalability Considerations:** The project is currently optimized for log files up to 10MB in size. If future requirements involve processing larger log files, it would be advisable to implement multithreading to handle the increased load efficiently.
