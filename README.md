# Processing Logs

## Overview

**Processing Logs** is a Python-based project designed to process log files, map dstport and protocols to tags, and analyze port-protocol combinations. The project is structured to handle different log formats.
    
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
    python main.py
    ```

    Using Custom Log Format (update custom_log_format.txt with the format you want to use)

    ```bash
    python main.py data/custom_log_format.txt
    ```

3. **View the Results**

    The results will be written to an output file ("output.txt") in the data directory. This output file will contain tag counts and port-prototcol combinations count


TODO:

1. why python
2. assumptions as following
3. case sensitivity
4. works with any type of log format
5. tag mapping code can be reusable for future additions or replacements
6. just added mostly used protocol numbers in the protocol number mapping can add more to that in the future
7. what test are done
8. analysis on my code
