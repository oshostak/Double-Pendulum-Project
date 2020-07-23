README

This is a readme file for Oleh Shostak's Double Rod Pendulum project.

In my project, I made a simulation of a double rod pendulum motion. This is an illustration to a mathematical phenomena
concerning a system of 2+ elements. In such a system, the position of the system elements cannot be predicted exactly,
because our results strongly rely on our measured data, which always had a margin of error. This is why people use 
computer simulations (like this one) to approximate the state of the system at a given time.

In the file named "dp_animation.py", I set up the basic equasions for a double rod pendulum elements and made an animation
that simply illustrates how the system works. The animation works with 400 points, each being registered at a rate of 0.05 
seconds per one position. The time measurment in this case represent the margin of error for the positioning of the elements
in this simulation. The animations goes for 20 seconds and then repeats itself.

In the file named "dp_stationary_scattering.py", I made a scatterplot with fixed points of mass_1 and mass_2 positions. This
graph represents the location distribution for both masses and illustrates the movement for the mass_1, which was not included
in the animated illustration. 400 point on the scatterplot help a reader understand the general pattern of the pendulum's 
movement.

In the file named "dp_stationary_randomizing.py", I made a simulation that operates with a particular number of random starting
angles. That being said, the position of the pendulum's masses is being varied N times (the lengths of the levers and masses 
are stable, however). N runs of the 'for' loop that I set up produce 400N points appended on the scatterplot. After running the
randomized version for a bunch of times, a user can see that the general patter always stays the same.

The libraries I used:

- NumPy
- SciPy
- Matplotlib.Pyplot
- Random

The source I used:
matplotlib.org/examples/animation/double_pendulum_animated.html