import unittest
import requests

class GetNewCidrsTests(unittest.TestCase):

    def test_get_new_cidrs_with_valid_input(self):
        api_url = "https://your-phpipam-server/"
        api_key = "your-api-key"
        new_cidrs = get_new_cidrs(api_url, api_key)
        self.assertIsNotNone(new_cidrs)

    def test_get_new_cidrs_with_invalid_input(self):
        api_url = "https://invalid-phpipam-server/"
        api_key = "invalid-api-key"
        new_cidrs = get_new_cidrs(api_url, api_key)
        self.assertIsNone(new_cidrs)

if __name__ == "__main__":
    unittest.main()