# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:30:30 2024

@author: j15536ag
"""

import numpy as np


# define functions #

def f1(x,y):
    
    return 10*x**2 + 5*y*x + 6*y**3 - 10

def f2(x,y):
    
    return 4*x*y + 3*x + 2*y -15

# Define Jacobian #

def J(x,y):
    
    return np.array([[20*x + 5*y, 5*x + 18*y**2],
                     [4*y + 3, 4*x + 2]])

# Intial guess #
x0 = 1.0
y0 = 1.0

# Define iteration process #

max_itr = 20
convegenece = 1e-8

# Newton-raphson computation #

for i in range (max_itr):
    # Define updated finctions # 
    F = np.array([f1(x0,y0), f2(x0,y0)])
    
    # Calculate the inverse of the Jacobian matrix at (x0, y0)#
    J_inv = np.linalg.inv(J(x0,y0))
    
    # Computing delta for updating guesses #
    delta = - J_inv @ F
    
    x0 += delta[0]
    y0 += delta[1]
    
    # Check for convergence #
    if np.linalg.norm(delta) < convegenece:
        print (f' Solution Converged in {i+1} iterations')
        print (f' x, y would be [{x0:.6f} , {y0:.6f}]')
        break
    
    
# Display result if not converged
if i == max_itr - 1:
    print(f'Did not converge after {max_itr} iterations')    
            
            
        
        
    