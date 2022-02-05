import json
import unittest
from sniffer import sniffer


class TestSniffer(unittest.TestCase):
    def test_sniffer(self):
        """
        test the sniffer function
        :return:
        """
        sniffer("data/example_input.json")

        test_path = "data/example_output.json"
        y = open(test_path)
        test_data = json.load(y)
        y.close()

        result_path = "sample.json"
        x = open(result_path)
        result_data = json.load(x)
        x.close()

        self.assertEqual(test_data, result_data)

