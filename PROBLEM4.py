#PROBLEM 4-PYTHON
import matplotlib.pyplot as plot
import numpy as np
import math as math
HEIGHT = float(input('Please input the Height: '))
VELO = float(input('Please input the velocity: '))
ANGLE = float(input('Please input the angle in degrees: '))
Ax = float(input('Please input the horizontal component of the acceleration: '))
Ay = float(input('Please input the vertical component of the acceleration: '))
if Ay == 0:
    raise NameError('ERROR!Zero verical acceleration results to non-existence of free-fall motion')   
THETA = math.radians(ANGLE) 
a = [Ay/2, (VELO*math.sin(THETA)), HEIGHT]
b = max(np.roots(a))
c = np.arange(0,b,0.1)
x = np.zeros((len(c),1))
y = np.zeros((len(c),1))
t = 0.1
y[0,0] = HEIGHT
n = np.arange(0,len(c),1)
for i in n:
    RXt = (Ax*(t**2))/2 + (VELO*math.cos(THETA))*t
    RYt = (Ay*(t**2))/2 + (VELO*math.sin(THETA))*t + HEIGHT
    x[i,0] = RXt
    y[i,0] = RYt
    t=t+0.1 
plot.plot(x,y)
plot.grid()
plot.xlabel('Horizontal Distance')
plot.ylabel('Vertical Distance')
plot.title('PROBLEM 4')