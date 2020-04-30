import pygame, sys, os, image
import pyglet
import random
import codecs
from tkinter import *
import winsound

class Przeszkoda:
    def __init__(self,data_string):
        tmp_1=data_string.split("|")
        self.nr_pytania=tmp_1[0]
        self.pytanie=tmp_1[1]
        self.odp_A=tmp_1[2]
        self.odp_B=tmp_1[3]
        self.odp_C=tmp_1[4]
        self.poprawna_odp=tmp_1[5]
    
    def display(self):
        print(self.pytanie)
        print(self.odp_A)
        print(self.odp_B)
        print(self.odp_C)

    def display_pytanie(self):
        a=str(self.pytanie)
        return a

    def display_A(self):
        a=str(self.odp_A)
        return a

    def display_B(self):
        a = str(self.odp_B)
        return a

    def display_C(self):
        a = str(self.odp_C)
        return a

    def display_poprawna_odp (self):
        a = int(self.poprawna_odp)
        return a

    def prepare_save(self):
        return (self.nr_pytania+"|"+self.pytanie+"|"+self.odp_A+"|"+self.odp_B+"|"+self.odp_C+"|"+self.poprawna_odp)
    

class Okno(Przeszkoda):
    def choice():
        choice_number=random.randint(1,61)
        choice_number=str(choice_number)
        return choice_number
    def pytanie(choice_number):
        for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
               a = przeszkoda.display_pytanie()
               return a
    def odp_A(choice_number):
        for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
               a =przeszkoda. display_A()
        return a
    def odp_B(choice_number):
        for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
                a = przeszkoda.display_B()
                return a
    def odp_C(choice_number):
        for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
                a = przeszkoda.display_C()
                return a
    def poprawna_odp(choice_number):
        for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
                a = przeszkoda.display_poprawna_odp()
                return a
    def sprawdzanie(a, choice_number):
         for przeszkoda in przeszkoda_1:
            if(przeszkoda.nr_pytania==choice_number):
                b=przeszkoda.display_poprawna_odp()
                if (a==b):
                    print("poprawna odp")
                    return 1
                else:
                    print("bledna odp")
                    return 0
   

    def okno(muzyka, obraz):

        choice_number = Okno.choice()
        a = Okno.pytanie(choice_number)
        b = Okno.odp_A(choice_number)
        c = Okno.odp_B(choice_number)
        d = Okno.odp_C(choice_number)
        
        winsound.PlaySound(muzyka, winsound.SND_ASYNC|winsound.SND_ALIAS)

        okno =Tk()
        okno.geometry('500x500')
        img = PhotoImage(file= obraz)
        label_grafika=Label(okno, image = img)
        label=Label(okno, text = a)
        topFrame = Frame(okno)
        topFrame.pack()
        bottomFrame=Frame(okno)
        bottomFrame.pack(side=BOTTOM)
        odp = IntVar()
        przyciskA=Radiobutton(okno,text = b , fg="red",value =1, variable=odp)

        przyciskB=Radiobutton(okno,text = c, fg="red", value=2, variable=odp)

        przyciskC=Radiobutton(okno,text = d, fg="red",value=3, variable=odp)

        
        przycisk=Button(okno,text="Zapisz odpowiedź", command=okno.destroy)

        przycisk.pack()
        label.pack()
        label_grafika.pack()
        przyciskA.pack()
        przyciskB.pack()
        przyciskC.pack()
        okno.mainloop()
        k = Okno.sprawdzanie(odp.get(),choice_number)
        winsound.PlaySound(None, winsound.SND_PURGE)
        return k

class krasnoludek(Okno):
    def pytanie_krasnala():
        obraz = "krasnal.gif"
        muzyka ="krasnal.wav"
        k=Okno.okno(muzyka,obraz)
        return k

class wilk(Okno):
    def pytanie_wilka():
        obraz="wilk.gif"
        muzyka="wilk.wav"
        k=Okno.okno(muzyka,obraz)
        return k

class niedzwiedz(Okno):
    def pytanie_niedzwiedzia():
        obraz="niedzwiedz.gif"
        muzyka="niedzwiedz.wav"
        k=Okno.okno(muzyka,obraz)
        return k

przeszkoda_1=[]
def load():
    file_name="pytania.txt"
    f=codecs.open(file_name,"r", encoding="utf-8")
    lines=f.readlines()
    przeszkoda_1=[]
    for line in lines:
        if line!="\n":
            przeszkoda_1.append(Przeszkoda(line[0:-1]))
    f.close()
    return przeszkoda_1
przeszkoda_1=load()


k=wilk.pytanie_wilka()
print(k)
m=krasnoludek.pytanie_krasnala()
print(m)
l=niedzwiedz.pytanie_niedzwiedzia()
print(l)


