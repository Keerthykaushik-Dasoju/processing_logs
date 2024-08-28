import unittest, sys, os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from log_line_parser import extract_dstport_and_protocol, load_log_format

class TestExtractFieldFromLine(unittest.TestCase):
    def test_extract_field_from_line(self):
        line = "tcp 80"
        protocol_index = 0
        dstport_index = 1
        
        dstport, protocol = extract_dstport_and_protocol(line, dstport_index, protocol_index)
        self.assertEqual(dstport, "80")
        self.assertEqual(protocol, "tcp")

    def test_load_log_format_success(self):
        # Create a temporary test file with log format
        test_format_filename = 'data/test_log_format.txt'
        with open(test_format_filename, 'w') as file:
            file.write("version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status\n")

        # Expected output
        expected_output = {
            'version': 0,
            'account-id': 1,
            'interface-id': 2,
            'srcaddr': 3,
            'dstaddr': 4,
            'srcport': 5,
            'dstport': 6,
            'protocol': 7,
            'packets': 8,
            'bytes': 9,
            'start': 10,
            'end': 11,
            'action': 12,
            'log-status': 13
        }

        # Call the function and verify the output
        result = load_log_format(test_format_filename)
        self.assertEqual(result, expected_output)

        # Clean up the test file
        os.remove(test_format_filename)

if __name__ == '__main__':
    unittest.main()
