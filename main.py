# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:58:54 2021

@author: NicSch02
"""

from unscramble import *

if __name__ == "__main__":
    candidates = unscramble('Wollsokcen', 'wordlist-german.txt')
    print(candidates)