import unittest, sys, os
from collections import Counter


# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from log_processor import process_log_file

class TestProcessLogFile(unittest.TestCase):
    def test_process_log_file(self):
        # Mock data and field index map
        field_index_map = {'protocol': 0, 'dstport': 1}
        dstport_protocol_to_tag = {('23','tcp'): 'web', ('25','udp'): 'video'}
        protocol_number_mapping = {'6': 'tcp', '17': 'udp'}
        
        # Write mock log data to a temporary file for testing
        with open('data/test_log_file.log', 'w') as f:
            f.write("6 23\n17 25\n6 23\n17 53\n")

        # Expected counts
        expected_tag_counts = Counter({'web': 2, 'video': 1, 'Untagged': 1})
        expected_port_proto_comb_counts = Counter({('23', 'tcp'): 2, ('25', 'udp'): 1, ('53', 'udp'): 1})
        
        tag_counts, port_proto_comb_counts = process_log_file(
            'data/test_log_file.log', 
            dstport_protocol_to_tag, 
            field_index_map, 
            protocol_number_mapping
        )
        
        self.assertEqual(tag_counts, expected_tag_counts)
        self.assertEqual(port_proto_comb_counts, expected_port_proto_comb_counts)

        # Clean up the test file
        os.remove('data/test_log_file.log')

if __name__ == '__main__':
    unittest.main()
