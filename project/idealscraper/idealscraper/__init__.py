# # adding /vagrant/project in PYTHONPATH
#
import os, sys
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(directory)