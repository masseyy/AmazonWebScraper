import time
# Importing functions
from functions import check_price, send_mail
# Importing Class
from config import checkPrice

check_price()

# Send email if current price is lower or equal to entered value (see config)
if(check_price.convert_price <= checkPrice.targetPrice):
    send_mail()

# Loop time in seconds (every hour)
while(True):
    check_price()
    print('Going to sleep for an hour')
    time.sleep(3600)
