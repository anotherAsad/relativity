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
		print("[%+0.3f, %+0.3f, %+0.3f] " % (particle[0], particle[1], particle[2]))
	print()
	return

stat = [0.0, 0.0, 1.0]
trav = [0.0, 0.1, 0.0]
para = [0.1, 0.0, 0.0]

list_of_particles = [stat, trav, para]

applyAcc('x', 0.0)

levM = +0.1;
levP = +0.000001;

for x in range(0, 1000000):
	applyAcc('x', +1*levM)
	applyAcc('y', +1*levP * sqrt(1-tanh(levM)**2))
	applyAcc('x', -1*levM)
	applyAcc('y', -1*levP)
#	Inexplicables that I want to get rid of.
#	x_acc = getAccExpended(stat, 0)
#	applyAcc('x', -1*x_acc)
#	y_acc = getAccExpended(stat, 1)
#	applyAcc('y', -1*y_acc)
	# print between interval
	if(x % 10000 == 0):
#		print(y_acc, levP / sqrt(1-tanh(levM)**2), levP / sqrt(1-tanh(levM)**2) / y_acc)
#		print(x_acc, y_acc, atan2(y_acc, x_acc)/pi*180)
		printVec()
