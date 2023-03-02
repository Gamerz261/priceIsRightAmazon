import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from messenger import Messenger


class Scraper:
    chromeOptions = Options()
    # chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions)

    def search_product_list(self, interval_count, interval_hours):

        url = "https://www.amazon.com/NETGEAR-16-Port-Gigabit-Ethernet-Unmanaged/dp/B08CQL5B87/?_encoding=UTF8&pd_rd_w=zM0gH&content-id=amzn1.sym.03bef33a-a357-4fe3-9505-7fd4d6236957&pf_rd_p=03bef33a-a357-4fe3-9505-7fd4d6236957&pf_rd_r=7P72JZ7K75SANCB4GZ39&pd_rd_wg=XTpfz&pd_rd_r=0061f9b6-3f19-4626-96b3-6d0cae83b5fe&ref_=pd_gw_ci_mcx_mr_hp_d&th=1"
        self.driver.get(url)
        a = self.driver.find_element('xpath', "//span[@class='a-price a-text-normal aok-align-center reinventPriceAccordionT2']//span[@aria-hidden='true']//span[@class='a-price-whole'][contains(text(),'363')]")
        print(a)
