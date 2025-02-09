
import os
import json
import shutil
import socket

from lib.status import *
from lib.enum import *

 

''' ?????????? '''
def banner ():
    BANNER =  '''
       /gg\           /gg
      /g.gg\         /gg.g\ 
     |gg..gg\       /gg..gg| 
     |gg...g|       |g...gg| 
     |gg...g|       |g...gg| 
      \gg..g/       \g..gg/ 
       |gg.gvgggggggvg.gg| 
      /ggggggggggggggggggg\ 
     /gggg(((ggggggg)))gggg\ 
    |ggggg....ggggg....ggggg| 
    |ggggg....ggggg....ggggg| 
    |ggcccgggg\___/ggggcccgg| 
    |ggcccccgggg|ggggcccccgg| 
      \gcccggg\---/gggcccg/ 
         \ggggggggggggg/
    '''
    print (colored (BANNER, 'white'))
def check_domain (domain):
    try :
        socket.gethostbyname (domain)
        return True
    except socket.gaierror :
        return False


def check_file (file_path):
    if os.path.isfile (file_path):
        answer = input (colored('(+) ', 'blue')+ "Delete Oldest File (N/y) > ")
        if answer == 'y' or answer == 'Y':
            os.remove (file_path)

def remove_duplicates_inplace(self, file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    unique_sorted_lines = sorted(set(lines))
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(unique_sorted_lines)


def configuration_extract (config_file):
     if os.path.isfile (config_file):
        print (colored ('[~] ', 'green')+ 'the configuration file is located !!')
        with open (config_file, 'r') as file :
            data = json.load (file)
        return data
     else :
         print (colored ('Error : cannot find the configuration file ! ', 'red'))
         return 0


def main () :
    banner ()
    
    CURRENT_PATH = os.getcwd ()
    CONFIGURATION_PATH = f"{CURRENT_PATH}/config/config.json"
    
    CONFIGURATION_FILE = configuration_extract (CONFIGURATION_PATH)     
    OUTPUT_FOLDER_NAME = CONFIGURATION_FILE['files']['output_directory_name']
    
    OUTPUT_FILE_PATH = f"{CURRENT_PATH}/{OUTPUT_FOLDER_NAME}"

    # TOOLS_NAMES = CONFIGURATION_PATH['tools']

    domain = 'edunet.tn'
    def mkdir_output_file_by_domain_name (domain):
        test_path = f'{OUTPUT_FILE_PATH}/{domain[0 : -3]}'
        if not(os.path.isdir (test_path)):
            file_created = os.mkdir (test_path)
            print (colored ('[~]', 'green')+ colored (f'Outpue file Created {test_path}','yellow'))
        else :
            print (colored ('File already exists', 'cyan'))
            answer = input ('Did you remove the folder and create New one (Y/n) > ')
            if answer == "Y" or answer == "y":
                shutil.rmtree (test_path)
                os.mkdir (test_path)
                print (colored('the new file wat created ', 'green'))
        return test_path




    
    answer = input ('Enter domain name : ')
    if check_domain (answer):
        local_shit = mkdir_output_file_by_domain_name (answer)
            






















if __name__ == "__main__" :
    main () 








