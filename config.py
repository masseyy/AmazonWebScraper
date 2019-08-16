class link:
    # 1.  Enter webpage URL (You do not need to format just paste with
    #                               single quotes inside the brackets)
    URL = ('https://www.amazon.co.uk/dp/B0792M4ZV5/' +
           'ref=gw_uk_desk_h1_aucc_dn_singlehero_aug19?' +
           'pf_rd_p=74004516-53cb-4f60-aaa6-154efdb13d4f&pf_rd_' +
           'r=JG0HQ8VSNBXFTVZK7D2Z')
    # 2.  Search google for "My user agent" (no quotes) and copy/paste.
    headers = {"User-Agent":
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) ' +
               'Gecko/20100101 Firefox/68.0'}


class emailSettings:
    # 3.  SMTP Email login settings (keep the single quotes)
    ename = 'ENTER YOUR EMAIL HERE'
    epass = 'ENTER YOUR PASSWORD'
    port = 587  # Ready for Gmail using TLS
    # 4.  Sender/Receiver Email address
    email = 'ENTER YOUR EMAIL HERE'


class checkPrice:
    # 5.  Checks if the current sale price is lower or equal to this value.
    #                   (If current price on webpage is $5.99, change to 5.98)
    targetPrice = 49.99

    # Postioning of characters for price on webpage. In FireFox or Chrome
    # right click then inspect element. Make sure the picker is on and
    # click on the product title then the price.

    prodTitle = 'productTitle'  # 6.  Under inspector you will see
    #                       <span id="" copy the ID and paste it below.
    #                       DEFAULT set to: id="productTitle

    pagePrice = 'priceblock_ourprice'  # 7.  Under inspector you will see
    #                       <span id="" copy the ID and paste it below.
    #                       DEFAULT set to: id="priceblock_ourprice"

    # 8.  Try setting below values from 0-5 and change accordingly.
    firstNumber = 1
    numberLength = 6
