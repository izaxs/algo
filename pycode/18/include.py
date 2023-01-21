import os
import sys

pycodeDirectory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(pycodeDirectory)
sys.path.append(os.path.join(pycodeDirectory, 'util'))
