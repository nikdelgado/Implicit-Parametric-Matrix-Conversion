# Author: Nik Delgado
# Class: CS 2300 (Linear Algebra
# Project 2
# This program reads in a data file with implicit and parametric values and converts between the two as well as point normal form.

import numpy as np
import math

# This function reads in the text file and stores the contents of the file into a list.
def file_cleanup():
	f = open("CS2300P2Mac", "r")
	contents = f.readlines()
	f.close()
	
	str1 = contents[0]
	str1 = str1[2:-1]
	str1 = str1.replace(" ", ",")
	list1 = str1.split(',')
	
	str2 = contents[1]
	str2 = str2[2:-1]
	str2 = str2.replace("  ", " ")
	str2 = str2.replace(" ", ",")
	list2 = str2.split(',')
	
	return list1, list2
	
# This function retrives the values from the list if parametric and returns the pValue and vValue
def getParametric(list):
	pVal = list[0:2]
	pVal = [float(i) for i in pVal]
	
	vVal = list[2:4]
	vVal = [float(i) for i in vVal]

	return pVal, vVal 

# This function converts a given p and v value and returns an implicit a, b, and c value.
def parametricToImplicit(p, v):
	aVal = v[1]
	bVal = -v[0]
	cVal = -((aVal * p[0]) + (bVal * p[1]))
	
	return aVal, bVal, cVal

# This function takes a given a,b, and c value and converts them to point normal form.
def getPointNormal(a, b, c):
	magA = math.sqrt(pow(a,2) + pow(b,2))
	magA = round(magA,2)
	a = round(a/magA,2)
	b = round(b/magA,2)
	c = round(c/magA,2)
	
	return a, b, c, magA

#  This function retrieves the points from a line with implicit data
def getPointsL1(list):
	point1 = list[4:6]
	point1 = [float(i) for i in point1]
		
	point2 = list[6:8]
	point2 = [float(i) for i in point2]
		
	point3 = list[8:10]
	point3 = [float(i) for i in point3]
	
	return point1, point2, point3

# This function retrives points from a line with parametric data
def getPointsL2(list):
	
	point1 = list[3:5]
	point1 = [float(i) for i in point1]
	
	point2 = list[5:7]
	point2 = [float(i) for i in point2]
	
	point3 = list[7:10]
	point3 = [float(i) for i in point3]
	
	return point1, point2, point3

# This function calculates the distance from a given inplicit line and returns the distance
def findDistance(a, b, c, magA, point):
	distance = (a * point[0] + b * point[1] + c) / magA
	distance = round(distance,2)
	return distance

# This function retrives the implicit points from a list with implicit data
def getImplicit(list):
	a = float(list[0])
	b = float(list[1])
	c = float(list[2])
	return a, b, c

# This function converts implicit data to parametric data
def implicitToParametric(a, b, c):
	v = []
	v.append(b)
	v.append(-a)
	
	p = []
	p.append(-float(c)/float(a))
	p.append(0.0)

	return p, v


def main():
	# Clean up and extract Data
	list1, list2 = file_cleanup();
	
	# Call all the functions to get data for first line of data from the list
	p1, v1 = getParametric(list1)
	a1, b1, c1 = parametricToImplicit(p1, v1)
	aPn,bPn, cPn, magA = getPointNormal(a1, b1, c1)
	point1, point2, point3 = getPointsL1(list1)
	distance1 = findDistance(a1, b1, c1, magA, point1)
	distance2 = findDistance(a1, b1, c1, magA, point2)
	distance3 = findDistance(a1, b1, c1, magA, point3)
	distance_list = [distance1, distance2, distance3]
	point_list = [point1, point2, point3]

	
	# Print the results of all the data gathered
	print("LINE 1 ")
	print("-------")
	print("Parametric Form: l(t) = ", p1, " + t", v1)
	print("Converted to Implicit Form: ", a1, "x1 + ", b1, "x2 + ", c1, " = 0")
	print("Converted to Point-Normal Form: ", aPn, "x1 + ", bPn, "x2 + ", cPn, " = 0")
	for i in  range(len(distance_list)):
		if distance_list[i] == 0:
			print("Distance from point", point_list[i], "to the line is ", distance_list[i], " The point is on the line.")
		else:
			print("Distance from point", point_list[i], "to the line is ", distance_list[i])
	
	
	# Call all the functions to get data for the second line of data from the list
	a2, b2, c2 = getImplicit(list2)
	p2, v2 = implicitToParametric(a2,b2,c2)
	aPn2, bPn2, cPn2, magA2 = getPointNormal (a2, b2, c2)
	point1, point2, point3 = getPointsL2(list2)
	distance1 = findDistance(a2, b2, c2, magA2, point1)
	distance2 = findDistance(a2, b2, c2, magA2, point2)
	distance3 = findDistance(a2, b2, c2, magA2, point3)
	distance_list = [distance1, distance2, distance3]
	point_list = [point1, point2, point3]	
	
	
	# Print the results of all the data gathered
	print("\nLINE 2 ")
	print("-------")
	print("Implicit Form: ", a2, "x1 + ", b2, "x2 + ", c2, " = 0")
	print("Converted to parametric Form: l(t) = ", p2, " + t", v2)
	print("Converted to Point-Normal Form: ", aPn2, "x1 + ", bPn2, "x2 + ", cPn2, " = 0")
	for i in  range(len(distance_list)):
		if distance_list[i] == 0:
			print("Distance from point", point_list[i], "to the line is ", distance_list[i], " The point is on the line.")
		else:
			print("Distance from point", point_list[i], "to the line is ", distance_list[i])				

main()
