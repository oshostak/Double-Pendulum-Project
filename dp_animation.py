#importing libraries

import numpy as np
from numpy import sin, cos
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setting up initial data

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

#a function for finding derivatives of the system at each 0.05 sec interval (ref. to line 21)
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

	return dydx #it returns an array of data

#next two functions are needed for enabling animation

def Initiate_Data():
	line.set_data([], [])
	time_text.set_text('')
	return line, time_text

#appends points from respectable lists (x1,x2,y1,y2), elements of which are inner lists containing two elements each

def Animation_Create(i):
	thisx = [0, x1[i], x2[i]]
	thisy = [0, y1[i], y2[i]]
	line.set_data(thisx, thisy)
	time_text.set_text(time_template % (i*dt))
	return line, time_text

#I'm using the SciPy module and its integration function

y = integrate.odeint(Find_Derivative, state, time)

#this actually creates lists of data that could be printed/plotted individually

x1 = lever_1*sin(y[:, 0])
y1 = -lever_1*cos(y[:, 0])

x2 = lever_2*sin(y[:, 2]) + x1
y2 = -lever_2*cos(y[:, 2]) + y1

#creating a figure withing matplotlyb, it's pretty simple

figure = plt.figure()
axis = figure.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
axis.grid()

line, = axis.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = axis.text(0.05, 0.9, '', transform=axis.transAxes)

animation_picture = animation.FuncAnimation(figure, Animation_Create, np.arange(1, len(y)),
                              interval=25, blit=True, init_func=Initiate_Data)

plt.show()