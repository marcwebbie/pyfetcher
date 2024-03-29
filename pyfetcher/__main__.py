#!/usr/bin/env python
from __future__ import print_function

# Execute with
# $ python pyfetcher/__main__.py (2.6+)
# $ python -m pyfetcher (2.7+)

import argparse
import sys

if __package__ is None and not hasattr(sys, "frozen"):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(path))
    sys.path.append(os.path.dirname(os.path.dirname(path)))


import pyfetcher
pyfetcher.main()
