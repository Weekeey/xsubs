'''
    xsusbs : python3 script automate the subdomain enumuration
    by using build in tools     

'''
import os
import json
import threading
from concurrent.futures import ThreadPoolExecutor

CONFIGURATION_FILE = 'config.json' 
with open (CONFIGURATION_FILE, 'r') as file :
    data = json.load (file)

OUTPUT_PATH = data['output']['filename']
#OUTPUT_PATH = data.get ('output', {}).get('filename', 'Not found')


print (OUTPUT_PATH)


