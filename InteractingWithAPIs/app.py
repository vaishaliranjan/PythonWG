
from InteractingWithAPIs.libs.openexchange import OpenExchangeClient
import time
APP_ID= "c7dfe084f179400e89c65d097f1c5857"
#ENDPOINT = "https://openexchangerates.org/api/latest.json"

# response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# exchange_rates= response.json()["rates"]
#
# usd_amount= 1000
# gbp_amount = usd_amount *exchange_rates["GBP"]

client= OpenExchangeClient(APP_ID)
usd_amount=1000

start= time.time()
gbp_amount= client.convert(usd_amount,"USD", "GBP")
end=time.time()
print(end-start)


start= time.time()
gbp_amount= client.convert(usd_amount,"USD", "GBP")
end=time.time()
print(end-start)

start= time.time()
gbp_amount= client.convert(usd_amount,"USD", "GBP")
end=time.time()
print(end-start)

print(f"USD {usd_amount} is GBP {gbp_amount:.2f}")