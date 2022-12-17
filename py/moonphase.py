#!/usr/bin/env python
"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import math, decimal, datetime
dec = decimal.Decimal

def position(now=None): 
   if now is None: 
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = dec("0.20439731") + (days * dec("0.03386319269"))

   return lunations % dec(1)


def phase(pos): 
   waxing_waning = "\u0307" if pos < dec("0.5") else "\u0323"
   if dec("0.485") < pos < dec("0.515"): 
      icon = "☀"
   else: 
      index = (pos * dec(8)) + dec("0.5")
      index = math.floor(index)
      icon = {
         0: "○",
         1: "◔",
         2: "◑",
         3: "◕",
         4: "●",
         5: "◕", # Ugh... i want this reversed
         6: "◑",
         7: "◔"  # same, ugh want this reversed 
      }[int(index) & 7]
   return icon + waxing_waning


def main(datetime=None): 
   pos = position(datetime)
   phasename = phase(pos)
   print(phasename)



if __name__=="__main__": 
   main()