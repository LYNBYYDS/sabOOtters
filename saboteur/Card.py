# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:53:04 2022

@author: pc
"""

class Card:
    
    
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
        
    
    def printCardGraph(self):
        print(self.top)
        print(self.middle)
        print(self.bottom)

    def gettop(self):
        return self.top
        
    def getmiddle(self):
        return self.middle    
        
    def getbottom(self):
        return self.bottom    
        
        
        
# start card        
class StartCard(Card):
    def __init__(self):
        super().__init__("( | )","(-S-)","( | )")
        
class RoleCard(Card):  
    pass      
        
class ActionCard(Card):
    
    def __init__(self, cardtype):
        self.cardtype = cardtype 
    
        # tools card
        # W = wagonnet, Li = lampe de mine, P = pioche de mine
        # + = repair, x = broke
        
        if self.cardtype == "W+":
            super().__init__("(DEF)","( W )","(   )")
        elif self.cardtype == "Li+":
            super().__init__("(DEF)","( L )","(   )")
        elif self.cardtype == "P+":
            super().__init__("(DEF)","( P )","(   )")
        elif self.cardtype == "Wx":
            super().__init__("(ATT)","( W )","(   )")
        elif self.cardtype == "Lix":
            super().__init__("(ATT)","( L )","(   )")
        elif self.cardtype == "Px":
            super().__init__("(ATT)","( P )","(   )")
        
        # Rock card
        elif self.cardtype == "RoF":
            super().__init__("(   )","(RoF)","(   )")
        
        # Map card
        elif self.cardtype == "MAP":
            super().__init__("( M )","(MAP)","( P )")       
        
class PathCard(Card):

    def __init__(self, cardtype):
        self.cardtype = cardtype 
        
        
        
        # tools card
        # U = up, R = right, D = down, L = left 
        # + = repair, x = broke
        
        if self.cardtype == "URDL+":
            super().__init__("( | )","(-+-)","( | )")
        elif self.cardtype == "URD +":
            super().__init__("( | )","( +-)","( | )")
        elif self.cardtype == "UR L+":
            super().__init__("( | )","(-+-)","(   )")
        elif self.cardtype == "UR  +":
            super().__init__("( | )","( +-)","(   )")
        elif self.cardtype == "U  L+":
            super().__init__("( | )","(-+ )","(   )")
        elif self.cardtype == "U D +":
            super().__init__("( | )","( | )","( | )")
        elif self.cardtype == " R L+":
            super().__init__("(   )","(---)","(   )")
        elif self.cardtype == "URDL-":
            super().__init__("( | )","(-x-)","( | )")
        elif self.cardtype == "URD -":
            super().__init__("( | )","( x-)","( | )")
        elif self.cardtype == "UR L-":
            super().__init__("( | )","(-x-)","(   )")
        elif self.cardtype == "UR  -":
            super().__init__("( | )","( x-)","(   )")
        elif self.cardtype == "U  L-":
            super().__init__("( | )","(-x )","(   )")
        elif self.cardtype == "U D -":
            super().__init__("( | )","( x )","( | )")
        elif self.cardtype == " R L-":
            super().__init__("(   )","(-x-)","(   )")
        elif self.cardtype == "U   -":
            super().__init__("( | )","( x )","(   )")
        elif self.cardtype == " R  -":
            super().__init__("(   )","( x )","(   )")

class RoundEndCard(Card):
    def __init__(self, cardtype):
        self.cardtype = cardtype 
        
        
        # tools card
        # W = wagonnet, Li = lampe de mine, P = pioche de mine
        # + = repair, x = broke
        
        if self.cardtype == "NU":
            super().__init__("(   )","(END)","(   )")
            self.backtop = "( | )"
            self.backmiddle = "(-N )"
            self.backbottom = "(   )"
        elif self.cardtype == "ND":
            super().__init__("(   )","(END)","(   )")
            self.backtop = "(   )"
            self.backmiddle = "(-N )"
            self.backbottom = "( | )"
        elif self.cardtype == "G":
            super().__init__("(   )","(END)","(   )")
            self.backtop = "( | )"
            self.backmiddle = "(-G-)"
            self.backbottom = "( | )"
    
    def turnCard(self):
        if self.cardtype == "NU":
            self.top = "( | )"
            self.middle = "(-N )"
            self.bottom = "(   )"
        elif self.cardtype == "ND":
            super().__init__("(   )","(END)","(   )")
            self.top = "(   )"
            self.middle = "(-N )"
            self.bottom = "( | )"
        elif self.cardtype == "G":
            super().__init__("(   )","(END)","(   )")
            self.top = "( | )"
            self.middle = "(-G-)"
            self.bottom = "( | )"
            
class GoldCard(Card):
    def __init__(self, nbGold):
        if self.nbGold == "1G":
            super().__init__("(   )","(1 G)","(   )")
        elif self.nbGold == "2G":
            super().__init__("(   )","(2 G)","(   )")
        elif self.nbGold == "3G":
            super().__init__("(   )","(3 G)","(   )")
            
            
            
            
            

# card1 = ActionCard('Wx')
# card1.printCardGraph()
# lista = [['a', 'b'],['c', 'd'],['e', 'f']]
# for y in range(3):
#     lista.append(['a']*3 )
#     lista[3][1] = 'b'
# print(lista)