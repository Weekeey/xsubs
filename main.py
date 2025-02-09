'''
    xsubs : python3 script automate the subdomain enumuration
    by using build in tools     

'''
import os
import json
import time
import subprocess
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor


CONFIGURATION_FILE = "config.json"
BANNER =  """
 _ _| \  ___ _ _| |_ ___ 
|_'_|\ \|_ -| | | . |_ -|
|_,_| \_|___|___|___|___|
Weekey!@github
"""


class Xsubs :
    def __init__ (self, conf_file, domain,wordlist=None,  list_domains=None):
        self.conf_file = conf_file
        self.wordlist = wordlist
        self.domain = domain
        self.max_workers = 75


    def configuration (self): 
        with open (self.conf_file, 'r') as file :
            data = json.load (file)
        return data

    
    def check_folder (self, folder_name):
        if not os.path.exists (folder_name):
            os.mkdir (folder_name)
            print (f'Folder was created {folder_name}')
    
    def run_tools (self):
        subdomains = set () 
        TOOLS_COMMAND = [
                ['subfinder','-d', self.domain],
                ['assetfinder', '-subs-only', self.domain]
        ]
        try : 
            for command in TOOLS_COMMAND :
                result = subprocess.run ([command][0], capture_output=True, text=True)
                if result.stdout :
                    subdomains.update (result.stdout.splitlines())

        except FileNotFoundError as e :
            print ("Error : make sure sunfinder and assetfinder are installed and accessible") 
            return []
        except Exception as e :
            print (f"An error occurred : {e}")

        return list(subdomains)
    

if __name__ == "__main__":
    print (colored(BANNER, 'cyan'))
    xsubs = Xsubs (CONFIGURATION_FILE, "edunet.tn")
    xsubs.run_tools ()

