#!/usr/bin/env python3
#
# particle in a 2D box of size 0->L and 0->L
#
# The wavefunction is
# psi ~ sin(nx * kx * x) * sin(ny * ky * y)
# with
# nx and ny as integers > 0
# kx = pi/L and ky=pi/L
#
# CC 10-Oct-2018
# Better labels CC 29-Jan-2019
#-------------------------
import numpy as np
import matplotlib.pyplot as plt
import math

# Hardwired for now
nx = 5
ny = 2
dx = 1
dy = 1

# number of steps in x and y
bx = 1000
by = 1000

# The color map..pick whatever you like
# More choices here
# https://matplotlib.org/examples/color/colormaps_reference.html
thisMap = "jet"
#thisMap = "brg"
#thisMap = "terrain"
#thisMap = "gnuplot"
#thisMap="ocean"
#thisMap ="brg"

# See comments at the top for definition of kx and ky
kx = math.pi/dx
ky = math.pi/dy

# The x and y ranges
x  = np.arange(0, dx+dx/bx, dx/bx)
y  = np.arange(0, dy+dy/by, dy/by)

# The sin(kx*x) and sin(ky*y)
sx = np.sin(nx*kx*x)
sy = np.sin(ny*ky*y)

# Wavefunction squared
psi2 = np.zeros( (bx,by) )

# Brute force
#for ix in range(0, len(x)-1):
#    for iy in range(0, len(y)-1):
#        psi2[ix, iy] = sx[ix]*sy[iy]*sx[ix]*sy[iy]

# Smart way which is equivalent to brute force but faster
psi2 = np.outer( (sx*sx) , (sy*sy))

# Stupid thing: when putting it on the screen
# the 1st index is the column and the 2nd index is the
# row.  So in order to really have [ix, iy] we need to
# transpose before plotting.
# Even more stupid: the vertical dimension increases
# from the top, not from the bottom.  The "flipud" function
# chnges the order of the rows
psi2 = np.flipud(psi2.transpose())

# now plot        
f1, ax1 = plt.subplots()
picture = ax1.imshow(psi2, cmap=thisMap, interpolation="nearest")
# ax1.axis("off")   
picture = ax1.imshow(psi2, cmap=thisMap, origin='lower', aspect='auto')
f1.colorbar(picture)
ax1.set_xlabel("X-coordinate")
ax1.set_ylabel("Y-coordinate")
ax1.set_title("Particle in a box")

# Customize the labels
ax1.locator_params(nbins=2)            # 2 ticks only, both x any axes
ax1.set_xticklabels( ('', '0', 'L') )  # not quite sure why it wants 3?
ax1.set_yticklabels( ('', '0', 'L') )  # not quite sure why it wants 3?

f1.show()


input("Press Enter to continue...")   
 
