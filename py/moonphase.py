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
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "🌑︎",
      1: "🌒︎",
      2: "🌓︎",
      3: "🌔︎",
      4: "🌕︎",
      5: "🌖︎",
      6: "🌗︎",
      7: "🌘︎"
   }[int(index) & 7]

def phase_basic(pos): 
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "○",
      1: "◔",
      2: "◑",
      3: "◕",
      4: "●",
      5: "◔", # Ugh... i want this reversed
      6: "◕",
      7: "◔"  # same, ugh want this reversed 
   }[int(index) & 7]


def phase_basic(pos): 
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "○",
      1: "◔\u0307",
      2: "◑\u0307",
      3: "◕\u0307",
      4: "●",
      5: "◕\u0323", # Ugh... i want this reversed
      6: "◑\u0323",
      7: "◔\u0323"  # same, ugh want this reversed 
   }[int(index) & 7]


def main(): 
   pos = position()
   phasename = phase_basic(pos)
   print(phasename)

if __name__=="__main__": 
   main()