import os
import sys
import signal
import requests
import threading
import readline
import subprocess

from termcolor import colored
from concurrent.futures import ThreadPoolExecutor


class Statuscheck  :
    def __init__ (self, url=None, max_workers=10 ):
        self.url = url
        self.max_workers = max_workers

    def single_url (self, url): 
        try :
            response  = requests.get (url)
            if response.status_code == 200:
                print (colored(f'{url} ','green'))
                with open (f'200.txt', 'a') as f :
                    f.write (url+"\n")

            elif response.status_code == 400 : 
                print (colored(f'{url}','red'))
                with open (f'400.txt', 'a') as k :
                    k.write (url+"\n")
            elif response.status_code == 404 :
                print (colored(f'{url}','cyan'))
                with open (f'404.txt', 'a') as n :
                    n.write (url+'\n')

        except Exception as e : 
            return false
        except KeyboardInterrupt :
            pass
    def multiple_url (self, list_urls):
        with ThreadPoolExecutor (max_workers=self.max_workers) as executor :
            with open (list_urls, 'r') as f :
                urls = f.readlines ()
                urls = [url.strip() for url in urls]
                executor.map (self.single_url, urls)

   