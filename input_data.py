# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:07:43 2022

@author: Mario Gayete Ibáñez
"""
# Import classes
from planet_class import planet
from constants_class import constant_parameters

# Import 
import os 

def input_data(input_folder):
    
    # Read the constants
    constants = constants_reading(input_folder + 'Constants.txt')
    
    # Read the bodies input data
    bodies = bodies_reading(input_folder + 'Planets/')
    return constants, bodies

def constants_reading(filename):
    # Initialize the constants class
    constants = constant_parameters()
    f = open(filename, "r")

    for line in f.readlines():
        constant_name, value = read_assignment(line)
        
        # Constant allocation
        constants.allocate_values(constant_name, value)
    
    return constants

def bodies_reading(folder):
    # Initialize the matrix
    bodies = []
    # Read all the txt except for the 'Template.txt'
    all_files = os.listdir(folder)
    
    for file in all_files:
        # Initialize the parameters needed
        planet_name = ''
        planet_mass = 0
        position = [0,0,0]
        velocity = [0,0,0]
        planet_radius = 0
        colour_representation = 'k'
        
        if file != 'Template.txt': # The template file is not read
            f = open(folder + file, "r")
            for line in f.readlines():
                constant_name, value = read_assignment(line)
                
                # Constant allocation
                if constant_name == 'NAME':
                    planet_name = value
                elif constant_name == 'MASS':
                    planet_mass = float(value)
                elif constant_name == 'RADIUS':
                    planet_radius = float(value)
                elif constant_name == 'Rx':
                    position[0] = float(value)
                elif constant_name == 'Ry':
                    position[1] = float(value)
                elif constant_name == 'Rz':
                    position[2] = float(value)
                elif constant_name == 'Vx':
                    velocity[0] = float(value)
                elif constant_name == 'Vy':
                    velocity[1] = float(value)
                elif constant_name == 'Vz':
                    velocity[2] = float(value)
                elif constant_name == 'COLOUR':
                    
                    colour_representation = value
                elif constant_name != None:
                    raise Exception("The following constant is not implemented: "  + constant_name)
            
            bodies.append(planet( planet_name, planet_mass, planet_radius, position, velocity))
            bodies[-1].color_representation(colour_representation)
    
    return bodies

def read_assignment(line):
    constant_name = []
    value = []
    
    if line[0] == '#' or line[0] == '\n': # it is a commentary or and empty line

        return None, None
    else:
        constant_name = read_before_equal(line)
        value = read_after_equal(line)
    
    return constant_name, value

def read_before_equal(line):
    content = ''
    
    found_equal = False
    index_line = 0
    
    # Save all the content before the equal
    while found_equal == False:
        content += line[index_line]
        index_line += 1
        
        if line[index_line] == '=':
            found_equal = True
    
    # Delete the white spaces before the equal
    all_deleted = False
    while all_deleted == False:
        if content[-1] == ' ':
            content = content[:-1]
        else:
            all_deleted = True
    return content

def read_after_equal(line):
    content = ''
    
    found_equal = False
    found_end = False
    found_endl = False
    index_line = 0
    index_equal = 0
    
    # Save all the content before the equal
    while found_end == False and found_endl == False:
        
        
        # If we are on the right side of the equal, we start saving the data
        if found_equal == True:
            content += line[index_line]
            
        
        # Check if the equal has been found
        if line[index_line] == '=':
            found_equal = True
            index_equal = index_line
        
        # Index update
        index_line += 1
        
        # Check if the end of the line is reached
        if index_line >= len(line):
            found_endl = True 
        
        # Check if the comentary sign '#' has been found
        elif line[index_line] == '#':
            found_end = True

    # Delete the '\n'
    if found_endl == True:
        content = content[:-1]
    
    # Delete the white spaces right after the equal
    all_deleted = False
    while all_deleted == False:
        if content[0] == ' ':
            content = content[1:]
        else:
            all_deleted = True
                 
    
    # Delete the white spaces at the end
    all_deleted = False
    while all_deleted == False:
        if content[-1] == ' ':
            content = content[:-1]
        else:
            all_deleted = True
    
    
    
    return content
    
        
        