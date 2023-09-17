"""
The purpose of the code below is to allow for in-module unit testing

When testing modules that imports other modules, the code dealing with
imports need to be changed with respect to the referencing of folders.
This lines of code below inserts this director into the sys.path list
so that it is seen by the 'main module' with having to '.' reference it,
as the creates problems when running an individual module.
"""

import os
import sys

directory = os.path.dirname(__file__)
sys.path.insert(0,directory)
