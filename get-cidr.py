import requests

def get_new_cidrs(api_url, api_key):
    response = requests.get(api_url + "/api/v1/subnets", headers={"X-API-KEY": api_key})
    if response.status_code == 200:
        return response.json()["data"]["subnets"]
    else:
        return None

if __name__ == "__main__":
    api_url = "https://your-phpipam-server/"
    api_key = "your-api-key"
    new_cidrs = get_new_cidrs(api_url, api_key)
    if new_cidrs:
        print(new_cidrs)
    else:
        print("No new CIDRs found")
