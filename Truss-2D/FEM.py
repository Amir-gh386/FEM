# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:57:05 2024

@author: j15536ag
"""

############ Frist try in FEM in Python-Truss Example ##############
############      This is a truss with 3 elements     ##############
import numpy as np
from function import *

NL=np.array([[0,0],
             [1,0],
             [0.5,1]])

EL=np.array([[1,2],
             [2,3],
             [3,1]])

DorN=np.array([[-1,-1],
               [1,-1],
               [1,1]])

Fu=np.array([[0,0],
             [0,0],
             [0,-20]])


U_u=np.array([[0,0],
             [0,0],
             [0,0]])

E=10**6
A=0.01

PD=np.size(NL,1)
NoN=np.size(NL,0)


#Extended Node List Size of (NoN,6*PD)#
ENL= np.zeros([NoN,6*PD])

ENL[:,0:PD]=NL[:,:]
ENL[:,PD:2*PD]=DorN[:,:]

(ENL,DOFs,DOCs) = assign_BCs(NL,ENL)

K = assemble_stiffness(ENL, EL, NL, E, A)

ENL[:, 4*PD:5*PD] = U_u[:,:]
ENL[:, 5*PD:6*PD] = Fu[:,:]

U_u = U_u.flatten()
Fu = Fu.flatten()

Fp = assemble_forces(ENL, NL)
Up = assemble_displacement(ENL, NL) 

K_UU = K[0:DOFs, 0:DOFs]
K_UP = K[0:DOFs, DOFs:DOFs+DOCs]
K_PU = K[DOFs:DOFs+DOCs, 0:DOFs]
K_PP = K[DOFs:DOFs+DOCs, DOFs:DOFs+DOCs]

F = Fp - np.matmul(K_UP,Up)
U_u = np.matmul(np.linalg.inv(K_UU),F)
Fu = np.matmul(K_PU,U_u) + np.matmul(K_PP,Up)

ENL = update_nodes(ENL, U_u, NL, Fu)

