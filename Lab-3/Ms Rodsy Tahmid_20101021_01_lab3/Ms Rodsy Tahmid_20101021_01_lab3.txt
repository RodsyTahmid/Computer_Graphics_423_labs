from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def drawpoints(x, y):
	glPointSize(1.5) #pixel size. by default 1 thake
	glBegin(GL_POINTS)
	glVertex2f(x, y) #jekhane show korbe pixel
	glEnd()

def midpoint_circle(x0, y0, r): #value = x0, y0
	d = 1 - r #initial d
	x = 0
	y = r
	Circlepoints(x, y, x0, y0)
	while (x < y):
	    # Choose E #East
	    if d < 0:
		    d = d + 2 * x + 3
		    x = x + 1
	    else: # d >= 0
	    # Choose SE #South-East
		    d = d + 2 * x - 2 * y + 5
		    x = x + 1
		    y = y - 1
	    Circlepoints(x, y, x0, y0)

def Circlepoints(x, y, x0, y0):
	drawpoints(x + x0, y + y0) #WritePixel(x, y, value) #zone 0
	drawpoints(y + x0, x + y0) #WritePixel(y, x, value) #zone 1
	drawpoints(y + x0, -x + y0) #WritePixel(y, -x, value) #zone 2 #zone-any to zone-0
	drawpoints(x + x0, -y + y0) #WritePixel(x, -y, value) #zone 7
	drawpoints(-x + x0, -y + y0) #WritePixel(-x, -y, value) #zone 4
	drawpoints(-y + x0, -x + y0) #WritePixel(-y, -x, value) #zone 5
	drawpoints(-y + x0, x + y0) #WritePixel(-y, x, value) #zone 6 #zone-any to zone-0
	drawpoints(-x + x0, y + y0) #WritePixel(-x, y, value)

def draw_circle(x, y, r): #by using 8-way symmetry
	# Main outer circle
	midpoint_circle(x, y, r)
	# Right inner circle
	midpoint_circle(x + (r / 2), y, r / 2)
	# Left inner circle
	midpoint_circle(x - (r / 2), y, r / 2)
	# Top inner circle
	midpoint_circle(x, y + (r / 2), r / 2)
	# Bottom inner circle
	midpoint_circle(x, y - (r / 2), r / 2)
	# NE circle #north-east
	x0 = x + (r / 2) - 18
	y0 = y + (math.sin(45) * r / 2) - 18
	midpoint_circle(x0, y0, r / 2)
	# NW circle #north-west
	x0 = x - (r / 2) + 18
	y0 = y + (math.sin(45) * r / 2) - 18
	midpoint_circle(x0, y0, r / 2)
	# SW circle #south-west
	x0 = x - (r / 2) + 18
	y0 = y - (math.sin(45) * r / 2) + 18
	midpoint_circle(x0, y0, r / 2)
	# SE circle #south-east
	x0 = x + (r / 2) - 18
	y0 = y - (math.sin(45) * r / 2) + 18
	midpoint_circle(x0, y0, r / 2)

def iterate():
	glViewport(0, 0, 500, 500)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def showscreen():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	iterate()
	glColor3f(1.0, 1.0, 0) #konokichur color set (RGB)
	#call the draw methods here
	draw_circle(300, 300, 150)
	glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab03Task_midpoint_circle") #window name
glutDisplayFunc(showscreen)

glutMainLoop()