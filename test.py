import picamera,io
from time import sleep
import pygame
import random
import pygame, Buttons
from pygame.locals import *
import StringIO
from PIL import Image
import datetime

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

class KJCam:
	def __init__(self):
		self.main()
    
    #Create a display
	def display(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
		pygame.display.set_caption("KJCam Plus - Premium Edition")

    #Update the display and show the button
	def update_display(self):
        #Parameters:               surface,      color,       x,   	y,  length, height, width,    text,      text_color
		self.Button2.create_button(self.screen, (107,142,35), 700, 	600, 	200,    50,    	0,        "Capture", (255,255,255))
		self.Button1.create_button(self.screen, (107,142,35), 910, 	600, 	200,    50,    	0,        "Close  ", (255,255,255))	
		pygame.display.flip()


    #Run the loop
	def main(self):
		self.Button1 = Buttons.Button()
		self.Button2 = Buttons.Button()
		self.display()
		self.update_display()


		while True:
			stream = io.BytesIO() # Capture into in-memory stream
			camera.capture(stream, 'jpeg')
			camera.resolution = (480,320)
			stream.seek(0)
			image = Image.open(stream)
			image.save('preview.bmp',quality=10)
			image = pygame.image.load('preview.bmp')
			screen.blit(image,(0,0))
			pygame.display.flip()
			self.update_display()           
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == MOUSEBUTTONDOWN:
					if self.Button1.pressed(pygame.mouse.get_pos()):
						pygame.quit()
					if self.Button2.pressed(pygame.mouse.get_pos()):
						camera.resolution = (WIDTH, HEIGHT)
						sleep(1)
						auto = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
						auto = "KJCam-capture-" + auto + ".jpg"
						print("File Saved as " + auto)
						camera.capture("/home/pi/Desktop/KJCam Photos/"+auto,resize=(WIDTH,HEIGHT))		
						img = pygame.image.load("/home/pi/Desktop/KJCam Photos/"+auto)
						screen.blit(img,(0,0))
						pygame.display.flip()
						self.update_display()

if __name__ == '__main__':
	obj = KJCam()
