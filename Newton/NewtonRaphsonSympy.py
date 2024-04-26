# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:25:53 2024

@author: j15536ag
"""
import sympy as sp

#### Solving Nonlinear Equation by Newton-Raphson Method ####
#### Define Variables ####

x,y = sp.symbols('x y')

#### Define Functions ####

f1 = x**2 + x*y - 10
f2 = y + 3*x*y**2 - 57

#### Define Jacobian Matrix ####

J = sp.Matrix([[f1.diff(x), f1.diff(y)], [f2.diff(x), f2.diff(y)]])

#### Delta Info ####
# Define Initial Guesses #

x_n = 1.5
y_n = 3.5

# Iterations #
max_itr = 10
convergence = 1e-8

#### Newton-Raphson Computing ####

for iteration in range (max_itr):
    
    f_n = sp.Matrix([f1.subs({x: x_n, y: y_n}), f2.subs({x: x_n, y: y_n})])
    J_n = J.subs({x: x_n, y: y_n})
    
    # Delta #
    deltas = J_n.inv() * -f_n
    
    # Guesses Updating #
    x_n += deltas[0]
    y_n += deltas[1]
    
    # Check updates for conergence #
    if deltas.norm() < convergence:
        print(f'Solution converged in: {iteration+1} iteration')
        break
    
print(f'Solution: x = {x_n.evalf()}, y = {y_n.evalf()}')


