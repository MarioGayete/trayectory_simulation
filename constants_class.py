# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""

class constant_parameters:
    def __init__(self):
        # Constants: all units in International System
        
        ####### Physical constants #######
        self.G = 6.67e-11 # Gravitation constant
        
        ####### Numerical constants #######
        # Time constants
        self.At = 1 # Numerical time step
        self.At_save = 1 # Time step interval for saving the data
        self.t_max = 100 # Maximum computational time
        #  Numerical integration constants
        self.epsilon = 1e-9 # Convergence error
        self.beta = 0.5 # Integration type (0 = implicit, 1 = explicit, 0.5 = Crank-Nicolson)
        self.max_it = 1e2 # Maximum iterations allowed within one time step	
    
    def allocate_values(self,constant_name, value):
        if constant_name == 'G':
            self.G = float(value)
        elif constant_name == 'At':
            self.At = float(value)
        elif constant_name == 'At_save':
            self.At_save = float(value)
        elif constant_name == 't_max':
            self.t_max = float(value)
        elif constant_name == 'EPSILON':
            self.epsilon = float(value)
        elif constant_name == 'beta':
            self.beta = float(value)
        elif constant_name == 'max_it':
            self.max_it = float(value)
        elif constant_name != None:
            raise Exception("The following constant is not implemented: "  + constant_name)
        
    
