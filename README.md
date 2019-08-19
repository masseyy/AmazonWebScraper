# AmazonWebScraper
This python application will scrape through a HTML webpage using Beautiful Soup. This allows us to check a webpage like Amazon, and set the current price. So if the price becomes lower or equal to the price declared it will send an email alert using the smtplib. Navigate to the config.py file to enter these details before use.

# Requirements
Your computer will need to have python 3 installed. You can do this by heading over to https://www.python.org/downloads/

# Instructions
Once python3 is installed you will need to navigate to where the clone downloaded. It will download as a zip file so unzip the file. Once unzipped, navigate to the config.py file and make the necessary changes. You can use a text editor like notepad++ or sublime. I built this using VS studio code.

The config.py file has very clear instructions. Same steps are on on the file also.

1.  Enter webpage URL 

2.  Search google for "My user agent" (no quotes) and copy/paste.

3.  SMTP Email login settings (keep the single quotes)

4.  Sender/Receiver Email address
 
5.  Checks if the current sale price is lower or equal to this value. (If current price on webpage is $5.99, change to 5.98). 

# Postioning of characters for price on webpage. In FireFox or Chrome right click, then inspect element. Make sure the picker is on and click on the product title then the price.

6.  For finding the Product Title's id, using inspector you will see <span id="" copy the ID and paste it below. DEFAULT is set to: id="productTitle

7.  For finding the Product price's id, using inspector you will see <span id="" copy the ID and paste it below. DEFAULT is set to: id="priceblock_ourprice"

8.  Try setting below values from 0-5 and change accordingly.

Open terminal and change the directory to where the files are in the unzipped folder. You can do this on a MacOS computer like 'cd ./Downloads/AmazonWebScraper-master' (without the ') or by clicking and droping the folder into the terminal.

You can now type the command 'python3 app.py' (without the ') into the terminal. 
Enjoy!
