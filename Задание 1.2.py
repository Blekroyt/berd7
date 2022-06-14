#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

def rev_key(dct):
    dct_new = dict()
    for i, v in dct.items():
        for w in v:
            dct_new[w] = dct_new.get(w, []) + [i]
    return dct_new
        
 
dct = {1: 'acc', 2: 'cab', 3: 'ccb'}
print(rev_key(dct))
