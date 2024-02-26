import argparse
from cowsay import cowsay, list_cows


parser = argparse.ArgumentParser("Cowsay custom program")

parser.add_argument('message',
                    nargs='?',
                    default='Hello, world!',
                    help='A string to wrap in the text bubble')
parser.add_argument('-c', '--cow',
                    default='default',
                    help='The name of the cow (valid names from list_cows)')
parser.add_argument('-l', '--list',
                    action='store_true',
                    help='List of cows')

args = parser.parse_args()
if args.list:
    print(list_cows())
else:
    print(cowsay(args.message, cow=args.cow))
