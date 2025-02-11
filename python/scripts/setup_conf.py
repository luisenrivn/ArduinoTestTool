import os
import sys

# Get the directory of the current script 
current_dir = os.path.dirname(__file__) 
# Construct the path to the module folder 
module_folder_path = os.path.abspath(os.path.join(current_dir, '..', r'api'))

# Add the module folder to the sys.path import sys 
sys.path.append(module_folder_path)
from test_api import * 