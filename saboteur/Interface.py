# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:26:23 2022

@author: pc
"""
from Card import *
import random

class Interface:
    
    def __init__(self, dimX = 9, dimY = 5, endgame = 0):
        
        self.dimX = dimX
        self.dimY = dimY
        self.cardtable = [[EmptyCard() for x in range(self.dimX)] for y in range(self.dimY)]
        self.table = [["     "] * self.dimX for y in range(self.dimY*3)]
        self.endgame = endgame
        self.endcardtable = []
    
    def printCardtable(self):
        
        for y in range(self.dimY):
            for x in range(self.dimX):
                print(" " + self.cardtable[y][x].cardtype + " ", end="")
            print("")
        
        
    def printInterface(self):
        print("Current mine state:")
        print(" |", end="")
        for x in range(self.dimX):
            print("  " + str(x) + "  ", end="")
        print("")
        print("-+", end="")
        for x in range(self.dimX):
            print("-----", end="")
        print("")
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
    
    
    def initCard(self):
        self.endgame = 0
        self.dimX = 9
        self.dimY = 5
        self.cardtable = [[EmptyCard() for x in range(self.dimX)] for y in range(self.dimY)]
        self.table = [["     "] * self.dimX for y in range(self.dimY*3)]
        
        endcardordre = [x for x in range(3)]
        random.shuffle(endcardordre)
        if endcardordre == [0, 1, 2]:
            roundendcard0 = RoundEndCard("G     ")
            roundendcard1 = RoundEndCard("ND    ")
            roundendcard2 = RoundEndCard("NU    ")
        elif endcardordre == [0, 2, 1]:
            roundendcard0 = RoundEndCard("G     ")
            roundendcard1 = RoundEndCard("NU    ")
            roundendcard2 = RoundEndCard("ND    ")
        elif endcardordre == [1, 0, 2]:
            roundendcard0 = RoundEndCard("ND    ")
            roundendcard1 = RoundEndCard("G     ")
            roundendcard2 = RoundEndCard("NU    ")
        elif endcardordre == [1, 2, 0]:
            roundendcard0 = RoundEndCard("ND    ")
            roundendcard1 = RoundEndCard("NU    ")
            roundendcard2 = RoundEndCard("G     ")
        elif endcardordre == [2, 0, 1]:
            roundendcard0 = RoundEndCard("NU    ")
            roundendcard1 = RoundEndCard("G     ")
            roundendcard2 = RoundEndCard("ND    ")
        else:
            roundendcard0 = RoundEndCard("NU    ")
            roundendcard1 = RoundEndCard("ND    ")
            roundendcard2 = RoundEndCard("G     ")
            
        self.cardtable[2][0] = StartCard()
        self.table[6][0] = StartCard().gettop()
        self.table[7][0] = StartCard().getmiddle()
        self.table[8][0] = StartCard().getbottom()
        
        self.cardtable[0][8] = roundendcard0
        self.table[0][8] = roundendcard0.gettop()
        self.table[1][8] = roundendcard0.getmiddle()
        self.table[2][8] = roundendcard0.getbottom()
        
        self.cardtable[2][8] = roundendcard1
        self.table[6][8] = roundendcard1.gettop()
        self.table[7][8] = roundendcard1.getmiddle()
        self.table[8][8] = roundendcard1.getbottom()
        
        self.cardtable[4][8] = roundendcard2
        self.table[12][8] = roundendcard2.gettop()
        self.table[13][8] = roundendcard2.getmiddle()
        self.table[14][8] = roundendcard2.getbottom()
        

    def insertCard(self, card, coordX, coordY):
        
        # reset the condition value
        put_aviliable = 1
        
        # if the card want to be put is not a path card
        if (not(card.cardtype == "URDL+ " or \
                card.cardtype == "URD + " or \
                card.cardtype == "UR L+ " or \
                card.cardtype == "UR  + " or \
                card.cardtype == "U  L+ " or \
                card.cardtype == "U D + " or \
                card.cardtype == " R L+ " or \
                card.cardtype == "URDL- " or \
                card.cardtype == "URD - " or \
                card.cardtype == "UR L- " or \
                card.cardtype == "UR  - " or \
                card.cardtype == "U  L- " or \
                card.cardtype == "U D - " or \
                card.cardtype == " R L- " or \
                card.cardtype == "U   - " or \
                card.cardtype == " R  - ")):
            put_aviliable = 0
            print("error, need put a path card!")
        
        # if there is already a card placed at the coord    
        if coordX >= 0 and coordX < self.dimX and coordY >= 0 and coordY < self.dimY:
            if self.cardtable[coordY][coordX].cardtype != "EMPTCD":
                put_aviliable = 0
                print("error, can not put a card above another!")
        
        # if there is no card at top left right bottom or the card is end card we dont test the condition of the path
        card_ontop = not ((coordY <= 0 or coordX < 0 or coordX >= self.dimX) \
            or (self.cardtable[coordY-1][coordX].cardtype == "NU    ") \
            or (self.cardtable[coordY-1][coordX].cardtype == "ND    ") \
            or (self.cardtable[coordY-1][coordX].cardtype == "G     ") \
            or (self.cardtable[coordY-1][coordX].cardtype == "EMPTCD"))
        card_atbottom = not ((coordY >= self.dimY-1 or coordX < 0 or coordX >= self.dimX) \
            or (self.cardtable[coordY+1][coordX].cardtype == "NU    ") \
            or (self.cardtable[coordY+1][coordX].cardtype == "ND    ") \
            or (self.cardtable[coordY+1][coordX].cardtype == "G     ") \
            or (self.cardtable[coordY+1][coordX].cardtype == "EMPTCD"))
        card_atleft = not ((coordX <= 0 or coordY < 0 or coordY >= self.dimY) \
            or (self.cardtable[coordY][coordX-1].cardtype == "NU    ") \
            or (self.cardtable[coordY][coordX-1].cardtype == "ND    ") \
            or (self.cardtable[coordY][coordX-1].cardtype == "G     ") \
            or (self.cardtable[coordY][coordX-1].cardtype == "EMPTCD"))
        card_atright = not ((coordX >= self.dimX-1 or coordY < 0 or coordY >= self.dimY) \
            or (self.cardtable[coordY][coordX+1].cardtype == "NU    ") \
            or (self.cardtable[coordY][coordX+1].cardtype == "ND    ") \
            or (self.cardtable[coordY][coordX+1].cardtype == "G     ") \
            or (self.cardtable[coordY][coordX+1].cardtype == "EMPTCD"))
        
        # if there is card but the path has conflict
        if (card_ontop and (self.table[coordY*3-1][coordX] != "( | )" or card.cardtype[0] != "U")) \
            or (card_atbottom and (self.table[coordY*3+3][coordX] != "( | )" or card.cardtype[2] != "D")) \
            or (card_atleft and (self.table[coordY*3+1][coordX-1][3] != "-" or card.cardtype[3] != "L")) \
            or (card_atright and (self.table[coordY*3+1][coordX+1][1] != "-" or card.cardtype[1] != "R")):
            put_aviliable = 0
            print("error, can not put here path conflict!")
            
        # if there is no card next to the place we wanna to put then is not correct
        if not (card_ontop or card_atbottom or card_atleft or card_atright):
            put_aviliable = 0
            print("error, no card anround the place chose!")
        
        
                    
        if put_aviliable == 1:
            # if the card is place inside of the table 
            if coordX >= 0 and coordX < self.dimX and coordY >= 0 and coordY < self.dimY:
                self.cardtable[coordY][coordX] = card
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
                        self.cardtable[y].insert(0,EmptyCard())
                    self.cardtable[coordY][0] = card
                    self.table[coordY*3][0] = card.gettop()
                    self.table[coordY*3+1][0] = card.getmiddle()
                    self.table[coordY*3+2][0] = card.getbottom()
                if coordX == self.dimX:
                    self.dimX += 1
                    for y in range(self.dimY*3):
                        self.table[y].append("     ")
                    for y in range(self.dimY):
                        self.cardtable[y].append(EmptyCard())
                    self.cardtable[coordY][coordX] = card
                    self.table[coordY*3][coordX] = card.gettop()
                    self.table[coordY*3+1][coordX] = card.getmiddle()
                    self.table[coordY*3+2][coordX] = card.getbottom()
                if coordY == -1:
                    self.dimY += 1
                    for y in range(3):
                        self.table.insert(0, ["     "] * self.dimX)
                    self.cardtable.insert(0, [EmptyCard() for x in range(self.dimX)])
                    self.cardtable[coordY+1][coordX] = card
                    self.table[0][coordX] = card.gettop()
                    self.table[1][coordX] = card.getmiddle()
                    self.table[2][coordX] = card.getbottom()
                if coordY == self.dimY:
                    self.dimY += 1
                    for y in range(3):
                        self.table.append(["     "] * self.dimX)
                    self.cardtable.append([EmptyCard() for x in range(self.dimX)])
                    self.cardtable[coordY][coordX] = card
                    self.table[coordY*3][coordX] = card.gettop()
                    self.table[coordY*3+1][coordX] = card.getmiddle()
                    self.table[coordY*3+2][coordX] = card.getbottom()
                    
                 
            if (not (coordY <= 0 or coordX < 0 or coordX >= self.dimX))\
                and (self.cardtable[coordY-1][coordX].cardtype == "NU    "\
                or self.cardtable[coordY-1][coordX].cardtype == "ND    "\
                or self.cardtable[coordY-1][coordX].cardtype == "G     "):
                self.cardtable[coordY-1][coordX].turnCard()
                self.table[(coordY-1)*3][coordX] = self.cardtable[coordY-1][coordX].gettop()
                self.table[(coordY-1)*3+1][coordX] = self.cardtable[coordY-1][coordX].getmiddle()
                self.table[(coordY-1)*3+2][coordX] = self.cardtable[coordY-1][coordX].getbottom()
                if self.cardtable[coordY-1][coordX].cardtype == "G     ":
                    self.endgame = 1
                        
            if (not (coordY >= self.dimY-1 or coordX < 0 or coordX >= self.dimX))\
                and ((self.cardtable[coordY+1][coordX].cardtype == "NU    ") \
                or self.cardtable[coordY+1][coordX].cardtype == "ND    " \
                or self.cardtable[coordY+1][coordX].cardtype == "G     "):
                
                self.cardtable[coordY+1][coordX].turnCard()
                self.table[(coordY+1)*3][coordX] = self.cardtable[coordY+1][coordX].gettop()
                self.table[(coordY+1)*3+1][coordX] = self.cardtable[coordY+1][coordX].getmiddle()
                self.table[(coordY+1)*3+2][coordX] = self.cardtable[coordY+1][coordX].getbottom()  
                
                if self.cardtable[coordY+1][coordX].cardtype == "G     ":
                    self.endgame = 1
                        
            if (not (coordX <= 0 or coordY < 0 or coordY >= self.dimY))\
                and (self.cardtable[coordY][coordX-1].cardtype == "NU    "\
                or self.cardtable[coordY][coordX-1].cardtype == "ND    "\
                or self.cardtable[coordY][coordX-1].cardtype == "G     "):
                self.cardtable[coordY][coordX-1].turnCard()
                self.table[coordY*3][coordX-1] = self.cardtable[coordY][coordX-1].gettop()
                self.table[coordY*3+1][coordX-1] = self.cardtable[coordY][coordX-1].getmiddle()
                self.table[coordY*3+2][coordX-1] = self.cardtable[coordY][coordX-1].getbottom()       
                if self.cardtable[coordY][coordX-1].cardtype == "G     ":
                    self.endgame = 1
                        
            if (not (coordX >= self.dimX-1 or coordY < 0 or coordY >= self.dimY))\
                and (self.cardtable[coordY][coordX+1].cardtype == "NU    "\
                or self.cardtable[coordY][coordX+1].cardtype == "ND    "\
                or self.cardtable[coordY][coordX+1].cardtype == "G     "):
                self.cardtable[coordY][coordX+1].turnCard()
                self.table[coordY*3][coordX+1] = self.cardtable[coordY][coordX+1].gettop()
                self.table[coordY*3+1][coordX+1] = self.cardtable[coordY][coordX+1].getmiddle()
                self.table[coordY*3+2][coordX+1] = self.cardtable[coordY][coordX+1].getbottom()
                if self.cardtable[coordY][coordX+1].cardtype == "G     ":
                    self.endgame = 1
            return 1
        else: 
            return 0
            
    def replaceCard(self, card, coordX, coordY):
        
        replace_aviliable = 1
        
        if self.cardtable[coordY][coordX].cardtype == "EMPTCD":
            print("error, there is nothing to be replaced!")
            replace_aviliable = 0
        elif self.cardtable[coordY][coordX].cardtype == "STATCD":
            print("error, the start path cant be replaced!")
            replace_aviliable = 0
        elif self.cardtable[coordY][coordX].cardtype == "NU    "\
            or self.cardtable[coordY][coordX].cardtype == "ND    "\
            or self.cardtable[coordY][coordX].cardtype == "G     ":    
            print("error, the end path cant be replaced!")
            replace_aviliable = 0
        elif card.cardtype != "RoF   ":
            print("error, only fall rock can replace path card!")
            replace_aviliable = 0
        
        if replace_aviliable:
            self.cardtable[coordY][coordX] = card
            self.table[coordY*3][coordX] = card.gettop()
            self.table[coordY*3+1][coordX] = card.getmiddle()
            self.table[coordY*3+2][coordX] = card.getbottom()
           
    def showRoundEndCard(self, card, coordX, coordY):
        show_aviliable = 0
        
        if not(self.cardtable[coordY][coordX].cardtype == "NU    "\
            or self.cardtable[coordY][coordX].cardtype == "ND    "\
            or self.cardtable[coordY][coordX].cardtype == "G     "):    
            print("error, only the end path canbe shown!")
        else:
            if card.cardtype != "MAP   ":
                print("error, only the map card has this fonction!")
            else:
                if self.cardtable[coordY][coordX].canturn == 0:
                    print("error, this card already showed up!")
                else:
                    print(self.cardtable[coordY][coordX].backtop)
                    print(self.cardtable[coordY][coordX].backmiddle)
                    print(self.cardtable[coordY][coordX].backbottom)
                    show_aviliable = 1
      
        return show_aviliable
        
        if replace_aviliable:
            self.cardtable[coordY][coordX] = card
            self.table[coordY*3][coordX] = card.gettop()
            self.table[coordY*3+1][coordX] = card.getmiddle()
            self.table[coordY*3+2][coordX] = card.getbottom()
           
            
            
# test code 


        

# interface1 = Interface()

# interface1.initCard()


# card4 = PathCard(" R L+ ")
# carrd4dirct = PathCard("URDL+ ")
# cardRoF = ActionCard("RoF   ")


# interface1.insertCard(carrd4dirct, 0, 3)
# interface1.insertCard(carrd4dirct, 0, 4)
# interface1.insertCard(carrd4dirct, 0, 5)
# interface1.insertCard(carrd4dirct, 0, 1)
# interface1.insertCard(carrd4dirct, 0, 0)

# interface1.insertCard(carrd4dirct, 0, -1)
# interface1.insertCard(carrd4dirct, 1, 0)
# interface1.insertCard(carrd4dirct, 2, 0)
# interface1.insertCard(carrd4dirct, 3, 0)
# interface1.insertCard(carrd4dirct, 4, 0)
# interface1.insertCard(carrd4dirct, 5, 0)
# interface1.insertCard(carrd4dirct, 6, 0)
# interface1.insertCard(carrd4dirct, 7, 0)
# interface1.printInterface()   
# interface1.printCardtable()
# interface1.insertCard(carrd4dirct, 8, 0)
# print("endgame=", end = "")
# print(interface1.endgame)
# interface1.printInterface()   
# interface1.printCardtable()
# interface1.insertCard(carrd4dirct, 9, 0)
# interface1.insertCard(carrd4dirct, 9, 1)
# interface1.insertCard(carrd4dirct, 9, 2)
# interface1.insertCard(carrd4dirct, 9, 3)
# print("endgame=", end = "")
# print(interface1.endgame)
# interface1.insertCard(carrd4dirct, 9, 4)
# interface1.insertCard(carrd4dirct, 9, 5)
# print("endgame=", end = "")
# print(interface1.endgame)
# interface1.insertCard(carrd4dirct, 9, 6)
# interface1.insertCard(carrd4dirct, 9, 7)

# interface1.insertCard(carrd4dirct, 1, 2)
# interface1.replaceCard(cardRoF, 0, 4)
# interface1.replaceCard(carrd4dirct, 0, 2)

# interface1.printInterface()   
# interface1.printCardtable()


        
        
        
        
        
        
        
        
        
        
        