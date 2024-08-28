import sys, os
import unittest

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from csv_reader import read_tag_mapping, read_protocol_number_mapping

class TestReadTagMapping(unittest.TestCase):
    def test_read_tag_mapping(self):
        # Mock data simulating the CSV content
        test_csv = """dstport,protocol,tag\n25,TCP,web\n26,UDP,video\n27,icmp,monitoring"""
        
        # Write mock data to a temporary file for testing
        with open('data/test_tag_mapping.csv', 'w') as f:
            f.write(test_csv)

        # Call the function and verify the output
        expected_output = {
            ('25','tcp'): 'web',
            ('26','udp',): 'video',
            ('27','icmp',): 'monitoring'
        }
        
        result = read_tag_mapping('data/test_tag_mapping.csv')
        self.assertEqual(result, expected_output)

        # Clean up the test file
        os.remove('data/test_tag_mapping.csv')

    def test_read_protocol_number_mapping(self):
        # Mock data simulating the CSV content
        test_csv = """protocol,number\nicmp,1\nipv4,4\ntcp,6"""
        
        # Write mock data to a temporary file for testing
        with open('data/test_protocol_number_mapping.csv', 'w') as f:
            f.write(test_csv)

        # Call the function and verify the output
        expected_output = {
            '1': 'icmp',
            '4': 'ipv4',
            '6': 'tcp'
        }
        
        result = read_protocol_number_mapping('data/test_protocol_number_mapping.csv')
        self.assertEqual(result, expected_output)

        # Clean up the test file
        os.remove('data/test_protocol_number_mapping.csv')

if __name__ == '__main__':
    unittest.main()
