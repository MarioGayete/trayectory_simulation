# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:07:43 2022

@author: Mario Gayete Ibáñez
"""



# Import functions
from input_data import *
from direct_solver import *
from postprocess import *


# Input data    
constants, bodies = input_data('Inputs/')

bodies[0].show_data()


"""bodies = []

bodies.append(planet('Sun', 1.9885e30, 0, [0.0, 0.0], [0,0]))
bodies.append(planet('Earth', 5.972e24, 0, [0.4293,  0.8886], [-19830.522032434674,9915.261016217337])) # velocities approx
bodies.append(planet('Mars', 6.39e24, 0, [-1.2043,  -1.0146,  0.0083], [7011.148301801897,-7011.148301801897]))# velocities approx

bodies.append(planet('1', 1, 0, [-0.97000436, 0.24308753], [0.4662036850, 0.4323657300]))
bodies.append(planet('2', 1, 0, [0,0], [-0.93240737, -0.86473146])) 
bodies.append(planet('3', 1, 0, [0.97000436, -0.24308753], [0.4662036850, 0.4323657300]))
"""
# Solver
temporal_solver(bodies, constants.G, constants.At, constants.t_max, constants.At_save, 
                constants.beta, constants.epsilon, constants.max_it)# 6.67e-11)

# Postprocess
position_2Drepresentation(bodies)
