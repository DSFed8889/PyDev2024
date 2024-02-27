import argparse
from io import StringIO
from cowsay import cowsay, list_cows, read_dot_cow, get_random_cow


class Presets:
    def __init__(self, p):
        self.p = p
        if p not in 'bdgpstwy' and p is not None:
            raise(ValueError('Have not such preset'))

    def __str__(self):
        return self.p


def read_file(file_name):
    if args.file:
        with open(file_name, 'r') as file:
            return read_dot_cow(StringIO(file.read()))
    return None

def get_cow(cow, random):
    if random:
        return get_random_cow()
    return cow


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
parser.add_argument('-p', '--preset',
                    nargs='?',
                    type=Presets,
                    default=None,
                    help='Presets of eyes and tongues')
parser.add_argument('-e', '--eyes',
                    nargs='?',
                    default='oo',
                    help='A custom eye string')
parser.add_argument('-T', '--tongue',
                    nargs='?',
                    default='  ',
                    help='A custom tongue string')
parser.add_argument('-w', '--width',
                    nargs='?',
                    type=int,
                    default=40,
                    help='The width of the text bubble')
parser.add_argument('-n',
                    action='store_false',
                    help="Whether text shouldn't be wrapped in the bubble")
parser.add_argument('-f', '--file',
                    nargs='?',
                    default=None,
                    help='File with a custom string representing a cow')
parser.add_argument('-r', '--rand',
                    action='store_true',
                    help='File with a custom string representing a cow')


args = parser.parse_args()

if args.list:
    print(list_cows())
else:
    print(cowsay(args.message,
                 cow=get_cow(args.cow, args.rand),
                 preset=str(args.preset),
                 eyes=args.eyes,
                 tongue=args.tongue,
                 width=args.width,
                 wrap_text=args.n,
                 cowfile=read_file(args.file)))
