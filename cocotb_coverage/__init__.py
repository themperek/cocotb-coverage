
import sys

__version__ = '0.1.0'

if sys.version_info[0] < 3:
    raise Exception("cocotb-coverage package requies Python 3")
