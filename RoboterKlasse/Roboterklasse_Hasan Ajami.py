# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:08:55 2021

@author: Hasan Ajami
"""

class Roboter:
    def __init__(self, name, orientation = "none"): #orientation is the direction   
        self.orientation = orientation
        self.name = name[0:10]  #max. 10 letters name
        self.x = 0
        self.y = 0
        self.position = [self.x, self.y]
    
    def Move(self, distance = 1):
        while True:
            try:
                orient = str(input("Bitte Richtung eingeben: "))
                if orient == "south" or orient == "west" or orient == "north" or orient == "east" or orient == "stop" and type(self.distance) != str:
                            if orient == "stop":
                                break
                            else:
                                self.distance = abs(int(input("Bitte Schritte eingeben: ")))
                            if orient == "south":
                                self.position[1] -= self.distance
                                self.orientation = "south"
                            elif orient == "north":
                                self.position[1] += self.distance
                                self.orientation = "north"
                            elif orient == "west":
                                self.position[0] -= self.distance
                                self.orientation = "west"
                            elif orient == "east":
                                self.position[0] += self.distance
                                self.orientation = "east"                        
                            print("Die Position lautet %s und die Orientierung ist: %s" %(self.position, self.orientation))
                else:
                    print("Bitte nur south, west, north, east oder stop eingeben!")
            except ValueError: #avoinding user mistake
                print("Bitte nur south, west, north, east oder stop oder gültige Zahlen eingeben!")

        print("Die letzte Position von %s lautet: %s" %(self.name, self.position))

roboter_Hasan = Roboter("Mr. Hasan3kljölkfajsdölkf")
print("Dein Roboter heißt %s" %roboter_Hasan.name)
roboter_Hasan.Move()