# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 05:45:13 2025

@author: PIOTR
"""

import hashlib

def generate_hash_from_file(file_name: str)->str:
    """Generates a hash from file."""
    
    hex = hashlib.sha1() # Creating a hash object
    
    with open(file_name, "rb") as file: # Reading file as binary
        
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            hex.update(chunk) 
            
    return hex.hexdigest()


def main():
    """Main function."""
    
    file_a = 'a.txt' 
    file_b = 'b.txt' # Identical with a.txt
    file_c = 'c.txt' # Different from a.txt
    
    msg_a = generate_hash_from_file(file_a)
    msg_b = generate_hash_from_file(file_b)
    msg_c = generate_hash_from_file(file_c)
    
    print(msg_a)
    print(msg_b)
    print(msg_c)
    
    if(msg_a == msg_b):
        print('Files: {} and {} are identical.'.format(file_a, file_b))
    else:
        print('Files: {} and {} are not identical.'.format(file_a, file_b))

    if(msg_a == msg_c):
        print('Files: {} and {} are identical.'.format(file_a, file_c))
    else:
        print('Files: {} and {} are not identical.'.format(file_a, file_c))


if __name__ == "__main__":
    main()