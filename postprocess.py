# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""

# Import functions
import numpy as np
import os
from datetime import datetime
import matplotlib.pyplot as plt
import cv2

def position_3Drepresentation(bodies, results_folder = 'Results/', input_subfolder = 'Position_and_time/', 
                            output_subfolder = 'Images/', output_video = 'Video/'): 
    
    
    # Directories organisation
    current_date = datetime.now()
    current_datename = str(current_date.year) + str(current_date.month) + str(current_date.day)
    
    results_folder += current_datename + '/'
    
    # Make the directory if it doesn't exist
    if os.path.isdir(results_folder + output_subfolder) == False:
        os.mkdir(results_folder + output_subfolder)
        
    
    # Check the matrix dimensions to create the global array
    current_filename = results_folder + input_subfolder + bodies[0].name + '.txt'
    current_matrix = np.loadtxt(current_filename)
    
    N_timesteps = current_matrix.shape[0]
    N_dim = current_matrix.shape[1] - 1 
    global_position = np.zeros((N_timesteps, N_dim, len(bodies)))
    t_vec = current_matrix[:,0]
        
    
    # Plot the movement for every body
    
    for i_body in range(0,len(bodies)):
        # Read the filename
        current_filename = results_folder + input_subfolder + bodies[i_body].name + '.txt'
        current_matrix = np.loadtxt(current_filename)
        
        for i_t in range(0,N_timesteps):
            for i_dim in range(0,N_dim):
                global_position[i_t, i_dim, i_body] = current_matrix[i_t, i_dim + 1]
            
              
    # Plotting the results
    for i_frame in range(0,current_matrix.shape[0]):
        fig = plt.figure()
        ax =  plt.axes(projection='3d')
        
        for i_body in range(0,len(bodies)):
            # Plot the current position
            ax.plot3D(global_position[i_frame,0,i_body],global_position[i_frame,1,i_body],
                      global_position[i_frame,2,i_body], marker = '.', c = bodies[i_body].color, markersize = 15)
            draw_trajectory(global_position[:,:,i_body], bodies[i_body].color, ax)
        
        ax.set_xlim([-1.5,1.5])
        ax.set_ylim([-1.5,1.5])
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('t = ' + str(round(t_vec[i_frame]/3600/24,2)) + ' days')
        
        plt.savefig(results_folder + output_subfolder + str(i_frame) + '.jpg')
        plt.close()
    
    # Generating the video from the plots
    video_generation_from_images(results_folder + output_video + 'video3D.avi', results_folder + output_subfolder, 
                                 current_matrix.shape[0])
    
    return 0
        
        


def position_2Drepresentation(bodies, results_folder = 'Results/', input_subfolder = 'Position_and_time/', 
                            output_subfolder = 'Images_2D/', output_video = 'Video/' ): 
    
    
    # Directories organisation
    current_date = datetime.now()
    current_datename = str(current_date.year) + str(current_date.month) + str(current_date.day)
    
    results_folder += current_datename + '/'
    
    # Make the directory if it doesn't exist
    if os.path.isdir(results_folder + output_subfolder) == False:
        os.mkdir(results_folder + output_subfolder)
    
    # Make the directory if it doesn't exist
    if os.path.isdir(results_folder + output_video) == False:
        os.mkdir(results_folder + output_video)
        
    
    # Check the matrix dimensions to create the global array
    current_filename = results_folder + input_subfolder + bodies[0].name + '.txt'
    current_matrix = np.loadtxt(current_filename)
    
    N_timesteps = current_matrix.shape[0]
    N_dim = current_matrix.shape[1] - 1 
    global_position = np.zeros((N_timesteps, N_dim, len(bodies)))
    t_vec = current_matrix[:,0]
        
    
    # Plot the movement for every body
    
    for i_body in range(0,len(bodies)):
        # Read the filename
        current_filename = results_folder + input_subfolder + bodies[i_body].name + '.txt'
        current_matrix = np.loadtxt(current_filename)
        
        for i_t in range(0,N_timesteps):
            for i_dim in range(0,N_dim):
                global_position[i_t, i_dim, i_body] = current_matrix[i_t, i_dim + 1]
            
              
    # Plotting the results
    for i_frame in range(0,current_matrix.shape[0]):
        fig, ax = plt.subplots()
        
        for i_body in range(0,len(bodies)):
            # Plot the current position
            ax.plot(global_position[i_frame,0,i_body],global_position[i_frame,1,i_body],
                      marker = '.', c = bodies[i_body].color, markersize = 15)
            draw_trajectory(global_position[:,:-1,i_body], bodies[i_body].color, ax)
        
        ax.set_xlim([-1.5,1.5])
        ax.set_ylim([-1.5,1.5])
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('t = ' + str(round(t_vec[i_frame])) + ' s')
        #ax.set_title('t = ' + str(round(t_vec[i_frame]/3600/24,2)) + ' days')
        
        plt.savefig(results_folder + output_subfolder + str(i_frame) + '.jpg')
        plt.close()
    
    # Generating the video from the plots
    video_generation_from_images(results_folder + output_video + 'video2D.avi', results_folder + output_subfolder, 
                                 current_matrix.shape[0])
    
    return 0

def draw_trajectory(matrix, ccolor, ax):
    
    if matrix.shape[1] == 2: # 2D representation
        x_vector = matrix[:,0]
        y_vector = matrix[:,1]
        
        ax.plot(x_vector,y_vector, linewidth = 0.5,c=ccolor)
    
    elif matrix.shape[1] == 3: # 3D representation
        x_vector = matrix[:,0]
        y_vector = matrix[:,1]
        z_vector = matrix[:,2]
        
        ax.plot3D(x_vector,y_vector, z_vector, linewidth = 0.5, c=ccolor)
    
        
def video_generation_from_images(output_filename, input_folder, N_images):
    img_array = []
    for i_file in range(0,N_images):
        img = cv2.imread(input_folder + str(i_file) + '.jpg')
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    
    out = cv2.VideoWriter(output_filename,cv2.VideoWriter_fourcc(*'DIVX'), 60, size)
     
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    
    return 0

        


