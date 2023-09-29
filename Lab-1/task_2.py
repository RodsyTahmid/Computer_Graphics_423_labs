from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()
def draw_triangles():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 1.0, 0.25)  # konokichur color set (RGB)
    glVertex2f(100,500) #the left point
    glVertex2f(300,700) #jekhane show korbe pixel
    glVertex2f(500,500) #the right point

   #inner
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(115,505) #the left point
    glVertex2f(300,690) #jekhane show korbe pixel
    glVertex2f(485,505) #the right point
    glEnd()

def draw_lines():
    glBegin(GL_LINES)
    glColor3f(0.5, 1.0, 0.25)  # konokichur color set (RGB)
    glVertex2f(100,500)#high left
    glVertex2f(100,100)#low left

    glVertex2f(500,500)#high right
    glVertex2f(500,100)#low right

    glVertex2f(100,100)#low left
    glVertex2f(500,100)#low right

    #door
    glVertex2f(250,100)#low left
    glVertex2f(250,250)#high left

    glVertex2f(350,100)#low right
    glVertex2f(350,250)#high right

    glVertex2f(250,250)#high left
    glVertex2f(350,250)#high right

    #window left
    glVertex2f(145,425)#high left
    glVertex2f(245,425)#high right

    glVertex2f(145,325)#low left
    glVertex2f(245,325)#low right

    glVertex2f(145,425)#high left
    glVertex2f(145,325)#low left

    glVertex2f(245,425)#high right
    glVertex2f(245,325)#low right

    #window right
    glVertex2f(355,425)#high left
    glVertex2f(455,425)#high right

    glVertex2f(355,325)#low left
    glVertex2f(455,325)#low right

    glVertex2f(355,425)#high left
    glVertex2f(355,325)#low left

    glVertex2f(455,425)#high right
    glVertex2f(455,325)#low right

    glEnd()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.5, 1.0, 0.25) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(330, 175)

    glColor3f(0.5, 1.0, 0.25)  # konokichur color set (RGB)
    draw_triangles()

    draw_lines()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
