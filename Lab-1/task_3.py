from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_lines():
    glLineWidth(5)  # pixel size. by default 1 thake
    glBegin(GL_LINES)
    glColor3f(0.5, 1.0, 0.25)# 2  # konokichur color set (RGB)
    glVertex2f(25,425)
    glVertex2f(100,425)

    glVertex2f(25,425)
    glVertex2f(25,500)

    glVertex2f(25,500)
    glVertex2f(100,500)

    glVertex2f(100,500)
    glVertex2f(100,575)

    glVertex2f(100,575)
    glVertex2f(25,575)
#########
    glColor3f(0.0, 0.5, 1.0)  # 0  # konokichur color set (RGB)
    glVertex2f(125, 425)
    glVertex2f(125, 575)

    glVertex2f(125, 425)
    glVertex2f(200, 425)

    glVertex2f(200, 425)
    glVertex2f(200, 575)

    glVertex2f(200, 575)
    glVertex2f(125, 575)
#########
    glColor3f(1.0, 0.5, 0.0)  # 1  # konokichur color set (RGB)
    glVertex2f(225, 575)
    glVertex2f(225, 425)
#########
    glColor3f(0.0, 1.0, 1.0)  # 0  # konokichur color set (RGB)
    glVertex2f(250, 425)
    glVertex2f(250, 575)

    glVertex2f(250, 425)
    glVertex2f(325, 425)

    glVertex2f(325, 425)
    glVertex2f(325, 575)

    glVertex2f(325, 575)
    glVertex2f(250, 575)
#########
    glColor3f(1.0, 1.0, 0.0)  # 1  # konokichur color set (RGB)
    glVertex2f(350, 575)
    glVertex2f(350, 425)
    #########
    glColor3f(1.0, 0.0, 1.0)  # 0  # konokichur color set (RGB)
    glVertex2f(375, 425)
    glVertex2f(375, 575)

    glVertex2f(375, 425)
    glVertex2f(450, 425)

    glVertex2f(450, 425)
    glVertex2f(450, 575)

    glVertex2f(450, 575)
    glVertex2f(375, 575)
#########
    glColor3f(1.0, 0.0, 0.25)  # 2  # konokichur color set (RGB)
    glVertex2f(475, 425)
    glVertex2f(550, 425)

    glVertex2f(475, 425)
    glVertex2f(475, 500)

    glVertex2f(475, 500)
    glVertex2f(550, 500)

    glVertex2f(550, 500)
    glVertex2f(550, 575)

    glVertex2f(550, 575)
    glVertex2f(475, 575)
    ########
    glColor3f(1.0, 0.9, 0.7)  # 1  # konokichur color set (RGB)
    glVertex2f(575, 575)
    glVertex2f(575, 425)
    #########
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
    #call the draw methods here

    draw_lines()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()