# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:33:34 2024

@author: j15536ag
"""

import numpy as np
from uniform_mesh import *


d1 = 1
d2 = 1
p = 1
m = 1
element_type = "D2QU4N"
defV = 0.1

NL, EL = uniform_mesh(d1, d2, p, m, element_type)

BC_flag = 'extension'

(ENL, DOFs, DOCs) = assign_BCs(NL, BC_flag, defV)

