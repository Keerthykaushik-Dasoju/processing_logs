# Processing Logs

## Overview

**Processing Logs** is a Python-based project designed to process log files, map dstport and protocols to tags, and analyze port-protocol combinations. The project is structured to handle different log formats.
    
## Project Structure

   ```bash
    .
    ├── Data                              # Data files directory
    │   ├── default_log_format.txt        # Default log format file
    │   ├── custom_log_format.txt         # Custom log format file (optional)
    │   ├── protocol_number_mapping.csv   # CSV file with protocol-to-number mapping
    │   ├── tag_mapping.csv               # CSV file with tag mapping
    │   ├── output.txt                    # Output file containing final results
    │   └── log_file.log                  # Sample log file to be processed
    ├── main.py                           # Main script to run the project
    ├── csv_reader.py                     # Handles CSV file reading and processing
    ├── log_processor.py                  # Processes log files and counts occurrences
    ├── log_line_parser.py                # Extracts fields from log lines
    ├── write_to_output_file.py           # Writes results to an output file
    └── README.md                         # Project documentation
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
