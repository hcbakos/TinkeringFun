############################################## 
# Programmer: Henry Bakos 
# Class: ENSC 201-01, Fall 2026 
# Programming Assignment #2
# 9/14/26 
#  
# Description: This program computes the area and cirumference of a cirlce with a given radius
# Notes: I referenced/used the following: Programming Assignment 2
############################################## 


import math

circle_radius = 5

compute_area = math.pi * circle_radius ** 2
#multiples the square of the circles radius by pi to get the area

compute_circumference = 2 * math.pi * circle_radius
#multiplies the circles radius by pi, and by 2 to get the circumference

print("area:", compute_area)
print("cirumference:", compute_circumference)
