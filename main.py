'''
    xsubs : python3 script automate the subdomain enumuration
    by using build in tools     

'''
import os
import sys
import json
import time
import threading
import subprocess

from termcolor import colored
from concurrent.futures import ThreadPoolExecutor


DEFAULT_OUTPUT_RESULT = f'{os.getcwd ()}/result/'
CONFIGURATION_FILE = "config.json"
BANNER =  """
 _ _| \  ___ _ _| |_ ___ 
|_'_|\ \|_ -| | | . |_ -|
|_,_| \_|___|___|___|___|
Weekey!@github
"""


class Xsubs :
    def __init__ (self, conf_file, domain,wordlist=None,  list_domains=None, output_path=DEFAULT_OUTPUT_RESULT):
        self.conf_file = conf_file
        self.wordlist = wordlist
        self.domain = domain
        self.output_path = output_path


        self.final_output = f'{self.output_path}/domains.txt'
        self.max_workers = 75


    def configuration (self): 
        with open (self.conf_file, 'r') as file :
            data = json.load (file)
        return data


    def check_file (self):

        if os.path.isfile (self.final_output):
            answer = input (colored('(+) ', 'blue')+ "Delete Oldest File (N/y) >")
            if answer == 'y' or answer == 'Y':
                os.remove (self.final_output)





    def check_folder (self):
        if not os.path.exists (self.output_path):
            os.mkdir (self.output_path)
            print (colored ('(+} ', 'blue') + f'Folder was created {self.output_path}')
        else : print (colored ('(+} ', 'blue') +'Folder already exist')
    
    def count_lines_in_file(file_path):
        last_count = 0
        while True:
            try:
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    count = len(lines)
                    
                    if count != last_count:  # Update only if count changes
                        sys.stdout.write(f"\r> Number of subdomains : {count} ")
                        sys.stdout.flush()
                        last_count = count
    
            except FileNotFoundError:
                sys.stdout.write("\r> Waiting for file... ")
                sys.stdout.flush()
    
            time.sleep(1)  # Adjust delay as needed






    def run_tools (self):
        
        subdomains = set () 
        TOOLS_COMMAND = [
                ['subfinder','-d',self.domain,'-silent','-o', self.final_output],
                ['assetfinder', '-subs-only', self.domain ,'>', self.final_output]
        ]
        try : 
            self.check_folder ()
            self.check_file ()       
            for command in TOOLS_COMMAND :
                print (colored(f'(+) ', 'green') + f'{command[0]} Is running ')
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

