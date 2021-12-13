# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:25:46 2021

@author: hasan.ajami
"""
print("\n----Komposition----\n")
class Raum:
    def __init__(self, flaeche, ID):
        self.ID = ID
        self.flaeche = flaeche
        
    def zeigeGroesse(self):
        return "Raumgröße: " + str(self.flaeche) + " m²"
    
class Gebaeude():
    def __init__(self, name, anzahl, flaeche):
        self.name = name
        if(anzahl == 0):
            self.anzahl = 1
        else:
            self.anzahl = anzahl
        self.flaeche = flaeche
        self.raumflaeche = self.flaeche / self.anzahl
        self.raeume =  []
        
        for i in range(1, anzahl+1):
            self.raeume.append(Raum(self.raumflaeche, i))
        
    def zeigeRaume(self):
        for raum in self.raeume:
            print("Raum " + str(raum.ID) + " " + raum.zeigeGroesse()) 
        

obj_gebauede = Gebaeude("Schule", 10, 100) #10 Räume, 100m² Fläche
obj_gebauede2 = Gebaeude("Bank", 5, 130)
print(obj_gebauede.name)
obj_gebauede.zeigeRaume()
print(obj_gebauede2.name)
obj_gebauede2.zeigeRaume()

#---------------Aggregation---------------
print("\n----Aggregation----\n")

class Student(object):
    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

class Vorlesung:
    studenten = []
    
    def __init__(self, student):
        self.student = student
        self.studenten.append(self.student)
    
    def werKommt(self):
        
        if(int(len(self.studenten) < 3)):
           print("Es müssen mindestens 3 Studenten zur Vorlesung kommen!")
        else: 
            for st in self.studenten:
                print(st.vorname + " " + st.name + " kommt zur Vorlesung")
    
    def wieVieleKommen(self):
        return str(len(self.studenten)) + " Studneten kommen zur Vorlesung..."
    
student1 = Student("Ajami", "Hasan")
student2 = Student("Gaedali", "Elyas")
student3 = Student("Stanczak", "Dominik")

meineVorlesung = Vorlesung(student1)
meineVorlesung = Vorlesung(student2)

meineVorlesung.werKommt()
print(meineVorlesung.wieVieleKommen())