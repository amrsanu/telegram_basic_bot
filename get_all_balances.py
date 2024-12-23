import json
import time
import requests

api_link = r"https://mainnet.mirrornode.hedera.com"
next = api_link + r"/api/v1/balances"

all_accounts = []
while next:
    time.sleep(1)
    try:
        response = requests.get(
            next,
            headers={},
        )
        data = response.json()
        all_accounts.extend(data["balances"])

        next = data.get("links", {}).get("next", None)
        if next and next != "null":
            next = api_link + next
    except Exception as e:
        print(f"Error: {data}, {e}")
        break

with open("all_balances.json", "w") as f:
    json.dump(all_accounts, f)
