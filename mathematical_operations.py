# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""

def mod_vector(vector):
    mod = 0.0
    for i_vec in vector:
        mod += i_vec**2
    
    return mod**0.5

def sum_vectors(v1,v2):
    v3 = v1.copy()
    for i in range(0,len(v1)):
        v3[i] = v1[i] + v2[i]
        
    return v3
        