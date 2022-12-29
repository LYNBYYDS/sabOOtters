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
        
    def printPlayerStat(self):
        print("player: " + self.playername)
        print("broken tools: ", end="")
        if self.toolstat[0] == 1:
            print("   ", end="")
        else:
            print("LI ", end="")
        if self.toolstat[1] == 1:
            print("   ", end="")
        else:
            print("P  ", end="")
        if self.toolstat[2] == 1:
            print("   ", end="")
        else:
            print("W  ", end="")
        print("")
        self.printPlayerCard()
        
        
    def printPlayerCard(self):
        for x in self.table_top:
            print(x, end="")
        print()
        for x in self.table_middle:
            print(x, end="")
        print(str(self.nbCard) + ") Throw away a card")
        for x in self.table_bottom:
            print(x, end="")
        print()
        
    def resetPlayer(self, resetpoint):
        for index in range(self.nbCard):
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
            
            for i in range(self.index-index-1):
                
                self.cardtable[index+i] = self.cardtable[index+i+1]
                self.table_top[index+i] = self.table_top[index+i+1]
                self.table_middle[index+i] = str(index+i) + ": " + self.cardtable[index+i+1].getmiddle() + ", "
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
       
    def changeToolStat(self, card): # ToolStat LI P W
        if self.toolstat[0] == 0 and card.cardtype == "Li+   ":
            self.toolstat[0] = 1
            return 1
        elif self.toolstat[1] == 0 and card.cardtype == "P+    ":
            self.toolstat[1] = 1
            return 1
        elif self.toolstat[2] == 0 and card.cardtype == "W+    ":
            self.toolstat[2] = 1
            return 1
        elif self.toolstat[0] == 1 and card.cardtype == "Lix   ":
            self.toolstat[0] = 0
            return 1
        elif self.toolstat[1] == 1 and card.cardtype == "Px    ":
            self.toolstat[1] = 0
            return 1
        elif self.toolstat[2] == 1 and card.cardtype == "Wx    ":
            self.toolstat[2] = 0
            return 1
        elif card.cardtype == "LiP+  ":
            if self.toolstat[0] == 0 and self.toolstat[1] == 0:
                tooltype = input("Enter which tool you want to repair(L for lamp, P for pick): ")
                if tooltype == "L":
                    self.toolstat[0] = 1
                    return 1
                elif tooltype == "P":
                    self.toolstat[1] = 1
                    return 1
                else:
                    return 0
            elif self.toolstat[0] == 0 and self.toolstat[1] == 1:
                self.toolstat[0] = 1
                return 1
            elif self.toolstat[0] == 1 and self.toolstat[1] == 0:
                self.toolstat[1] = 1
                return 1
            else:
                return 0
        elif card.cardtype == "LiW+  ":
            if self.toolstat[0] == 0 and self.toolstat[2] == 0:
                tooltype = input("Enter which tool you want to repair(L for lamp, C for mine car): ")
                if tooltype == "L":
                    self.toolstat[0] = 1
                    return 1
                elif tooltype == "C":
                    self.toolstat[2] = 1
                    return 1
                else:
                    return 0
            elif self.toolstat[0] == 0 and self.toolstat[2] == 1:
                self.toolstat[0] = 1
                return 1
            elif self.toolstat[0] == 1 and self.toolstat[2] == 0:
                self.toolstat[2] = 1
                return 1
            else:
                return 0
        elif card.cardtype == "PW+   ":
            if self.toolstat[2] == 0 and self.toolstat[1] == 0:
                tooltype = input("Enter which tool you want to repair(P for pick, C for mine car): ")
                if tooltype == "C":
                    self.toolstat[2] = 1
                    return 1
                elif tooltype == "P":
                    self.toolstat[1] = 1
                    return 1
                else:
                    return 0
            elif self.toolstat[2] == 0 and self.toolstat[1] == 1:
                self.toolstat[2] = 1
                return 1
            elif self.toolstat[2] == 1 and self.toolstat[1] == 0:
                self.toolstat[1] = 1
                return 1
            else:
                return 0
        else:
            print("error, cant play this aation card, tool stat not changed")
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