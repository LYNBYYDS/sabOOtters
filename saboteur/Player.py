#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:30:20 2022

@author: ly
"""



from Card import *

class Player:
    
    def __init__(self, playername, age, role, nbCard = 6, index = 0, point = 0, toolstat = [1, 1, 1]):
        
        self.playername = playername
        self.age = age
        self.role = role
        self.nbCard = nbCard
        self.index = index
        self.point = point
        self.cardtable = [EmptyCard() for x in range(nbCard)]
        self.table_top = ["          " for x in range(nbCard)]
        self.table_middle = [str(x) + ":      , " for x in range(nbCard)]
        self.table_bottom = ["          " for x in range(nbCard)]
        
    def printPlayerCard(self):
        for x in self.table_top:
            print(x, end="")
        print()
        for x in self.table_middle:
            print(x, end="")
        print(str(self.nbCard+1) + ") Throw away a card")
        for x in self.table_bottom:
            print(x, end="")
        print()
        
    def resetPlayer(self, resetpoint):
        for index in range(nbCard):
            self.cardtable[self.index] = EmptyCard()
            self.table_top[self.index] = "          " 
            self.table_middle[self.index] = str(self.index) + ":      , "
            self.table_bottom[self.index] = "          "
        self.index = 0
        self.toolstat = [1, 1, 1]
        if resetpoint:
            self.point = 0
        
    def insertCard(self, card):
        if self.index < self.nbCard:
            self.cardtable[self.index] = card
            self.table_top[self.index] = "   " + card.gettop() + "  "
            self.table_middle[self.index] = str(self.index) + ": " + card.getmiddle() + ", "
            self.table_bottom[self.index] = "   " + card.getbottom() + "  "
            self.index += 1
            return 1
        else:
            print("no place to put more card")
            return 0
       
    def removeCard(self, index):
        if self.index >= index:
            for i in range(self.index-index):
                self.cardtable[index+i] = self.cardtable[index+i+1]
                self.table_top[index+i] = self.table_top[index+i+1]
                self.table_middle[index+i] = self.table_middle[index+i+1]
                self.table_bottom[index+i] = self.table_bottom[index+i+1]
            self.index -= 1
            self.cardtable[self.index] = EmptyCard()
            self.table_top[self.index] = "          " 
            self.table_middle[self.index] = str(self.index) + ":      , "
            self.table_bottom[self.index] = "          "
            return 1
        else:
            print("index out range")
            return 0
       
    def changeToolStat(self, toolname, card): # ToolStat LI P W
        if (toolstat[0] == 0 and (card.cardtype == "Li+" or card.cardtype == "LiP+" or card.cardtype == "LiW+")):
            toolstat[0] = 1
            return 1
        elif (toolstat[1] == 0 and (card.cardtype == "P+" or card.cardtype == "LiP+" or card.cardtype == "PW+")):
            toolstat[1] = 1
            return 1
        elif (toolstat[2] == 0 and (card.cardtype == "W+" or card.cardtype == "LiW+" or card.cardtype == "PW+")):
            toolstat[2] = 1
            return 1
        elif (toolstat[0] == 1 and card.cardtype == "Lix" ):
            toolstat[0] = 0
            return 1
        elif (toolstat[1] == 1 and card.cardtype == "Px" ):
            toolstat[1] = 0
            return 1
        elif (toolstat[2] == 1 and card.cardtype == "Wx" ):
            toolstat[2] = 0
            return 1
        else:
            print("error, cant play this cation card tools stat not changed")
            return 0
        
    def changePoint(self, point):
        self.point += point
    
        
# test code
        
    
# card1 = PathCard("URDL+")
# card2 = PathCard("URD +")
# card3 = PathCard("UR L+")
# card4 = PathCard("UR  +")

# player1 = Player("titi", 18, "bad", 5)
# print(player1.index)
# # print(player1.__dict__)
# player1.printPlayerCard()
# player1.insertCard(card1)
# player1.insertCard(card2)
# player1.insertCard(card3)
# player1.insertCard(card4)
# player1.printPlayerCard()

# player1.removeCard(1)
# player1.printPlayerCard()