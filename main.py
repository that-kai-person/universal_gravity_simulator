import scipy
import pytime
from scipy.constants import G
import math
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Delete support prompt
import pygame
from pygame.locals import *

def crash(obj_arr): #Collision function
	for p in range(len(obj_arr)):
		for q in range(p + 1, len(obj_arr)):
			if abs(obj_arr[p].x - obj_arr[q].x) < (obj_arr[p].size+obj_arr[q].size) and abs(obj_arr[p].y - obj_arr[q].y) < (obj_arr[p].size+obj_arr[q].size):
				
				#Calculating using momentum
				vx = (obj_arr[p].vx*obj_arr[p].m + obj_arr[q].vx*obj_arr[q].m)/(obj_arr[p].m+obj_arr[q].m)
				vy = (obj_arr[p].vy*obj_arr[p].m + obj_arr[q].vy*obj_arr[q].m)/(obj_arr[p].m+obj_arr[q].m)
				x = (obj_arr[p].x+obj_arr[q].x)/2
				y = (obj_arr[p].y+obj_arr[q].y)/2
				m = obj_arr[p].m+obj_arr[q].m
				obj_arr[p] = Obj(m, x, y, vx, vy)
				obj_arr[p].size = obj_arr[p].size + obj_arr[q].size
				del obj_arr[q]
				break

#Constants
WHITE = (255,255,255)

#Introduction to the program
print("Welcome to gravity simulator v2.0!")
print("This is a model based on newtonian universal gravity")
print("that simulates real time gravitational interaction.")
print("Tip: Low masses have a very weak force, so try using very high masses.")
a = input("To start press enter...")
print('\n')

#Start objects
n = int(input("Enter number of objects: "))
obj_arr = []  # Initialize an empty list
for _ in range(n):
	print("Object ", len(obj_arr) + 1)
	m = float(input("Enter mass: "))
	x = float(input("Enter x: "))
	y = float(input("Enter y: "))
	vx0 = float(input("Enter initial vx: "))
	vy0 = float(input("Enter initial vy: "))
	obj = Obj(m, x, y, vx0, vy0)
	obj_arr.append(obj)
	

t=0

# Start of the pygame program
	
pygame.init()
display_window = pygame.display.set_mode((1000,1000)) #Create a window with 800px width and 500px height
clock = pygame.time.Clock() #Setting a framerate
pygame.display.set_caption('Gravitation simulation version 2.0') #Define window title

#Main loop
sim_end = False
while not sim_end:
	
	if len(obj_arr) == 1:
		print("Exiting main loop")
		sim_end = True
		break
	
	# Vector update
	for p in range(len(obj_arr)):
		Fx = 0
		Fy = 0
		ax = 0
		ay = 0
		vx = 0
		vy = 0
		for q in range(len(obj_arr)):
			if p != q:  # Skip self-interaction
				Fx, Fy = obj_arr[p].force_g(obj_arr[q], t)
				ax, ay = obj_arr[p].acceleration(Fx, Fy)
				vx, vy = obj_arr[p].velocity(ax, ay, t)
			
		obj_arr[p].ax = ax
		obj_arr[p].ay = ay
		obj_arr[p].vx = vx
		obj_arr[p].vy = vy
		
	
	# Location update
	for p in range(len(obj_arr)):
		x, y = obj_arr[p].location(obj_arr[p].ax, obj_arr[p].ay, t)
		obj_arr[p].x = x
		obj_arr[p].y = y
		
	
			
	
	#Visual update
	display_window.fill((0, 0, 0))  #Restart screen
	for p in range(len(obj_arr)):
		obj_arr[p].exist(display_window)
	pygame.display.update()
	
	crash(obj_arr)
	

	
	for event in pygame.event.get(): #Event handling
		if event.type == QUIT: #Quitting
			print("Program end.")
			pygame.quit()
			sys.exit()
	t = t+0.01 #Moving the independant var
	clock.tick(60)
print("Simulation done.")

while True: #Sim end loop
	x, y = obj_arr[0].location(obj_arr[0].ax, obj_arr[0].ay, t)
	obj_arr[0].x = x
	obj_arr[0].y = y
	
	display_window.fill((0, 0, 0))
	obj_arr[0].exist(display_window)
	pygame.display.update()
	
	for event in pygame.event.get(): #Event handling
		if event.type == QUIT: #Quitting
			print("Program end.")
			pygame.quit()
			sys.exit()
	t = t+0.01 #Moving the independant var
	clock.tick(60)
