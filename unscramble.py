# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:56:46 2021

@author: NicSch02
"""

def unscramble (scramble, dictionary, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    # check input variables
    if type(scramble) != str:
        raise ValueError('scramble must be of type str')
    if type(dictionary) != str:
        raise ValueError('dictionary must be a str pointing to a file')
    if type(alphabet) != str:
        raise ValueError('alphabet must be of type str')
    
    # read dictionary
    with open(dictionary) as f:
        lines = f.readlines()
        
    scramble = scramble.upper()
    notscramble = alphabet.upper()
    for s in scramble:
        notscramble = notscramble.replace(s, '')
    
    # filter dictionary   
    lines_filtered = []
    for l in lines:
        l = l[0:len(l)-1]
        if len(scramble) == len(l):
            lupper = l.upper()
            s_in = True
            for s in scramble:
                if s not in lupper:
                    s_in = False
            
            ns_not_in = True
            for ns in notscramble:
                if ns in lupper:
                    ns_not_in = False
                    
            if (s_in and ns_not_in):
                lines_filtered.append(l)
             
    return lines_filtered