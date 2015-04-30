import picamera
from time import sleep
import pygame
import random
import pygame, Buttons
from pygame.locals import *

WIDTH=1280
HEIGHT=720
FONTSIZE=50
# INIT CAMERA
camera = picamera.PiCamera()
camera.vflip = False
camera.hflip = False
camera.brightness = 60

# BUILD A SCREEN
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
color = pygame.Color(255, 255, 255)
textcol = pygame.Color(255, 255, 0)
screen.fill(color)

class Button_Example:
	def __init__(self):
		self.main()
    
    #Create a display
	def display(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
		pygame.display.set_caption("KJCam Plus - Premium Edition")

    #Update the display and show the button
	def update_display(self):
        #Parameters:               surface,      color,       x,   	y,  length, height, width,    text,      text_color
		self.Button2.create_button(self.screen, (107,142,35), 0, 	0, 	200,    50,    	0,        "Capture", (255,255,255))
		self.Button1.create_button(self.screen, (107,142,35), 210, 	0, 	200,    50,    	0,        "Close  ", (255,255,255))	
		pygame.display.flip()


    #Run the loop
	def main(self):
		self.Button1 = Buttons.Button()
		self.Button2 = Buttons.Button()
		self.display()
		self.update_display()
		while True:            
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == MOUSEBUTTONDOWN:
					if self.Button1.pressed(pygame.mouse.get_pos()):
						pygame.quit()
					if self.Button2.pressed(pygame.mouse.get_pos()):
						camera.resolution = (WIDTH, HEIGHT)
						camera.start_preview()
						sleep(1)
						camera.capture('hello.jpg',resize=(WIDTH,HEIGHT))			    
						camera.stop_preview()			
						img = pygame.image.load('hello.jpg')
						screen.blit(img,(0,0))
						pygame.display.flip()
						self.update_display()

if __name__ == '__main__':
	obj = Button_Example()
