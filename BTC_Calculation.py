#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:50:59 2022

@author: benjamin
"""

import numpy as np
from numpy import array

#Example without fees (exchanges)

listofcurrentPrice = array([39705.45,29984.12,53646.11,52874.55])
listofpaidBTC = array([80,55,50,10])

listofreceivedBTC = listofpaidBTC/listofcurrentPrice
print("Total BTC: " + str(sum(listofreceivedBTC)))
listofTotalBTC=sum(listofreceivedBTC)
listofrecandcurr = listofreceivedBTC*listofcurrentPrice
#listofrecandcurr = listofreceivedBTCFEES*listofcurrentPrice
listSum=sum(listofrecandcurr)
print("Investement: " + str(sum(listofpaidBTC)) + "€")
print("Average cost: " + str(listSum/listofTotalBTC) + "€")






