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
        self.nbplayer += 1
        # if this is not the first player we need to check if he is the youngest
        if self.nbplayer != 0:
            if self.playerlist[self.ageminindex].age > player.age:
                self.ageminindex = self.nbplayer-1
        else:
            self.ageminindex = 0
            
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
            for y in range(nbcard):
                for x in range(self.nbplayer):
                    if self.playerlist[x].insertCard(self.cardlist[self.cardlistindex]):
                        self.cardlistindex += 1
        
        
    def startGame(self, nbplayer, listplayer):
        for x in range(nbplayer):
            listplayer[x].resetPlayer(1)
            self.addPlayer(listplayer[x])
        self.sendCard()
        self.interface.initCard()
            
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
        
    def playActionCardRoF(self, playerindex,)   
        
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
                
    # def playOnePathCard(self, playerindex, cardindex, coordX, coordY):
    #     if(inter)
    
# test code
    
player1 = Player("titi", 18, "GOOD")
player2 = Player("toto", 17, "BAD")
player3 = Player("tutu", 19, "GOOD")
listplayer = [player1, player2, player3]
nbplayer = len(listplayer)
game1 = Game()
game1.startGame(nbplayer, listplayer)
game1.interface.printInterface()
game1.showEveryoneStat()
while(1):
    if (int(input("Entre 0 for play an action card, Entre 1 for play a path card"))):
        
        playerindexinput = int(input("请输入你的玩家号：0-"+str(game1.nbplayer-1)))
        cardindexinput = int(input("请输入你打的牌号：0-"+str(game1.playerlist[playerindexinput].index-1)))
        coordXinput = int(input("请输入X坐标："))
        coordYinput = int(input("请输入Y坐标："))
        game1.playPathCard(playerindexinput,cardindexinput,coordXinput,coordYinput)
    else:
        playerindexinput = int(input("请输入你的玩家号：0-"+str(game1.nbplayer-1)))
        cardindexinput = int(input("请输入你打的牌号：0-"+str(game1.playerlist[playerindexinput].index-1)))
        targetindexinput = int(input("请输入你目标的玩家号：0-"+str(game1.nbplayer-1)))
        game1.playActionToolsCard(playerindexinput,cardindexinput,targetindexinput)
    game1.interface.printInterface()
    game1.showEveryoneStat()


