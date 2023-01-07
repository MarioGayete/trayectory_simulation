# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:00 2022

@author: Mario Gayete Ibáñez
"""
# Import libraries
from numpy import *

# Import functions
from mathematical_operations import *
from results_saving import *

def temporal_solver(bodies, G, At, t_max, At_save, beta, EPSILON, max_it):
    # Time initialization
    t = 0
    writing_mode = 'w'
    for current_body in bodies:
        save_positions(current_body.name, t, current_body.r, writing_mode)
    writing_mode = 'a'
    
    # Temporal loop
    while t < t_max:
        print('Current time step = ' + str(t) + ' seconds')
        # Solve the new position
        bodies = direct_solver(bodies, G, At, beta, EPSILON, max_it)
        
        # New time step
        t += At
        for i_body in range(0,len(bodies)):
            bodies[i_body].time_step()
        
        # Save the results
        if int((t-At)/At_save) != int(t/At_save):
            for current_body in bodies:
                save_positions(current_body.name, t, current_body.r, writing_mode)
      
    return 0


def direct_solver(bodies, G, At, beta, epsilon, max_it):
    
    # Iterative solver --> Gauss-Seidel (point-by-point)
    final = False
    
    # Initial guess --> considering constant acceleration
  
    for i_body in range(0,len(bodies)):
        bodies[i_body].accel = specific_force_computation(bodies, i_body, G)
        bodies[i_body].r, bodies[i_body].v = time_step_movement( bodies[i_body].r_prev,  bodies[i_body].v_prev,
                                              0, bodies[i_body].accel, bodies[i_body].accel, At)

        bodies[i_body].r_guess =  bodies[i_body].r
        bodies[i_body].v_guess =  bodies[i_body].v
        
    # Iterative process
    it = 0
    while final == False:
        # Compute the movement
        for i_body in range(0,len(bodies)):
            # Compute the accelerations
            bodies[i_body].accel = specific_force_computation(bodies, i_body, G)
            bodies[i_body].accel_prev = specific_force_computation_prev(bodies, i_body, G)
            # Compute the new position
            bodies[i_body].r, bodies[i_body].v = time_step_movement( bodies[i_body].r_prev,  bodies[i_body].v_prev,
                                                  beta, bodies[i_body].accel, bodies[i_body].accel_prev, At)
            
        # Check convergence
        final = convergence_check(bodies, epsilon)
        
        # If the convergence is no achieved, the a new iteration is needed
        if final == False:
            it += 1
            for i_body in range(0,len(bodies)):
                bodies[i_body].iteration_step()
        
        # 
        if max_it < it:
            raise Exception("No convergence achieved. Time step (At) too big. Try a smaller one.")
        

    return bodies

def specific_force_computation(bodies, current_body, G):
    f = [0.0, 0.0, 0.0]
    for i in range(0,len(bodies)):
        if i != current_body:
            vector = bodies[i].r - bodies[current_body].r
            #print(bodies[i].r)
            f = sum_vectors(f , dot(G * bodies[i].m / mod_vector(vector)**3, vector))

    return f

def specific_force_computation_prev(bodies, current_body, G):
    f = [0.0, 0.0, 0.0]
    for i in range(0,len(bodies)):
        if i != current_body:
            vector = bodies[i].r_prev - bodies[current_body].r_prev
            f = sum_vectors(f , dot(G * bodies[i].m / mod_vector(vector)**3, vector))
            
    return f

def time_step_movement(r0, v0, beta, f, f_ant, At):
    rf = r0.copy()
    vf = v0.copy()
    for i_dim in range(0,len(r0)):
        rf[i_dim] += v0[i_dim]*At + At**2/2 * (beta*f[i_dim] + (1-beta) * f_ant[i_dim])
        vf[i_dim] += At * (beta*f[i_dim] + (1-beta) * f_ant[i_dim])

    return rf, vf

def convergence_check(bodies, epsilon):
    max_error = 0
    i_max = 0
    for i_body in range(0,len(bodies)):
        for i_dim in range(0,len(bodies[0].r)):
            #if abs(bodies[i_body].r[i_dim] - bodies[i_body].r_guess[i_dim]) > max_error:
            #    i_max = i_body
            
            max_error = max(max_error, abs(bodies[i_body].r[i_dim] - bodies[i_body].r_guess[i_dim]))
            if abs(bodies[i_body].r[i_dim] - bodies[i_body].r_guess[i_dim]) > epsilon: # no convergence achieved
                return False
    '''if max_error > epsilon:
        print(max_error)
        print(i_max)
        print(bodies[i_max].r)
        print(bodies[i_max].r_guess)
        print(bodies[i_max].r - bodies[i_max].r_guess)
        input('...')
        return False
    '''
    return True # if we finish the loop, then the convergence is achieved
        
        
    
        
            
            
    
    
    
