import picamera
from time import sleep
import pygame
import random

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
black = pygame.Color(0, 0, 0)
textcol = pygame.Color(255, 255, 0)
screen.fill(black)



events = pygame.event.get()
camera.start_preview()
count=0
while True:	
	#pygame.display.update()
	sleep(1)
	count+=1
	if(count>10):
		pygame.quit()
		break
	for event in pygame.event.get():
		if(event.type == pygame.KEYUP):
			print "key pressed"
			camera.capture('hello.jpg',resize=(WIDTH,HEIGHT))			    
			camera.stop_preview()			
			img = pygame.image.load('hello.jpg')
			screen.blit(img,(0,0))
			pygame.display.flip()
			pygame.quit()

pygame.quit()
