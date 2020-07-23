#importing libraries

import numpy as np
from numpy import sin, cos
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#initial data

lever_1 = 1.0
lever_2 = 1.0
mass_1 = 1.0
mass_2 = 1.0
gravity = 9.8
angle_1 = 180.0
angle_2 = 180.0
velocity_1 = 0.0
velocity_2 = 0.0

dt = 0.05 #important point here = this is a margin of error for the system and the time slicing rate
time = np.arange(0.0, 20, dt)

state = np.radians([angle_1, velocity_1, angle_2, velocity_2])

#a function for finding derivatives of the system at each 0.05 sec interval (ref. to line 20)
#I took the fomulas from this source matplotlib.org/examples/animation/double_pendulum_animated.html, I also used the code idea when
#thinking about how I was going to do this

def Find_Derivative(state, time):

	dydx = np.zeros_like(state)
	dydx[0] = state[1]
	delta = state[2] - state[0]

	den1 = (mass_1 + mass_2)*lever_1 - mass_2*lever_1*cos(delta)*cos(delta)

	dydx[1] = (mass_2*lever_1*state[1]*state[1]*sin(delta)*cos(delta) + mass_2*gravity*sin(state[2])*cos(delta) + mass_2*lever_2*state[3]*state[3]*sin(delta) - (mass_1 + mass_2)*gravity*sin(state[0]))/den1
	dydx[2] = state[3]
	den2 = (lever_2/lever_1)*den1
	dydx[3] = (-mass_2*lever_2*state[3]*state[3]*sin(delta)*cos(delta) + (mass_1 + mass_2)*gravity*sin(state[0])*cos(delta) - (mass_1 + mass_2)*lever_1*state[1]*state[1]*sin(delta) - (mass_1 + mass_2)*gravity*sin(state[2]))/den2

	return dydx

#I'm using the SciPy module and its integration function

y = integrate.odeint(Find_Derivative, state, time)

#this actually creates lists of data that could be printed/plotted individually, and that's what I do next

x1 = lever_1*sin(y[:, 0])
y1 = -lever_1*cos(y[:, 0])

x2 = lever_2*sin(y[:, 2]) + x1
y2 = -lever_2*cos(y[:, 2]) + y1

#setting up a figure in matplotlyb and appending each pair of positions for both pendulum masses (x1,y1) and (x2,y2)

figure = plt.figure()
axis = figure.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
axis.grid()
axis.scatter(0, 0, color='green') #marking the origin
axis.scatter(x1, y1)
axis.scatter(x2, y2, color='red') #just used different color to make things clear


plt.show()