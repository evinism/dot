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
      icon = "\u2600"
   else: 
      index = (pos * dec(8)) + dec("0.5")
      index = math.floor(index)
      icon = {
         0: "\u25cb",
         1: "\u25d4",
         2: "\u25d1",
         3: "\u25d5",
         4: "\u25cf",
         5: "\u25d5", # reversed
         6: "\u25d1",
         7: "\u25d4"  # reversed
      }[int(index) & 7]
   return icon + waxing_waning


def main(datetime=None): 
   pos = position(datetime)
   phasename = phase(pos)
   print(phasename)

if __name__=="__main__": 
   main()