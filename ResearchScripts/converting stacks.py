#! /usr/bin/python3  

import csv
from math import pi
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

global l
a = [] #area put out by the csv file
i = [] #irradiance put out by the csv file
l = 0 # number of lines in the file 

global name
name = input() #Name of file?

with open(name,'r') as csvfile:
    plots = csv.reader(csvfile,delimiter = ',')
    for row in plots:
        PD = float(row[0]) #PulseDuration
        RSS = float(row[1]) #RetinalSpotSize-diameter
        TD = float(row[2]) #ThresholdDose-Energy
        WL = float(row[3]) #Wavelength
        Area = pi * ((RSS/2)**2)
        Power = TD/PD
        Irradiance = Power/Area
        a.append(Area)
        i.append(Irradiance)
        l += 1
csvfile.close



for n in range (0, l):
    print(str(a[n]) + " " + str(i[n]) + '\n') #a i
