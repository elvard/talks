from argparse import ArgumentParser
__version__ = '0.1'
parser = ArgumentParser(version=__version__)
parser.add_argument("args", nargs="*")
parser.add_argument("-f", "--file", dest="filename",
          help="write report to FILE", metavar="FILE")

__doc__ = '\n'.join([parser.format_usage(), parser.format_help()])

if __name__ == '__main__':
    args = parser.parse_args()
    print args, args.filename, args.args
