import sys, getopt
from Amazon_Scraper import Scraper

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
    try:
        opts, args = getopt.getopt(argv, "ht:")
    except getopt.GetoptError:

        sys.exit(2)
    for opt, arg in opts:

        # Set defaults, they get updated as the user updates them.
        repeats = 12
        interval = 6
        run = True

        if opt in "-h":
            print(blue + "Syntax: " + white + "python3 main.py [-i (integer)]")
            run = False
            mode.append(opt)
        # Accept manual override for num repeats and intervals
        if opt in "-t":
            print("accepting override")

            Trepeats = input(pink + "Please input the number of times you would like the program to repeat: ")
            Tinterval = input(pink + "Please input the number of hours in between each interval: ")
            if Trepeats is not None:
                repeats = Trepeats
            else:
                print('Going with default value 12')

            if Tinterval is not None:
                interval = Tinterval
            else:
                print('Going with default value 6')
            mode.append(opt)

        print(1)
        if run:
            client.search_product_list(int(repeats), int(interval))


if __name__ == '__main__':
    main(sys.argv[1:])
