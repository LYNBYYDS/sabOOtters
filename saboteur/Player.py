#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:30:20 2022

@author: ly
"""
class Player:
    
    def __init__(self, nbCard, role, index = 0):
        
        self.role = role
        self.index = index
        self.nbCard = nbCard
        self.cardtable = ["NOCARD " * nbCard];
        self.table_top = ["          " * nbCard]
        self.table_middle = [str(x) + ")          " for x in range(nbCard)]
        self.table_bottom = ["          " * nbCard]
        
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
        # for x in range(len(self.table_bottom)):
    
    def insertCard(self, card, )
        
        
player1 = Player(5, "bad")
# print(player1.__dict__)
player1.printPlayerCard()