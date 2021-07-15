#! /usr/bin/python3

from math import *

sech = lambda x: 1/cosh(x)
getAccExpended = lambda particle, dim: atanh(particle[dim])

def fastAcc(vel, dir, mag):
	if(dir == 'y'): vel[0], vel[1] = vel[1], vel[0]
	# figure constants
	c0 = atanh(vel[0])
	c1 = vel[1] / sqrt(1 - vel[0]**2)
	c2 = sqrt(1 - c1**2)
	# apply acceleration
	vel[0] = tanh(mag + c0)
	vel[1] = c1 * sech(mag + c0)
	vel[2] = c2 * sech(mag + c0)
	# Swap and return
	if(dir == 'y'): vel[0], vel[1] = vel[1], vel[0]
	return

def applyAcc(dir, mag):
	for particle in list_of_particles:
		fastAcc(particle, dir, mag)
	return

def printVec():
	for particle in list_of_particles:
		print("[%+0.4f, %+0.4f, %+0.4f] " % (particle[0], particle[1], particle[2]))
	print()
	return

stat = [0.0, 0.0, 1.0]
trav = [0.0, 0.5, 0.0]
para = [0.5, 0.0, 0.0]

list_of_particles = [stat, trav, para]

applyAcc('x', 0.0)

levM = +0.2;
levP = +0.000001;

x = 0
while True:
	x += 2
	levM = 0.4*cos(2*pi*x/370)
	applyAcc('x', +1*levM)
	applyAcc('y', +1*levP * sqrt(1-tanh(levM)**2))
	applyAcc('x', -1*levP * sqrt(1-tanh(levM)**2) * 0.4*sin(2*pi*x/370)*(2*pi/370))
	applyAcc('x', -1*levM)
	# Rest frame attractive force.
	applyAcc('y', -1*levP)
	# print between interval
	if(x % 10000 == 0):
		print("%+0.5f"% levM)
		printVec()
