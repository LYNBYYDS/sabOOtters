#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:59:58 2022

@author: ly
"""
from Card import *

class Cardset:
    
    def __init__(self):
        self.pathcards = [PathCard("URDL+ ") for x in range(5)]

        # URDL	5	1
        # URD	5	1
        # URL	5	1
        # UR	5	1
        # UL	4	1
        # UD	4	1
        # RL	3	1
        # U	    0	1
        # R	    0	1
        # total 40
        for x in range(5):
            self.pathcards.append(PathCard("URD + "))
        for x in range(5):
            self.pathcards.append(PathCard("UR L+ "))
        for x in range(5):
            self.pathcards.append(PathCard("UR  + "))
        for x in range(5):
            self.pathcards.append(PathCard("U  L+ "))
        for x in range(5):
            self.pathcards.append(PathCard("U D + "))
        for x in range(5):
            self.pathcards.append(PathCard(" R L+ "))
        self.pathcards.append(PathCard("URDL- "))
        self.pathcards.append(PathCard("URD - "))
        self.pathcards.append(PathCard("UR L- "))
        self.pathcards.append(PathCard("UR  - "))
        self.pathcards.append(PathCard("U  L- "))
        self.pathcards.append(PathCard("U D - "))
        self.pathcards.append(PathCard(" R L- "))
        self.pathcards.append(PathCard("U   - "))
        self.pathcards.append(PathCard(" R  - "))

        # Li	2	3
        # P	2	3
        # W	2	3
        # LiP	1	0
        # LiW	1	0
        # PW	1	0
        # MAP	6	
        # RoF	3	 
        
        self.actioncards = [ActionCard("Li+   ") for x in range(2)]
        for x in range(2):
            self.actioncards.append(ActionCard("P+    "))
        for x in range(2):
            self.actioncards.append(ActionCard("W+    "))
        for x in range(3):
            self.actioncards.append(ActionCard("Lix   "))
        for x in range(3):
            self.actioncards.append(ActionCard("Px    "))
        for x in range(3):
            self.actioncards.append(ActionCard("Wx    "))
        for x in range(6):
            self.actioncards.append(ActionCard("MAP   "))
        for x in range(3):
            self.actioncards.append(ActionCard("RoF   "))
        self.actioncards.append(ActionCard("LiP+  "))
        self.actioncards.append(ActionCard("LiW+  "))
        self.actioncards.append(ActionCard("PW+   "))
      
        
        # 1G	16	
        # 2G	8	
        # 3G	4	
        self.goldcards = [GoldCard("1G    ") for x in range(16)]
        for x in range(8):
            self.goldcards.append(GoldCard("2G    "))
        for x in range(4):
            self.goldcards.append(GoldCard("3G    "))
      
        
# 道路牌：	40張
# 行動牌：	27張
# 金塊卡：	28張
# 身份卡：	11張

# test code

# cardset1 = Cardset()
# print(cardset1.__dict__)

# endcardordre = [x for x in range(3)]
# if endcardordre == [0, 1, 2]:
#     print("ok")



