# Based heavily on an example in the Pygame documentation:
# http://www.pygame.org/docs/ref/joystick.html

import pygame
import serial

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class TextPrinter:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printToScreen(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10

ser = serial.Serial(3)
pygame.init()
 
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Quadcopter Controller")

done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrinter = TextPrinter()

while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)
    textPrinter.reset()

    joystick_count = pygame.joystick.get_count()
    textPrinter.printToScreen(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrinter.indent()
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrinter.printToScreen(screen, "Joystick {}".format(i) )
        textPrinter.indent()
    
        name = joystick.get_name()
        textPrinter.printToScreen(screen, "Joystick name: {}".format(name) )
        
        axes = joystick.get_numaxes()
        textPrinter.printToScreen(screen, "Number of axes: {}".format(axes) )
        textPrinter.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrinter.printToScreen(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrinter.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrinter.printToScreen(screen, "Number of buttons: {}".format(buttons) )
        textPrinter.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrinter.printToScreen(screen, "Button {:>2} value: {}".format(i,button) )
        textPrinter.unindent()
            
        hats = joystick.get_numhats()
        textPrinter.printToScreen(screen, "Number of hats: {}".format(hats) )
        textPrinter.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrinter.printToScreen(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrinter.unindent()
        
        textPrinter.unindent()

    pygame.display.flip()

    ser.write("W")
    ser.read()

    clock.tick(20)
    
ser.close()
pygame.quit()