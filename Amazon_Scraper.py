from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from messenger import Messenger


class Scraper:
    green = "\033[38;5;150m"
    white = "\033[38;5;252m"
    print(green + "SELENIUM :: " + white + "Opening browser...")
    # --- Define browser options, and run them on the calling of the class Scraper --- #
    chromeOptions = Options()
    # For some reason this doesn't work on MacOS... if you're on windows it should work fine.
    # chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions)

    # --- search_product_list takes in a target price and a url and finds the price --- #
    def search_product_list(self, target, url):
        # Color codes for console
        white = "\033[38;5;252m"
        pink = "\033[38;5;5m"
        red = "\033[38;5;1m"
        orange = "\033[38;5;3m"
        green = "\033[38;5;150m"
        blue = "\033[38;5;4m"
        purple = "\033[38;5;20m"
        #url = "https://www.amazon.com/NETGEAR-16-Port-Gigabit-Ethernet-Unmanaged/dp/B08CQL5B87/?_encoding=UTF8&pd_rd_w=zM0gH&content-id=amzn1.sym.03bef33a-a357-4fe3-9505-7fd4d6236957&pf_rd_p=03bef33a-a357-4fe3-9505-7fd4d6236957&pf_rd_r=7P72JZ7K75SANCB4GZ39&pd_rd_wg=XTpfz&pd_rd_r=0061f9b6-3f19-4626-96b3-6d0cae83b5fe&ref_=pd_gw_ci_mcx_mr_hp_d&th=1"

        # Load the url into the browser
        self.driver.get(url)
        # Locate the position of the price based on where it's typically located
        a = self.driver.find_element('xpath', "/html[1]/body[1]/div[1]/div[3]/div[9]/div[6]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h5[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]")
        # The price returns with a $ in front of it, so we remove it here
        parsedPrice = str(a.get_attribute('innerHTML'))[1:]
        print(green + "SELENIUM :: " + white + "Found price: " + purple + parsedPrice)

        # Determine if the parsedPrice is lower than the defined 'target' price
        if float(parsedPrice) < target:
            messageClient = Messenger()
            messageClient.sendMessage("The listing for " + str(url) + " is now priced at " + str(a) + " which is lower than your target price " + str(target))
            return parsedPrice
        else:
            print(green + "SELENIUM :: " + white + "Price is not lower than target " + red + str(target))
            return False
