class Obj:
  
  import scipy
  from scipy.constants import G
  import math
  import sys
  import os
  os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Delete support prompt
  import pygame
  from pygame.locals import *

	#Class defining a gravitational body using the MKS system, and handling a list of obj type objects
	G = scipy.constants.G
	ax = 0
	ay = 0
	
	def __init__(self, m, x, y, vx, vy):
		self.m = float(m)
		self.x = float(x)
		self.y = float(y)
		self.vx = float(vx)
		self.vy = float(vy)
		self.size = 5
	
	def location(self, ax, ay, t): #Get next location by acceleration, self v and self location
		return self.x + self.vx * t + 0.5 * self.ax * t**2, self.y + self.vy * t + 0.5 * self.ay * t**2
	
	def velocity(self, ax, ay, t): #Get velocity by acceleration and current v
		return self.vx+ax*t, self.vy+ay*t
	
	def acceleration(self, Fx, Fy): #Get acceleration from gravitational force
		#By Newtonian gravity. F = G*((m1*m2)/r^2)
		#F = ma --> a = F/m1
		ax = Fx/self.m
		ay = Fy/self.m
		print("ax:", ax, "ay:", ay)
		return ax, ay
	
	def force_g(self, obj2, t): #Force calculating function
		if isinstance(obj2, Obj):
			dy = self.y - obj2.y
			dx = self.x - obj2.x
			r2 = float((dx)**2 + (dy)**2)
			print("r2:", r2, "dx^2:", dx**2, "dy^2:", dy**2)
			r = math.sqrt(r2)
			Fg = G*((self.m*obj2.m)/r2)
			Fx = Fg*(dx/r)
			Fy = Fg*(dy/r)
			print("Fx:", Fx, "Fy:", Fy)
			print("t: ", t)
			return (-Fx), (-Fy)
		else:
			return 0, 0
	
	def exist(self, display_window): #Object draw function
		center = tuple((self.x, self.y))
		pygame.draw.circle(display_window, (255,255,255), center, self.size)
	
	def __str__(self):
		return f"{self.m}{self.x}{self.y}{self.vx}{self.vy}"
