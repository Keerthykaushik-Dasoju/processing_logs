import unittest
import os, sys

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from write_to_output_file import write_results_to_file
from collections import Counter

class TestWriteResultsToFile(unittest.TestCase):
    def test_write_results_to_file(self):
        # Mock data
        tag_counts = Counter({'web': 2, 'video': 3})
        port_proto_comb_counts = Counter({('23', 'tcp'): 2, ('24', 'udp'): 3})
        
        # Write results to a test output file
        output_filename = 'data/test_output.txt'
        write_results_to_file(tag_counts, port_proto_comb_counts, output_filename)
        
        # Verify the content of the output file
        with open(output_filename, 'r') as f:
            content = f.read()
        
        expected_content = """Count of matches for each tag, sample o/p shown below

Tag Counts:

Tag, Count
web, 2
video, 3

Count of matches for each port/protocol combination

Port/Protocol Combination Counts:

Port,Protocol,Count
23, tcp, 2
24, udp, 3
"""
        self.assertEqual(content, expected_content)
        
        # Clean up the test output file
        os.remove(output_filename)

if __name__ == '__main__':
    unittest.main()
