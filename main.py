import sys, getopt
import time

from Amazon_Scraper import Scraper
from time import sleep

mode = []

white = "\033[38;5;252m"
pink = "\033[38;5;5m"
red = "\033[38;5;1m"
orange = "\033[38;5;3m"
green = "\033[38;5;150m"
blue = "\033[38;5;4m"
purple = "\033[38;5;20m"


def main(argv):
    # Initialize variables for use in running the proper method for encrypting or decrypting the password
    client = Scraper()
    # Takes in arguments from the command line
    userIn = str(sys.argv[len(sys.argv) - 1]).encode('utf-8')
    try:
        opts, args = getopt.getopt(argv, "ht:")
    except getopt.GetoptError:

        sys.exit(2)
    for opt, arg in opts:

        # Set defaults, they get updated as the user updates them.
        target = 0
        interval = 6
        run = True

        if opt in "-h":
            print(blue + "Syntax: " + white + "python3 main.py [-i (integer)]")
            run = False
            mode.append(opt)
        # Accept manual override for num repeats and intervals
        if opt in "-t":
            target = float(userIn)
            print(red + "MAIN :: " +blue + "Target price set as " + str(target))

            mode.append(opt)

        if run:
            url = input(red + "MAIN :: " + pink + "Please type in the Amazon url: " + white)
            # Loop it
            while True:
                client.search_product_list(target, url)
                time.sleep(5 * 60)


if __name__ == '__main__':
    main(sys.argv[1:])
