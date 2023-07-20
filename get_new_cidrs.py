import unittest
import requests

def get_new_cidrs_from_range(api_url, api_key, range_start, range_end):
    response = requests.get(api_url + "/api/v1/subnets?range_start=" + range_start + "&range_end=" + range_end, headers={"X-API-KEY": api_key})
    if response.status_code == 200:
        return response.json()["data"]["subnets"]
    else:
        return None

class GetNewCidrsFromRangeTests(unittest.TestCase):

    def test_get_new_cidrs_from_range_with_valid_input(self):
        api_url = "https://your-phpipam-server/"
        api_key = "your-api-key"
        range_start = "10.0.0.0/16"
        range_end = "10.0.255.255/16"
        new_cidrs = get_new_cidrs_from_range(api_url, api_key, range_start, range_end)
        self.assertIsNotNone(new_cidrs)

    def test_get_new_cidrs_from_range_with_invalid_input(self):
        api_url = "https://invalid-phpipam-server/"
        api_key = "invalid-api-key"
        range_start = "10.0.0.0/16"
        range_end = "10.0.255.255/16"
        new_cidrs = get_new_cidrs_from_range(api_url, api_key, range_start, range_end)
        self.assertIsNone(new_cidrs)

if __name__ == "__main__":
    unittest.main()