# trayectory_simulation
This is a first version of a Python code that solves numerically the gravitational problem of N-bodies. It is intended to be further developed so transfer orbit optimization could be carried out.

The input data for the simulation can be found in the "Inputs/" folder. The document "Constants.txt" corresponds to the numerical parameters of the solver, such as the time step or the numerical integration method.
In the subfolder "Planets/", there will be as many .txt files as planets in the problem. Use the template document to have a reference of the input format.

As a results, it generates a folder called results, where a video of the orbit can be found in a 2D plane or in a 3D plot, along with its different frames and with the results saved in a text file for the different planets.
