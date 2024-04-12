# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:08:41 2024

@author: j15536ag
"""

import numpy as np


def uniform_mesh(d1, d2, p, m, element_type):
    
    PD= 2 
    q = np.array([[0,0],[d1,0],[0,d2],[d1,d2]]) #for corners
    
    NoN= (p+1)*(m+1)
    NoE= p*m
    NPE=4
    
    
    ###Nodes###
    NL= np.zeros([NoN, PD])
    
    a= (q[1,0]-q[0,0])/p  #increment the horizontal direction
    b= (q[2,1]-q[0,1])/m #increment the vertical direction
    
    
    n = 0 #This will allow to go through rows in NL
    for i in range (1,m+2):
        for j in range (1,p+2):
            
            NL[n,0]= q[0,0] + (j-1)*a  # For x values
            NL[n,1]= q[0,1] + (i-1)*b  # For y values
            
            n+=1
            
            
    #### Elements ####
    EL= np.zeros([NoE, NPE])
    
    for i in range (1,m+1):
        for j in range (1,p+1):
            
            if j ==1:
                
                EL[(i-1)*p+j-1,0]=(i-1)*(p+1)+j
                EL[(i-1)*p+j-1,1]=EL[(i-1)*p+j-1,0]+1
                EL[(i-1)*p+j-1,3]=EL[(i-1)*p+j-1,0]+(p+1)
                EL[(i-1)*p+j-1,2]=EL[(i-1)*p+j-1,3]+1
                
            else:
                
                EL[(i-1)*p+j-1,0]=EL[(i-1)*p+j-2,1]
                EL[(i-1)*p+j-1,3]=EL[(i-1)*p+j-2,2]
                EL[(i-1)*p+j-1,1]=EL[(i-1)*p+j-1,0]+1
                EL[(i-1)*p+j-1,2]=EL[(i-1)*p+j-1,3]+1
                
    EL = EL.astype(int)
    
    return (NL,EL)
                
                
                
        
                
                
                
                
    
      
    
    
    
    
    
    
    
    