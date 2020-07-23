#importing libraries

import numpy as np
from numpy import sin, cos
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import random

#initial data

velocity_1 = 0.0
velocity_2 = 0.0
lever_1 = 1.0
lever_2 = 1.0
mass_1 = 1.0
mass_2 = 1.0
gravity = 9.8

dt = 0.05 #important point here = this is a margin of error for the system and the time slicing rate
time = np.arange(0.0, 300, dt)

#setting up the figure first

figure = plt.figure()
axis = figure.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
axis.grid()

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

#setting up a "for" loop. n runs of the loop give us n combinations of two random starting angles measured from 0 to 360

for i in range(10):

	angle_1 = 179
	angle_2 = 179

	state = np.radians([angle_1, velocity_1, angle_2, velocity_2])

	y = integrate.odeint(Find_Derivative, state, time)

	x1 = lever_1*sin(y[:, 0])
	y1 = -lever_1*cos(y[:, 0])

	x2 = lever_2*sin(y[:, 2]) + x1
	y2 = -lever_2*cos(y[:, 2]) + y1
	
	axis.scatter(0, 0, color='green')
	axis.scatter(x2, y2, color='red') #i'm tracking olny the mass_2, which is the farest mass on the double pendulum

plt.show()
