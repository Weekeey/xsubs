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
            answer = input (colored('(+) ', 'blue')+ "Delete Oldest File (N/y) > ")
            if answer == 'y' or answer == 'Y':
                os.remove (self.final_output)

    def remove_duplicates_inplace(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        unique_sorted_lines = sorted(set(lines))

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(unique_sorted_lines)






    def check_folder (self):
        if not os.path.exists (self.output_path):
            os.mkdir (self.output_path)
            print (colored ('(+} ', 'blue') + f'Folder was created {self.output_path}')
        else : print (colored ('(+} ', 'blue') +'Folder already exist')
    
    def count_lines(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)

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
        except Exception as e :
            print (f"An error occurred : {e}")

        print (colored ("(~) ", 'yellow')+ 'Subdomains Founded > ' + colored (f'{self.count_lines(self.final_output)}', 'yellow'))
    

if __name__ == "__main__":
    print (colored(BANNER, 'cyan'))
    xsubs = Xsubs (CONFIGURATION_FILE, "edunet.tn")
    xsubs.run_tools ()








