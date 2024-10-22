import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    bitcoinapi = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_keys = bitcoinapi.json()
    rate_bitcoin = float(bitcoin_keys["bpi"]["USD"]["rate_float"])
try:
    float(sys.argv[1])
    amount = rate_bitcoin * float(sys.argv[1])
    print(f"${amount:,.4f}")

except (requests.RequestException, ValueError):
    sys.exit("Command-line argument is not a number")
