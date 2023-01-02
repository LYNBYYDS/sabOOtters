#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:39:42 2022

@author: ly
"""

from Player import *
from Interface import *
from Cardset import *


class Game:
    
    def __init__(self, playerlist = [], nbplayer = 0, playerindex = 0, ageminindex = 0,\
                 cardlist = [], cardlistindex = 0):
        
        self.interface = Interface()
        self.playerlist = playerlist
        self.nbplayer = nbplayer
        self.playerindex = playerindex
        self.ageminindex = ageminindex
        self.cardlist = cardlist
        self.cardlistindex = cardlistindex
        
        
    def addPlayer(self, player):
        self.playerlist.append(player)
        # if this is not the first player we need to check if he is the youngest
        if self.nbplayer != 0:
            if self.playerlist[self.ageminindex].age > player.age:
                self.ageminindex = self.nbplayer
        else:
            self.ageminindex = 0
        self.nbplayer += 1 
        self.playerindex = self.ageminindex
        
    def showEveryoneCards(self):
        for index in range(self.nbplayer):
            self.playerlist[index].printPlayerCard()
    
    def showEveryoneStat(self):
        for index in range(self.nbplayer):
            self.playerlist[index].printPlayerStat()
        
    def sendCard(self):
        listcardindex = [[0, x] for x in range(40)]
        for y in range(27):
            listcardindex.append([1, y])
        
        takeordre = [x for x in range(67)]
        random.shuffle(takeordre)
        newstackcard = Cardset()
        self.cardlist = []
        self.cardlistindex = 0
        for i in range(67):
            if(listcardindex[takeordre[i]][0] == 0):
                self.cardlist.append(newstackcard.pathcards[listcardindex[takeordre[i]][1]])
            else:
                self.cardlist.append(newstackcard.actioncards[listcardindex[takeordre[i]][1]])
        nbcard = 0       
        if self.nbplayer > 10:
            nbcard = -1
            print("error, too many players")
            return 0
        elif self.nbplayer < 3:
            nbcard = -1
            print("error, need more players")
            return 0
        else:
            
            if self.nbplayer >= 3 and self.nbplayer <= 5:
                nbcard = 6
            elif self.nbplayer >= 6 and self.nbplayer <= 7:
                nbcard = 5
            else:
                nbcard = 4
            for x in range(self.nbplayer):
                self.playerlist[x].nbCard = nbcard
                self.playerlist[x].resetPlayer(1)
            for y in range(nbcard):
                for x in range(self.nbplayer):
                    if self.playerlist[x].insertCard(self.cardlist[self.cardlistindex]):
                        self.cardlistindex += 1
            
       
    def inportPlayerInfo(self):
        while(1):
            datain = input("How many players are going to play?(Entre a number between 3 and 10): ")
            if datain.isdigit():
                nbPlayer = int(datain)
                if(nbPlayer <= 10 and nbPlayer >= 3):
                    break
              
        for playerindex in range(nbPlayer):
            playername = input("Please entre the " + str(playerindex+1)+ "th player's name(Can not be empty): ")
            while(not playername):
                playername = input("Please entre the " + str(playerindex+1)+ "th player's name(Can not be empty): ")
            datain = input("Please entre the " + str(playerindex+1)+ " th player's age(Entre a number between 3 and 122): ")
            while(1):
                if datain.isdigit():
                    playerage = int(datain)
                    if playerage <= 122 and playerage >= 3:
                        break
                datain = input("Please entre the " + str(playerindex+1)+ "th player's age(Entre a number between 3 and 122): ")
            self.addPlayer(Player(playername, playerage))
        if self.nbplayer >= 3 and self.nbplayer <= 5:
            deletenum = 0
        elif self.nbplayer >= 6 and self.nbplayer <= 7:
            deletenum = 1
        else:
            deletenum = 2
        if deletenum != 0:
            for i in range(deletenum):
                for x in range(self.nbplayer):
                    del self.playerlist[x].cardtable[-1]
                    del self.playerlist[x].table_top[-1]
                    del self.playerlist[x].table_middle[-1]
                    del self.playerlist[x].table_bottom[-1]
           
    def playPathCard(self, playerindex, cardindex, coordX, coordY):
        if self.interface.insertCard(self.playerlist[playerindex].cardtable[cardindex], coordX, coordY):
            self.playerlist[playerindex].removeCard(cardindex)
            if self.cardlistindex < 67:
                self.takeOneCard(playerindex)
                return 1
            else:
                return 0
        else: 
            return 0
        
    def playActionToolsCard(self, playerindex, cardindex, targetindex):
        if self.playerlist[targetindex].changeToolStat(self.playerlist[playerindex].cardtable[cardindex]):
            self.playerlist[playerindex].removeCard(cardindex)
            if self.cardlistindex < 67:
                self.takeOneCard(playerindex)
                return 1
            else:
                return 0
        else: 
            return 0
        
    def playActionRoFCard(self, playerindex, cardindex, coordX, coordY): 
        if self.interface.replaceCard(self.playerlist[playerindex].cardtable[cardindex], coordX, coordY):
            self.playerlist[playerindex].removeCard(cardindex)
            if self.cardlistindex < 67:
                self.takeOneCard(playerindex)
                return 1
            else:
                return 0
        else: 
            return 0
    
    def takeOneCard(self, playerindex):
        if(playerindex >= self.nbplayer or playerindex < 0):
            print("error, plater index out of range")
        if(self.cardlistindex >= 67):
            print("error, there no more card to take")
        else:
            if(self.playerlist[playerindex].insertCard(self.cardlist[self.cardlistindex])):
                self.cardlistindex += 1
            else:
                print("error, fail to get a card")
    
    def startGame(self):
        self.inportPlayerInfo()
        self.sendCard()
        self.interface.initCard()
        
        while(not self.interface.endgame):
            self.showEveryoneStat()
            self.playCard()
        
        
    def playCard(self):
        print("It is player " + self.playerlist[self.playerindex].playername + " turn:")
        self.interface.printInterface()
        self.playerlist[self.playerindex].printPlayerStat()
        if self.nbplayer >= 3 and self.nbplayer <= 5:
            nbcard = 6
        elif self.nbplayer >= 6 and self.nbplayer <= 7:
            nbcard = 5
        else:
            nbcard = 4
        while(1):
            datain = input("Which card u want to play(entre a number between 0 and " + str(nbcard) + "): ")
            if datain.isdigit():
                cardindex = int(datain)
                if(cardindex <= nbcard and cardindex >= 0):
                    break
        if self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "URDL+ "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "URD + "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "UR L+ "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "UR  + "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "U  L+ "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "U D + "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == " R L+ "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "URDL- "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "URD - "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "UR L- "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "UR  - "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "U  L- "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "U D - "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == " R L- "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "U   - "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == " R  - ":
            while(1):
                datain = input("Where you want to play this card?\nCoord x:(entre a number between -1 and " + str(self.interface.dimX) + "): ")
                if datain.isdigit():
                    coordX = int(datain)
                    if(coordX <= self.interface.dimX and coordX >= -1):
                        break
            while(1):
                datain = input("Coord y:(entre a number between -1 and " + str(self.interface.dimY) + "): ")
                if datain.isdigit():
                    coordY = int(datain)
                    if(coordY <= self.interface.dimY and coordY >= -1):
                        break
            if (not self.playPathCard(self.playerindex, cardindex, coordX, coordY)):
                self.playCard()
                return 1
                    
        elif self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "W+    "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "Li+   "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "P+    "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "LiP+  "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "LiW+  "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "PW+   "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "Wx    "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "Lix   "\
            or self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "Px    ":
            while(1):
                datain = input("Which player want to play to(entre a number between 1 and " + str(self.nbplayer) + "): ")
                if datain.isdigit():
                    playerindex = int(datain)
                    if(playerindex <= self.nbplayer and playerindex >= 1):
                        break
            while (not self.playActionToolsCard(self.playerindex, cardindex, playerindex-1)):
                if self.playActionToolsCard(self.playerindex, cardindex, playerindex-1):
                    break
            
        elif self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "RoF   ":
            while(1):
                datain = input("Where you want to play this card?\nCoord x:(entre a number between -1 and " + str(self.interface.dimX) + "): ")
                if datain.isdigit():
                    coordX = int(datain)
                    if(coordX <= self.interface.dimX and coordX >= -1):
                        break
            while(1):
                datain = input("Coord y:(entre a number between -1 and " + str(self.interface.dimY) + "): ")
                if datain.isdigit():
                    coordY = int(datain)
                    if(coordY <= self.interface.dimY and coordY >= -1):
                        break
            while (not self.playActionRoFCard(self.playerindex, cardindex, coordX, coordY)):
                if self.playActionRoFCard(self.playerindex, cardindex, coordX, coordY):
                    break
            
        
        # elif self.playerlist[self.playerindex].cardtable[cardindex].cardtype == "MAP   ":
        print(str(self.playerindex)+"   "+str(self.nbplayer))
        if self.playerindex < self.nbplayer-1:
            self.playerindex += 1
        elif self.playerindex == self.nbplayer-1:
            self.playerindex = 0
        else:
            print("error, index of player out of range!")
                 
                 
    
                
    # def playOnePathCard(self, playerindex, cardindex, coordX, coordY):
    #     if(inter)
    
# test code
    
# player1 = Player("titi", 18, "GOOD")
# player2 = Player("toto", 17, "BAD")
# player3 = Player("tutu", 19, "GOOD")
# listplayer = [player1, player2, player3]
# nbplayer = len(listplayer)
game1 = Game()
game1.startGame()
game1.interface.printInterface()

# game1.startGame(nbplayer, listplayer)
# game1.interface.printInterface()
# game1.showEveryoneStat()
# while(1):
#     if (int(input("Entre 0 for play an action card, Entre 1 for play a path card"))):
        
#         playerindexinput = int(input("请输入你的玩家号：0-"+str(game1.nbplayer-1)))
#         cardindexinput = int(input("请输入你打的牌号：0-"+str(game1.playerlist[playerindexinput].index-1)))
#         coordXinput = int(input("请输入X坐标："))
#         coordYinput = int(input("请输入Y坐标："))
#         game1.playPathCard(playerindexinput,cardindexinput,coordXinput,coordYinput)
#     else:
#         playerindexinput = int(input("请输入你的玩家号：0-"+str(game1.nbplayer-1)))
#         cardindexinput = int(input("请输入你打的牌号：0-"+str(game1.playerlist[playerindexinput].index-1)))
#         targetindexinput = int(input("请输入你目标的玩家号：0-"+str(game1.nbplayer-1)))
#         game1.playActionToolsCard(playerindexinput,cardindexinput,targetindexinput)
#     game1.interface.printInterface()
#     game1.showEveryoneStat()


