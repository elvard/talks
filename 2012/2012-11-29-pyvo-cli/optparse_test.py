from optparse import OptionParser
__version__ = '0.1'
parser = OptionParser(version=__version__)
parser.add_option("-f", "--file", dest="filename",
          help="write report to FILE", metavar="FILE")
__doc__ = parser.get_usage()  # missing get_help()

if __name__ == '__main__':
    options, args = parser.parse_args()
