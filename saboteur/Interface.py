# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:26:23 2022

@author: pc
"""
from Card import *

class Interface:
    
    
        
    def __init__(self, dimX = 9, dimY = 5):
        
        self.dimX = dimX;
        self.dimY = dimY;
        self.table = [["     "] * self.dimX for y in range(self.dimY*3)]
        self.cardtable = [["NOCARD   "] * self.dimX for y in range(self.dimY)]
    
    def printCardtable(self):
        
        for y in range(self.dimY):
            for x in range(self.dimX):
                print(" " + self.cardtable[y][x] + " ", end="")
            print("")
            
        
    def printTitle(self):
        print("Current mine state:")
        print(" |", end="")
        for x in range(self.dimX):
            print("  " + str(x) + "  ", end="")
        print("")
        print("-+", end="")
        for x in range(self.dimX):
            print("-----", end="")
        print("")
        
    def printBody(self):
        
        for y in range(self.dimY*3):
            if y%3 == 0:
                print(" |", end="")
                for x in range(self.dimX):
                    print(self.table[y][x], end="")
                print("")
            elif y%3 == 1:
                print(str(int(y/3)) + "|", end="")
                for x in range(self.dimX):
                    print(self.table[y][x], end="")
                print("")
            elif y%3 == 2:
                print(" |", end="")
                for x in range(self.dimX):
                    print(self.table[y][x], end="")
                print("")
        print("-+", end="")
        for x in range(self.dimX):
            print("-----", end="")
        print("")
    
    
    def initCard(self, startcard, roundendcard0, roundendcard1, roundendcard2):
        self.dimX = 9
        self.dimY = 5
        self.table = [["     "] * self.dimX for y in range(self.dimY*3)]
        self.cardtable = [["NOCARD   "] * self.dimX for y in range(self.dimY)]
        
        self.cardtable[2][0] = "STARTCARD"
        self.table[6][0] = startcard.gettop()
        self.table[7][0] = startcard.getmiddle()
        self.table[8][0] = startcard.getbottom()
        
        self.cardtable[0][8] = "ENDCARD  "
        self.table[0][8] = roundendcard0.gettop()
        self.table[1][8] = roundendcard0.getmiddle()
        self.table[2][8] = roundendcard0.getbottom()
        
        self.cardtable[2][8] = "ENDCARD  "
        self.table[6][8] = roundendcard1.gettop()
        self.table[7][8] = roundendcard1.getmiddle()
        self.table[8][8] = roundendcard1.getbottom()
        
        self.cardtable[4][8] = "ENDCARD  "
        self.table[12][8] = roundendcard2.gettop()
        self.table[13][8] = roundendcard2.getmiddle()
        self.table[14][8] = roundendcard2.getbottom()


    def insertCard(self, card, coordX, coordY):
        
        # if there is no card at top left right bottom or the card is end card we dont test the condition of the path
        existcardtop = not ((coordY <= 0 or coordX < 0 or coordX >= self.dimX) \
            or (self.cardtable[coordY-1][coordX] == "ENDCARD  ") \
            or (self.cardtable[coordY-1][coordX] == "NOCARD   "))
        existcardbottom = not ((coordY >= self.dimY-1 or coordX < 0 or coordX >= self.dimX) \
            or (self.cardtable[coordY+1][coordX] == "ENDCARD  ") \
            or (self.cardtable[coordY+1][coordX] == "NOCARD   "))
        existcardleft = not ((coordX <= 0 or coordY < 0 or coordY >= self.dimY) \
            or (self.cardtable[coordY][coordX-1] == "ENDCARD  ") \
            or (self.cardtable[coordY][coordX-1] == "NOCARD   "))
        existcardright = not ((coordX >= self.dimX-1 or coordY < 0 or coordY >= self.dimY) \
            or (self.cardtable[coordY][coordX+1] == "ENDCARD  ") \
            or (self.cardtable[coordY][coordX+1] == "NOCARD   "))
        
        isaviliabletoput = 1
        
        # if there is card but the path has conflict
        if (existcardtop and (self.table[coordY*3-1][coordX] != "( | )" or card.cardtype[0] != "U")) \
            or (existcardbottom and (self.table[coordY*3+3][coordX] != "( | )" or card.cardtype[2] != "D")) \
            or (existcardleft and (self.table[coordY*3+1][coordX-1][3] != "-" or card.cardtype[3] != "L")) \
            or (existcardright and (self.table[coordY*3+1][coordX+1][1] != "-" or card.cardtype[1] != "R")):
            isaviliabletoput = 0
            print("error, path conflict!")
        # if there is no card next to the place we wanna to put then is not correct
        if not (existcardtop or existcardbottom or existcardleft or existcardright):
            isaviliabletoput = 0
            print("error, no card anround the place chose!")
        
        if isaviliabletoput == 1:
            # if the card is place inside of the table 
            if coordX >= 0 and coordX < self.dimX and coordY >= 0 and coordY < self.dimY:
                self.cardtable[coordY][coordX] = card.cardtype + "    "
                self.table[coordY*3][coordX] = card.gettop()
                self.table[coordY*3+1][coordX] = card.getmiddle()
                self.table[coordY*3+2][coordX] = card.getbottom()
            # if the card is not inside the table we need to get a bigger table 
            else:
                if coordX == -1 :
                    self.dimX += 1
                    for y in range(self.dimY*3):
                        self.table[y].insert(0,"     ")
                    for y in range(self.dimY):
                        self.cardtable[y].insert(0,["NOCARD   "])
                    self.cardtable[coordY][0] = card.cardtype + "    "
                    self.table[coordY*3][0] = card.gettop()
                    self.table[coordY*3+1][0] = card.getmiddle()
                    self.table[coordY*3+2][0] = card.getbottom()
                if coordX == self.dimX:
                    self.dimX += 1
                    for y in range(self.dimY*3):
                        self.table[y].append("     ")
                    for y in range(self.dimY):
                        self.cardtable[y].append(["NOCARD   "])
                    self.cardtable[coordY][coordX] = card.cardtype + "    "
                    self.table[coordY*3][coordX] = card.gettop()
                    self.table[coordY*3+1][coordX] = card.getmiddle()
                    self.table[coordY*3+2][coordX] = card.getbottom()
                if coordY == -1:
                    self.dimY += 1
                    for y in range(3):
                        self.table.insert(0, ["     "] * self.dimX)
                    for y in range(3):
                        self.cardtable.insert(0, ["NOCARD   "] * self.dimX)
                    self.cardtable[coordY+1][coordX] = card.cardtype + "    "
                    self.table[0][coordX] = card.gettop()
                    self.table[1][coordX] = card.getmiddle()
                    self.table[2][coordX] = card.getbottom()
                if coordY == self.dimY:
                    self.dimY += 1
                    for y in range(3):
                        self.table.append(["     "] * self.dimX)
                    for y in range(3):
                        self.cardtable.append(["NOCARD   "] * self.dimX)
                    self.cardtable[coordY-1][coordX] = card.cardtype + "    "
                    self.table[coordY*3][coordX] = card.gettop()
                    self.table[coordY*3+1][coordX] = card.getmiddle()
                    self.table[coordY*3+2][coordX] = card.getbottom()
                    
        else:
            print("Choose another card!")
                
            
    def replaceCard(self, card, coordX, coordY):
        ablereplace = (not ((self.cardtable[coordY][coordX] == "ENDCARD  ") \
            or (self.cardtable[coordY][coordX] == "STARTCARD") \
            or (self.cardtable[coordY][coordX] == "NOCARD   "))) \
            and card.cardtype == "RoF"
        if ablereplace:
            self.cardtable[coordY][coordX] = card.cardtype + "      "
            self.table[coordY*3][coordX] = card.gettop()
            self.table[coordY*3+1][coordX] = card.getmiddle()
            self.table[coordY*3+2][coordX] = card.getbottom()
        elif card.cardtype == "RoF":
            print("error, actioncard cant replace this card")
        else:
            print("error, this card cant replace others")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# test code 


        
card0 = StartCard()
card1 = RoundEndCard("G")
card2 = RoundEndCard("ND") 
card3 = RoundEndCard("NU")
interface = Interface()
# card1.turnCard()
interface.initCard(card0, card1, card2, card3)



card4 = PathCard(" R L+")
carrd4dirct = PathCard("URDL+")
cardRoF = ActionCard("RoF")
interface.insertCard(carrd4dirct, 0, 3)

interface.insertCard(carrd4dirct, 0, 4)
interface.insertCard(carrd4dirct, 0, 5)
interface.insertCard(carrd4dirct, 0, 1)
interface.insertCard(carrd4dirct, 0, 0)
interface.insertCard(carrd4dirct, 0, -1)
# interface.replaceCard(cardRoF, 0, 4)
# interface.replaceCard(carrd4dirct, 0, 2)
interface.printTitle()
interface.printBody()   
interface.printCardtable()
interface.replaceCard(cardRoF, 0, 3)
interface.printTitle()
interface.printBody()    
# interface.printCardtable()

        
        
        
        
        
        
        
        
        
        
        