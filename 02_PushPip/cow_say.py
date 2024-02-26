import argparse
from cowsay import cowsay


parser = argparse.ArgumentParser("Cowsay custom program")

parser.add_argument('message', nargs='?',
                    default='Hello, world!',
                    help='A string to wrap in the text bubble')

args = parser.parse_args()
print(cowsay(args.message))
