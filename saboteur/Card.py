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
        
class EmptyCard(Card):
    def __init__(self,cardtype = "EMPTCD"):
        self.cardtype = cardtype
        super().__init__("     ","     ","     ")
      
class StartCard(Card):
    def __init__(self,cardtype = "STATCD"):
        self.cardtype = cardtype
        
        # startcard
        # STARTCD
        
        super().__init__("( | )","(-S-)","( | )")
        
        
class RoleCard(Card):  
    def __init__(self, cardtype):
        self.cardtype = cardtype
        
        # role card
        # GOOD/BAD
        
        if self.cardtype == "GOOD  ":
            super().__init__("(   )","(GUD)","(   )")
        elif self.cardtype == "BAD   ":
            super().__init__("(   )","(BAD)","(   )")    
        else: 
            print("error, creat card fail")
        
class ActionCard(Card):
    
    def __init__(self, cardtype):
        self.cardtype = cardtype 
    
        # tool card
        # W = wagonnet, Li = lampe de mine, P = pioche de mine
        # + = repair, x = broke
        
        if self.cardtype == "W+    ":
            super().__init__("(DEF)","( W )","(   )")
        elif self.cardtype == "Li+   ":
            super().__init__("(DEF)","( L )","(   )")
        elif self.cardtype == "P+    ":
            super().__init__("(DEF)","( P )","(   )")
        elif self.cardtype == "LiP+  ":
            super().__init__("(DEF)","( L )","( P )")
        elif self.cardtype == "LiW+  ":
            super().__init__("(DEF)","( L )","( W )")
        elif self.cardtype == "PW+   ":
            super().__init__("(DEF)","( P )","( W )")
        elif self.cardtype == "Wx    ":
            super().__init__("(ATT)","( W )","(   )")
        elif self.cardtype == "Lix   ":
            super().__init__("(ATT)","( L )","(   )")
        elif self.cardtype == "Px    ":
            super().__init__("(ATT)","( P )","(   )")
        
        # Rock card
        elif self.cardtype == "RoF   ":
            super().__init__("(   )","(RoF)","(   )")
        
        # Map card
        elif self.cardtype == "MAP   ":
            super().__init__("( M )","(MAP)","( P )")   
        
        else: 
            print("error, creat card fail")
        
class PathCard(Card):

    def __init__(self, cardtype):
        self.cardtype = cardtype 
        
        # path card
        # U = up, R = right, D = down, L = left 
        # + = repair, x = broke
        
        if self.cardtype == "URDL+ ":
            super().__init__("( | )","(-+-)","( | )")
        elif self.cardtype == "URD + ":
            super().__init__("( | )","( +-)","( | )")
        elif self.cardtype == "UR L+ ":
            super().__init__("( | )","(-+-)","(   )")
        elif self.cardtype == "UR  + ":
            super().__init__("( | )","( +-)","(   )")
        elif self.cardtype == "U  L+ ":
            super().__init__("( | )","(-+ )","(   )")
        elif self.cardtype == "U D + ":
            super().__init__("( | )","( | )","( | )")
        elif self.cardtype == " R L+ ":
            super().__init__("(   )","(---)","(   )")
        elif self.cardtype == "URDL- ":
            super().__init__("( | )","(-x-)","( | )")
        elif self.cardtype == "URD - ":
            super().__init__("( | )","( x-)","( | )")
        elif self.cardtype == "UR L- ":
            super().__init__("( | )","(-x-)","(   )")
        elif self.cardtype == "UR  - ":
            super().__init__("( | )","( x-)","(   )")
        elif self.cardtype == "U  L- ":
            super().__init__("( | )","(-x )","(   )")
        elif self.cardtype == "U D - ":
            super().__init__("( | )","( x )","( | )")
        elif self.cardtype == " R L- ":
            super().__init__("(   )","(-x-)","(   )")
        elif self.cardtype == "U   - ":
            super().__init__("( | )","( x )","(   )")
        elif self.cardtype == " R  - ":
            super().__init__("(   )","( x )","(   )")
        else: 
            print("error, creat card fail")

class RoundEndCard(Card):
    def __init__(self, cardtype):
        self.cardtype = cardtype 
        self.canturn = 1
        
        # end card
        # NU = Rock with a path top left ND = Rock with a path down left G = Gold
        
        if self.cardtype == "NU    ":
            self.backtop = "( | )"
            self.backmiddle = "(-N )"
            self.backbottom = "(   )"
            super().__init__("(   )","(END)","(   )")
            
        elif self.cardtype == "ND    ":
            self.backtop = "(   )"
            self.backmiddle = "(-N )"
            self.backbottom = "( | )"
            super().__init__("(   )","(END)","(   )")
            
        elif self.cardtype == "G     ":
            self.backtop = "( | )"
            self.backmiddle = "(-G-)"
            self.backbottom = "( | )"
            super().__init__("(   )","(END)","(   )")
            
        else: 
            print("error, creat card fail")
    
    # to turn the endroundcard to show the path
    def turnCard(self):
        if self.canturn:
            self.top = self.backtop
            self.middle = self.backmiddle
            self.bottom = self.backbottom
            self.canturn = 0
            return 1
        else: 
            print("error, already turned")
            return 0
        
class GoldCard(Card):
    def __init__(self, cardtype):
        self.cardtype = cardtype 
        
        if self.cardtype == "1G    ":
            super().__init__("(   )","(1 G)","(   )")
        elif self.cardtype == "2G    ":
            super().__init__("(   )","(2 G)","(   )")
        elif self.cardtype == "3G    ":
            super().__init__("(   )","(3 G)","(   )")
            
        else: 
            print("error, creat card fail")


