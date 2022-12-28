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
    
    def __init__(self, playerlist = [], nbplayer = 0, playerindex = 0, ageminindex = 0, cardlist = [], cardlistindex = 0):
        
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
        for index in range(nbPlayer):
            self.playerlist[index].printPlayerCard()
        
    def sendCard(self):
        listcardindex = [[0, x] for x in range(40)]
        for y in range(27):
            listcardindex.append([1, y])
        
        takeordre = [x for x in range(67)]
        random.shuffle(takeordre)
        
        self.cardlist = []
        self.cardlistindex = 0
        for i in range(67):
            if(listcardindex[takeordre[i]][0] == 0):
                self.cardlist.append(self.newstackcard.pathcards[listcardindex[takeordre[i]][1]])
            else:
                self.cardlist.append(self.newstackcard.actioncards[listcardindex[takeordre[i]][1]])
                
        if nbplayer > 10:
            nbcard = -1
            print("error, too many players")
            return 0
        elif nbplayer < 3:
            nbcard = -1
            print("error, need more players")
            return 0
        else:
            if nbplayer >= 3 and nbplayer <= 5:
                nbcard = 6
            elif nbplayer >= 6 and nbplayer <= 7:
                nbcard = 5
            else:
                nbcard = 4
            for y in range(nbcard):
                for x in range(nbplayer):
                    self.playerlist[x].insertCard(self.cardlist[listcardindex])
                    listcardindex += 1
        
        
    def startGame(self, nbplayer, listplayer):
        for x in range(nbplayer):
            listplayer[x].resetPlayer(1)
            self.addPlayer(listplayer[x])
        self.sendCard()
            
        
        
        
    def takeOneCard(self, playerindex):
        if(playerindex >= nbplater or playerindex < 0):
            print("error, plater index out of range")
        if(cardlistindex >= 67):
            print("error, there no more card to take")
        else:
            if(self.playerlist[playerindex].insertCard(self.cardlist[self.cardlistindex])):
                cardlistindex += 1
            else:
                print("error, fail to get a card")
                
    # def playOnePathCard(self, playerindex, cardindex, coordX, coordY):
    #     if(inter)
    
    
    
player1 = Player("titi", 18, "GOOD")
player2 = Player("toto", 17, "BAD")
player3 = Player("tutu", 19, "GOOD")


game1 = Game()
game1.addPlayer(player1)
game1.addPlayer(player2)
game1.addPlayer(player3)
game1.sendCard()

