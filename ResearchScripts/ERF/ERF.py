#! /usr/bin/python3  

import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from scipy.special import erfinv

global lines
lines = 0    #number of lines in the files
PN = [] #PUlse number list
DD = [] #Desired dose list
P = [] #intensity of single pulse
InvERF = [] #value from the inverse error function
FD = [] #final dose

global name
name = input() #name of file

with open(name,'r') as csvfile:
    plots = csv.reader(csvfile,delimiter = ',')
    for row in plots:
        N = float(row[0]) #PulseNumber
        D = float(row[1]) #Desired Dose
        OneP = 1-((1-D)**(1/N))
        E = erfinv(OneP)
        dose = math.exp(E)
        InvERF.append(E)
        FD.append(dose)
        PN.append(N)
        DD.append(D)
        P.append(OneP)
        lines += 1
csvfile.close

for n in range (0, lines):
     print(str(PN[n]) + " " + str(DD[n]) + " " + str(P[n]) + " " + str(InvERF[n]) + " " + str(FD[n]) + '\n') #output
