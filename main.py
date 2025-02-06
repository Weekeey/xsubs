'''
    xsusbs : python3 script automate the subdomain enumuration
    by using build in tools     

'''
import os
import json
import threading
import shutil
from time import sleep

from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

tools = [
    'shuffledns','subfinder','assetfinder','dnsx','puredns',
    'scilla'
]

CONFIGURATION_FILE = 'config.json' 
with open (CONFIGURATION_FILE, 'r') as file :
    data = json.load (file)
SAVE_FOLDER = data['output']['filename']
#OUTPUT_PATH = data.get ('output', {}).get('filename', 'Not found')
def check_folder (folder_name):
    if not os.path.exists (folder_name):
        os.mkdir (folder_name)
        print (f'Folder was created {folder_name}')

def tools_check (tool):
    check_tool_result = shutil.which (tool)
    if check_tool_result : print (colored(f'{tool} i found !','green'))
    else : print (colored (f'{tool} is not found', 'red'))



for tool in tools :
    tools_check (tool)

check_folder (SAVE_FOLDER)




