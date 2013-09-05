"""Usage: docopt_test.py [options] <argument>

Options:
  --version             show version
  -h, --help            show this help message
  -f FILE, --file=FILE  write report to FILE
"""
from docopt import docopt
__version__ = '0.1'

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    print args
