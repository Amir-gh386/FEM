# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:43:01 2024

@author: j15536ag
"""

import numpy as np
import math

def assign_BCs(NL, BC_flag, defV):
    
    NoN = np.size(NL,0)
    PD = np.size(NL,1)
    
    ENL = np.zeros([NoN], 6*PD)
    
    ENL[:,0:PD] = NL
    
    if BC_flag == 'extension':
        
        for i in range (0, NoN):
            
            for E[i,0] == 
    
    
    
    return (ENL, DOFs, DOCs)