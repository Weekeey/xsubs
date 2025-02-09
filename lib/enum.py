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


class Xsubs :
    def __init__ (self, domain=None,wordlist=None,  list_domains=None, output_path=None):
        self.wordlist = wordlist
        self.domain = domain
        self.output_path = output_path


        self.final_output = f'{self.output_path}/domains.txt'
        self.max_workers = 75

    # def count_lines(self, file_path):
    #     with open(file_path, 'r') as file:
    #         lines = file.readlines()
    #         return len(lines)



    def run_tools (self):
        subdomains = set () 
        TOOLS_COMMAND = [
                ['subfinder','-d',self.domain,'-silent','-o', self.final_output],
                ['assetfinder', '-subs-only', self.domain ,'>', self.final_output]
                
        ]
        try : 
            for command in TOOLS_COMMAND :
                print (colored(f'(+) ', 'green') + f'{command[0]} Is running ')
                result = subprocess.run ([command][0], capture_output=True, text=True)
                if result.stdout :
                    subdomains.update (result.stdout.splitlines())

        except FileNotFoundError as e :
            print ("Error : make sure sunfinder and assetfinder are installed and accessible") 
        except Exception as e :
            print (f"An error occurred : {e}")

    







if __name__ == "__main__":
    print (colored(BANNER, 'cyan'))
    xsubs = Xsubs (CONFIGURATION_FILE, "edunet.tn")
    xsubs.run_tools ()








