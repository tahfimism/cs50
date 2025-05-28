import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].replace(".", "").isdigit() == False:
    sys.exit("Command-line argument is not a number")


responce = requests.get("http://rest.coincap.io/v3/assets/bitcoin?apiKey=c108264ff342fe773043a09586a7aeff729b6ba1439ae9cea30423f4d9ac9c96")
res = responce.json()



data = res["data"]
price = data["priceUsd"]

output = float(sys.argv[1]) * float(price)
print(f"${output:,.4f}")  # 4 decimal places and thousand separator with a comma


