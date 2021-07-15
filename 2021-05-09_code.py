#! /usr/bin/python3
import math, random

delT = 1/80000
initSpeed = 0.5		# keep it positive
actionLim = 100000

FC = [0, initSpeed]		# Frame of moving Charge
statR = [0, 0]
statS = [0, 0]
paraR = [0, +initSpeed/2.0]
paraS = [0, +initSpeed/2.0]
travR = [+initSpeed/2.0, 0]
travS = [+initSpeed/2.0, 0]
force = [0.99999, 0]

dotProduct = lambda a, b : a[0] * b[0] + a[1] * b[1]
magnitude  = lambda a : dotProduct(a, a) ** 0.5 

def getRandAcc():
	angle = random.random()*2*math.pi
	return [math.cos(angle), math.sin(angle)]
def applyAcc(v, a):
	scaleFactor = dotProduct(a, v)
	v[0] = v[0] + delT * (a[0] - scaleFactor * v[0])
	v[1] = v[1] + delT * (a[1] - scaleFactor * v[1])
	return v

def getDirectionalForce(vec, s):
	mag = magnitude(vec)
	return [s*vec[0]/mag, s*vec[1]/mag]

def printVec(varStr, var):
	print(varStr+": [%+0.2f" % var[0], ", %+0.2f" % var[1], ", %+0.2f]" % (1-dotProduct(var, var))**0.5,
		"\tSpeed: %+0.4f" % magnitude(var), sep="")
	return
	
def printAll():
	print("\tVx\tVy\tVt")
	printVec("statR", statR)
	printVec("statS", statS)
	printVec("paraR", paraR)
	printVec("paraS", paraS)
	printVec("travR", travR)
	printVec("travS", travS)
	printVec("force", force)
	printVec("fCarr", FC)
	print("")

if magnitude(paraR) >= 1 or magnitude(travR) >= 1:
	print("ERR: Mover exceeding speed of light")
	exit()
	
#################################################### MAIN ####################################################
while True:
	statR = [0, 0]
	paraR = [0, +initSpeed]
	travR = [+initSpeed, 0]
	# Apply random accelerations
	actionCount = 0
	acc = getRandAcc()
	while actionCount < actionLim:
		actionCount += 1
		applyAcc(statR, acc)
		applyAcc(paraR, acc)
		applyAcc(travR, acc)	
	# Apply random accelerations
	actionCount = 0
	acc = getRandAcc()
	while actionCount < actionLim:
		actionCount += 1
		applyAcc(statR, acc)
		applyAcc(paraR, acc)
		applyAcc(travR, acc)
	# Apply random accelerations
	actionCount = 0
	acc = getRandAcc()
	while actionCount < actionLim:
		actionCount += 1
		applyAcc(statR, acc)
		applyAcc(paraR, acc)
		applyAcc(travR, acc)
	# Decelerate the statR
	while statR[0] > 0:
		applyAcc(statR, [-1, 0])
		applyAcc(paraR, [-1, 0])
		applyAcc(travR, [-1, 0])
	while statR[1] > 0:
		applyAcc(statR, [0, -1])
		applyAcc(paraR, [0, -1])
		applyAcc(travR, [0, -1])
	while statR[0] < 0:
		applyAcc(statR, [+1, 0])
		applyAcc(paraR, [+1, 0])
		applyAcc(travR, [+1, 0])
	while statR[1] < 0:
		applyAcc(statR, [0, +1])
		applyAcc(paraR, [0, +1])
		applyAcc(travR, [0, +1])
	print("Lab Frame Attractive ES force applied")
	printAll()
		
exit()
while True:
	# Initial
	#print("Initial State")
	#printAll()
	# Decelerate to moving charge's rest frame
	while FC[1] > 0:
		applyAcc(FC, [0, -1])
		applyAcc(statR, [0, -1])
		applyAcc(statS, [0, -1])
		applyAcc(paraR, [0, -1])
		applyAcc(paraS, [0, -1])
		applyAcc(travR, [0, -1])
		applyAcc(travS, [0, -1])
	#print("Decelerated to FC's rest frame")
	#printAll()

	# Apply repulsive force on Reactive movers entirely in x-axis
	actionCount = 0
	while actionCount < actionLim:
		actionCount += 1
		applyAcc(statR, [1, 0])
		applyAcc(paraR, [1, 0])
		applyAcc(travR, [1, 0])
	#print("Charge Frame Repulsive ES force applied")
	#printAll()

	# Re-accelerate to Lab frame
	while FC[1] < initSpeed:
		applyAcc(FC, [0, 1])
		applyAcc(statR, [0, 1])
		applyAcc(statS, [0, 1])
		applyAcc(paraR, [0, 1])
		applyAcc(paraS, [0, 1])
		applyAcc(travR, [0, 1])
		applyAcc(travS, [0, 1])
	#print("Re-accelerated to Lab frame")
	#printAll()

	# Apply rest frame forces to achieve a static statR. This equates to a case with only magnetic force applied.
	while statR[0] > 0:
		applyAcc(statR, [-1, 0])
		applyAcc(paraR, [-1, 0])
		applyAcc(travR, [-1, 0])
	while statR[1] > 0:
		applyAcc(statR, [0, -1])
		applyAcc(paraR, [0, -1])
		applyAcc(travR, [0, -1])
	while statR[0] < 0:
		applyAcc(statR, [+1, 0])
		applyAcc(paraR, [+1, 0])
		applyAcc(travR, [+1, 0])
	while statR[1] < 0:
		applyAcc(statR, [0, +1])
		applyAcc(paraR, [0, +1])
		applyAcc(travR, [0, +1])
		
	print("Lab Frame Attractive ES force applied")
	printAll()
"""	# MATLAB side
gamma = 1/((1-dotProduct(v1, v1))**0.5);
fact2 = 1-dotProduct(v1, v2);
extSc = 1/(gamma * fact2);
intFc = v2 - v1 + v1.*(gamma-1).*(sum(v1 .* v2)/sum(v1 .* v1)-1);
vrel = extSc .* intFc;
"""
