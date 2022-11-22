#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:50:59 2022

@author: benjamin
"""

import numpy as np
from numpy import array

#Example without fees (exchanges)

#listofcurrentPrice = np.array([39705.45,29984.12,53646.11,52874.55])
#listofpaidBTC = np.array([80,55,50,10])

#listofcurrentPrice =np.array([39705.45])
#listofpaidBTC = np.array([80])


listA = []
listB = []
a = float(input("Invest in EUR: " ))
listA.append(a)
b = float(input("By Bitcoin Price in EUR: " ))
listB.append(b)
print("Would you like to enter more investments? Yes or No? For yes enter y and for no enter n")
c = input("Yes or No?: " )
while c != "n":
    print("Okay")
    v = float(input("Invest in EUR: " ))
    w = float(input("By Bitcoin Price in EUR: " ))
    listA.append(v)
    listB.append(w)
    print("Would you like to enter more investments? Yes or No? For yes enter y and for no enter n")
    c = input("Yes or No?: Neu " )
    if c == "y":
        print("Okay")
        g = float(input("Invest in EUR: " ))
        z = float(input("By Bitcoin Price in EUR: " ))
        listA.append(g)
        listB.append(z)
        c = input("Yes or No?: Neu2 " )
    else:
        break
        print ("No investemenst more")
 

print(np.array(listA))
print(np.array(listB))

listC = np.array(listA)/np.array(listB)
newC=np.around(listC,8)
print(listC)
print("Total BTC: " + str(sum(newC)))

listD = sum(newC)
listE = listC*(np.array(listB))

listS=sum(listE)
print(listS)
print("Investement: " + str(sum(np.array(listA))) + "€")
print("Average cost: " + str(round(listS/listD,2)) + "€")


"""
#print("Investement: " + str(a) + " €")
listofreceivedBTC = listofpaidBTC/listofcurrentPrice
newlistofreceivedBTC=np.around(listofreceivedBTC,8)

print("Total BTC: " + str(sum(newlistofreceivedBTC)))
listofTotalBTC = sum(newlistofreceivedBTC)
listofrecandcurr = listofreceivedBTC*listofcurrentPrice
#listofrecandcurr = listofreceivedBTCFEES*listofcurrentPrice
listSum=sum(listofrecandcurr)
print("Investement: " + str(sum(listofpaidBTC)) + "€")
print("Average cost: " + str(round(listSum/listofTotalBTC,2)) + "€")
"""

#Test Commit

#1 Satoshi = 0.00000001 BTC






