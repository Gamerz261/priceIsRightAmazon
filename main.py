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

    # Takes in arguments from the command line
    try:
        opts, args = getopt.getopt(argv, "hrt:")
    except getopt.GetoptError:

        sys.exit(2)
    for opt, arg in opts:

        # Set defaults, they get updated as the user updates them.
        repeats = 12
        interval = 6

        if opt in ("-h"):
            print(blue + "Syntax: " + white + "python3 main.py [-i (integer)]")
            mode.append(opt)
        elif opt in "-r":
            mode.append(opt)
            print(pink + "Please input the number of times you would like the program to repeat: ")
            repeats = input()
        elif opt in "-t":
            mode.append(opt)
            print(pink + "Please input the hours in between each cycle")
            interval = input()
        # When all the data is collected from the user, run the program.
        Scraper.search_product_list(repeats, interval)

if __name__ == '__main__':
    main(sys.argv[1:])
