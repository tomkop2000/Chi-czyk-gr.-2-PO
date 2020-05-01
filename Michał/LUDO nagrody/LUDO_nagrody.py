
import pygame, sys, os, image
import pyglet
import random
import codecs
from tkinter import *
import winsound

class Nagroda:
    def __init__(self,data_string):
        tmp_1=data_string.split("|")
        self.nr_nagrody=tmp_1[0]
        self.wartosc=tmp_1[1]
        self.nagrody=tmp_1[2]
        

    
    def display(self):
        print(self.nagrody)
        print(self.wartosc)


    def display_nagroda(self):
        a=str(self.nagrody)
        return a

    def display_wartosc (self):
        a = int(self.wartosc)
        return a

    

class Okno(Nagroda):
    def choice():
        choice_number=random.randint(1,8)
        choice_number=str(choice_number)
        return choice_number
    def nagroda_wys (choice_number):
        for nagroda in nagroda_1:
            if(nagroda.wartosc==choice_number):
               a = nagroda.display_nagroda()
               return a
    
    def nagroda_wartosc (choice_number):
        for nagroda in nagroda_1:
            if(nagroda.wartosc==choice_number):
               a = nagroda.display_wartosc()
               return a

   

    def okno(muzyka, obraz):

        choice_number = Okno.choice()
        a = Okno.nagroda_wys(choice_number)
        b = Okno.nagroda_wartosc(choice_number)
        
        winsound.PlaySound(muzyka, winsound.SND_ASYNC|winsound.SND_ALIAS)

        okno =Tk()
        okno.geometry('500x500')
        img = PhotoImage(file= obraz)
        label_grafika=Label(okno, image = img)
        label=Label(okno, text = a)
        okno.title("Nagroda")
        topFrame = Frame(okno)
        topFrame.pack()
        bottomFrame=Frame(okno)
        bottomFrame.pack()
        
        przycisk=Button(okno,text="OK", command=okno.destroy)

        przycisk.pack()
        label.pack()
        label_grafika.pack()
        okno.mainloop()
        winsound.PlaySound(None, winsound.SND_PURGE)
        return b

class krolik(Okno):
    def nagroda_krolika():
        obraz = "krolik.gif"
        muzyka ="krolik.wav"
        k=Okno.okno(muzyka,obraz)
        return k

class swMikolaj(Okno):
    def nagroda_swMikolaja():
        obraz="swMikolaj.gif"
        muzyka="swMikolaj.wav"
        k=Okno.okno(muzyka,obraz)
        return k

class kotek(Okno):
    def nagroda_kota():
        obraz="kotek.gif"
        muzyka="kotek.wav"
        k=Okno.okno(muzyka,obraz)
        return k

nagroda_1=[]
def load():
    file_name="nagrody.txt"
    f=codecs.open(file_name,"r", encoding="utf-8")
    lines=f.readlines()
    nagroda_1=[]
    for line in lines:
        if line!="\n":
            nagroda_1.append(Nagroda(line[0:-1]))
    f.close()
    return nagroda_1
nagroda_1=load()

k=krolik.nagroda_krolika()
print(k)
m=swMikolaj.nagroda_swMikolaja()
print(m)
l=kotek.nagroda_kota()
print(l)
