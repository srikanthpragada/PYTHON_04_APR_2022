import sys

sys.path.insert(0, r'c:\library')

print(sys.path)  # Module search path

from stlib import *

print(str_funs.has_upper('abc'))
