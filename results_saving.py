# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""

import os
from datetime import datetime

def save_positions(name, time, position, writing_mode, output_folder = 'Results/', subfolder = 'Position_and_time/'):
    # Build the results folder if it doesn't exist
    if os.path.isdir(output_folder) == False:
        os.mkdir(output_folder)
        
    # Directories organisation
    current_date = datetime.now()
    current_datename = str(current_date.year) + str(current_date.month) + str(current_date.day)
    
    output_folder += current_datename + '/'
    
    # Build the results folder with the current date subfolder if it doesn't exist
    if os.path.isdir(output_folder) == False:
        os.mkdir(output_folder)    
    
    # Make the directory if it doesn't exist
    if os.path.isdir(output_folder + subfolder) == False:
        os.mkdir(output_folder + subfolder)
    
    # Open the document where the results are saved
    filename = output_folder + subfolder + name + '.txt'
    
    file = open(filename, writing_mode)
    
    # Write the data in the file
    # The data will be organized in columns as: 'time', 'x-position', 'y-position', 'z-position'
    # Each row will correspond to a single time interval
    
    file.write(str(time) + '\t')
    
    for dim_content in position:
        file.write(str(dim_content) + '\t') # save in m
        #file.write(str(dim_content/1.496e11) + '\t') # save in UA
    
    file.write('\n')
    file.close()
    
    
    
    
