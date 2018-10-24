#!/usr/bin/python
import random
from urllib.parse import urlsplit
import re

# no of digits for initial unique id generation
NO_OF_DIGITS = 10

# List consisting of allowed charcters in URL
character_set =['-','_']

# base value for encoding
BASE = 64

is_first_url = True
IDToURLMap ={}
URLtoID = {}

# Loading character set to have all characters of range 0-9, a-z and A-Z
def generate_character_set():
    for i in range(97,123):
        character_set.append(chr(i))
    for i in range(65,91):
        character_set.append(chr(i))
    for i in range(0,10):
        character_set.append(str(i))

# generates  n digit unique number for each URL
def get_unique_number():
    if(is_first_url):
        random_num = random.randrange(1, 10**NO_OF_DIGITS)
    else:
        random_num = random_num +1
    return random_num

# Used to generate base64 short url
def get_short_url(original_url):
    if(original_url in IDToURLMap.values()):
        unique_id = URLtoID[original_url]
    else:
        unique_id = get_unique_number()
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(original_url))
                    
    short_url = ''
    while(bool(re.match('[0-9\_\-]+[A-Za-z1-9\-\_]*', short_url)) or short_url == '') :
        copy_id = unique_id
        while unique_id > 0:
            short_url += character_set[unique_id %BASE]
            unique_id //= BASE
        if(re.match('[0-9\_\-]+[A-Za-z1-9\-\_]*', short_url)):
            unique_id = get_unique_number()
                
    URLtoID[original_url] = copy_id
    IDToURLMap[copy_id] = original_url
    return base_url + short_url

# returns original url given short-url
def get_long_url(short_url):
    short_str = short_url.split("://")[1].split("/")[1]
        
    if bool(re.match('^[a-zA-Z0-9\-\_]+$',short_str)):
        unique_id  = 0
        indx = 0
        for c in short_str:
            unique_id += (character_set.index(c)) * (BASE ** indx)
            indx  = indx + 1
        if not unique_id in IDToURLMap:
            return ''
        return IDToURLMap[unique_id]
    return ''


def main_func():
    generate_character_set()
    original_url = input("Enter URL: ")
    while original_url != "":
        surl= get_short_url(original_url)
        print("")
        print("corresponding short URL: ",surl)
        print("")
    
        surl_ip = input("Enter short URL: ")
        lurl = get_long_url(surl_ip)
        print("")
        if(lurl == ''):
            print("short url does not exist")
        else:
            print("Corresponding original URL: ",lurl)
        is_first_url = False
        print("")
        original_url = input("Enter URL: ")
if __name__== "__main__":
    main_func()
