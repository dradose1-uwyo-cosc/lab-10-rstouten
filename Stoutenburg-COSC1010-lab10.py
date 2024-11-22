# Reuben Stoutenburg
# UWYO COSC 1010
# Submission Date: 11/21/2024
# Lab 10
# Lab Section: 13
# Sources, people worked with, help given to: 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()  

path = Path('rockyou.txt')
passwords = path.read_text()
split_pass = passwords.splitlines()

path = Path('hash')
hash_txt = path.read_text()

try:
    for line in split_pass:
        pass_hash = get_hash(line)
        if pass_hash == hash_txt:
            print(line)
        else:
            pass
except:
    pass






