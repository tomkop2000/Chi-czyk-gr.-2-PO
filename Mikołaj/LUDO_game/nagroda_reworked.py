# coding=utf-8
# coding: utf-8
import random
import codecs
from tkinter import *
import winsound
import time

# klasa Nagroda (z niej dziedziczone będą treści nagórd i wartości, które one przyjmują)
class Nagroda:

    # ładowanie bazy pytań o nazwie pytania.txt
    file_name = "nagrody.txt"
    nagroda_1 = []

    def __init__(self):  # wczytuje dane ze stringa, dane muszą być ustawione w odpowiedzniej kolejności, jak niżej i oddzielone znakiem "|"
        # ładowanie bazy pytań o nazwie pytania.txt
        f = codecs.open(self.file_name, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            if line != "\n":
                self.nagroda_1.append(line[0:-1])
        f.close()




    def okno(self,obraz):

        losowa_zmienna = random.randint(0, 8-1)#8 to liczba pytań

        data_string = self.nagroda_1[losowa_zmienna]

        #dane do wyświetlania pytań
        tmp_1 = data_string.split("|")
        nr_nagrody = tmp_1[0]
        wartosc = tmp_1[1]
        nagrody = tmp_1[2]

        self.tk = Tk()
        self.tk.title = "Game"
        self.canvas = Canvas(self.tk, width=500, height=300, bd=0, highlightthickness=0)
        self.canvas.pack()

        self.tekstura = PhotoImage(file=obraz)

        #powołanie przycisku i testu
        self.przycisk = Button(self.tk, text="OK", command=self.tk.destroy)  # przycisk zamykający okno
        self.label = Label(self.tk, text=nagrody)

        #powołanie zdjecia
        self.postac = self.canvas.create_image(1, 1, image=self.tekstura, anchor=NW)

        #"spakowanie" napisu i przycisku
        self.label.pack(side="top", fill=X, expand=True)
        self.przycisk.pack(expand=False)

        #presuniecie postaci na pozycje 0,0
        self.canvas.move(self.postac, 0, 0)

        #zmienne konfiguracyjne
        self.pozycja =0
        self.velocity = 0.5
        self.time = 1


        self.draw()  # Changed per Bryan Oakley's comment
        mainloop()
        winsound.PlaySound(None, winsound.SND_PURGE)  # zakończenie odtwarzania muzyki jeśli nie zakończyło się to wcześniej
        return wartosc


class krolik(Nagroda):
    def glos(self):
        muzyka= "krolik.wav"
        winsound.PlaySound(muzyka, winsound.SND_ASYNC | winsound.SND_ALIAS)



    def draw(self):
        if self.pozycja > 300:
            self.velocity = self.velocity * (-1)
        elif self.pozycja < 0:
            self.velocity = self.velocity * (-1)

        self.canvas.move(self.postac, self.velocity, 0)
        self.canvas.after(self.time, self.draw)  # (time_delay, method_to_execute)
        self.pozycja += self.velocity

    def animacja(self):
        obraz = "krolik.gif"

        a = self.okno(obraz)
        return a

    def pytanie_krolika(self):
        self.glos()
        a =self.animacja()
        return a

if __name__ == "__main__":
    krolik = krolik()
    print(krolik.pytanie_krolika())
