# Import request library for HTTP requests
# Import the config.py files Classes
# BeautifulSoup4 for extracting data from HTML and XML
# Send emails using SMTP

import requests
from config import link, emailSettings, checkPrice
from bs4 import BeautifulSoup
import smtplib


def check_price():
    page = requests.get(link.URL, headers=link.headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    global title

    title = soup.find(id=checkPrice.prodTitle).get_text()
    checkPrice.price = soup.find(id=checkPrice.pagePrice).get_text()
    check_price.convert_price = float(checkPrice.price
                                      [checkPrice.firstNumber:
                                       checkPrice.numberLength])

    print(title.strip())
    print("£", (check_price.convert_price))


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', emailSettings.port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(emailSettings.ename, emailSettings.epass)

    subject = 'Price fell down!'
    body = 'Check the amazon link ' + str(link.URL)

    price = (check_price.convert_price)
    msg = f"Subject: {subject}\n\n{title.strip()} \
          \n\n{(price)}{(' GBP')}\n\n{body}"

    server.sendmail(
        emailSettings.email,
        emailSettings.email,
        msg
    )
    print('Email sent')

    server.quit()
