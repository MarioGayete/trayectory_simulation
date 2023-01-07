# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""
# Import libraries
from numpy import *

class planet:
    def __init__(self, planet_name, planet_mass, planet_radius, position, velocity):
        # planet_name is a string corresponding to the name of the planet
        # planet_mass is a scalar corresponding to the mass of the planet
        # position is a 3D vector corresponding to the rectangular coordinates of the planet in UA
        # velocity is a 3D vector corresponding to the velocity of the planet in the xyz basis in m/s
        self.name = planet_name
        self.m = planet_mass
        self.r = position
        self.v = velocity
        self.R = planet_radius
        
        # if the position or velocity vectors are 2D, we force them to be 3D
        if len(self.r) < 3: 
            self.r.append(0.0)
        if len(self.v) < 3: 
            self.v.append(0.0)
            
        # convert position in UA into meters (1 UA = 1.496e11 m)
        self.r = dot(self.r,1)#1.496e11)
        
        # Initialize the numerical parameters
        self.accel = [0.0,0.0,0.0]
        
        # Previous time step values
        self.r_prev = self.r.copy()
        self.v_prev = self.v.copy()
        self.accel_prev = self.accel.copy()
        
        # Guess values
        self.r_guess = self.r.copy()
        self.v_guess = self.v.copy()
        
        # Color representation
        self.color = 'k'
        
    def iteration_step(self): # the guess values are updated
        self.r_guess = self.r.copy()
        self.v_guess = self.v.copy()
        
    def color_representation(self, new_color):
        self.color = new_color
        
    def time_step(self): # the values corresponding to the previous time step are updated
        self.r_prev = self.r.copy()
        self.v_prev = self.v.copy()
        
    def show_data(self):
        print('Name: ' + self.name)
        print('Mass = ' + str(self.m) + 'kg')
        print('Radius = ' + str(self.R) + 'm')
        print('r = [' + str(self.r[0]) + ', ' + str(self.r[1]) + ', ' + str(self.r[2]) + ']m')
        print('v = [' + str(self.v[0]) + ', ' + str(self.v[1]) + ', ' + str(self.v[2]) + ']m/s')
    