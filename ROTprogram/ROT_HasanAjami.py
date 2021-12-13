# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:53:18 2021

@author: hasan.ajami
"""
buchstaben = "abcdefghijklmnopqrstuvwxyz"
buchtaben = buchstaben.upper()

verstecken = input("möchtest du verschlüsseln? (y, n): ")
ROTwert = int(input("Um wie viele Stellen rotieren?: "))
ausgabe = []

if(verstecken == "y"): 
    eingabe = input("Bitte schreibe den Satz zum verschlüsseln: ") 
    eingabe = eingabe.upper()
    
    for buchstabe in eingabe:
        if(buchstabe != " "):
            a = buchtaben.index(buchstabe) + ROTwert
            if(a >= len(buchstaben)):
                a =  -(len(buchstaben)-ROTwert) + buchtaben.index(buchstabe)
                ausgabe.append(buchstaben[a])
            else:   
                 ausgabe.append(buchstaben[a])
        else:
            ausgabe.append(" ")
        
else:    
    eingabe = input("Bitte schreibe den Satz zum entschlüsseln: ")
    eingabe = eingabe.upper()
    
    for buchstabe in eingabe:
        if(buchstabe != " "):
            a = buchtaben.index(buchstabe)
            ausgabe.append(buchstaben[a-ROTwert])
        else:
            ausgabe.append(" ")

ausgabe = "".join(ausgabe)
ausgabe = ausgabe.upper()
print("Dein Satz ist: %s" %ausgabe)