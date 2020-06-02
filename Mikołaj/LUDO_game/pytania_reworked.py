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
    file_name = "pytania.txt"
    przeszkoda_1 = []

    def __init__(self):  # wczytuje dane ze stringa, dane muszą być ustawione w odpowiedzniej kolejności, jak niżej i oddzielone znakiem "|"
        # ładowanie bazy pytań o nazwie pytania.txt
        f = codecs.open(self.file_name, "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            if line != "\n":
                self.przeszkoda_1.append(line[0:-1])
        f.close()



    def okno(self,obraz):


        losowa_zmienna = random.randint(0, 81-1)#81 to liczba pytań

        data_string = self.przeszkoda_1[losowa_zmienna]

        #dane do wyświetlania pytań
        tmp_1 = data_string.split("|")
        self.nr_pytania = tmp_1[0]
        self.pytanie = tmp_1[1]
        self.odp_A = tmp_1[2]
        self.odp_B = tmp_1[3]
        self.odp_C = tmp_1[4]
        self.poprawna_odp = tmp_1[5]

        self.tk = Tk()
        self.tk.title = "Pytanie"
        self.canvas = Canvas(self.tk, width=500, height=300, bd=0, highlightthickness=0)
        self.canvas.pack()

        self.tekstura = PhotoImage(file=obraz)

        #powołanie przycisku i testu

        self.odp = IntVar()

        self.przyciskA = Radiobutton(self.tk, text=self.odp_A, fg="red", value=1, variable=self.odp)  # wyświetlenie odpowiedzi A, której wartość jest równa 1
        self.przyciskB = Radiobutton(self.tk, text=self.odp_B, fg="red", value=2, variable=self.odp)  # wyświetlenie odpowiedzi B, której wartość jest równa 2
        self.przyciskC = Radiobutton(self.tk, text=self.odp_C, fg="red", value=3, variable=self.odp)  # wyświetlenie odpowiedzi C, której wartość jest równa 3

        self.przycisk = Button(self.tk, text="OK", command=self.tk.destroy)  # przycisk zamykający okno
        self.label = Label(self.tk, text=self.pytanie)#tekst pytnia

        #powołanie zdjecia
        self.postac = self.canvas.create_image(1, 1, image=self.tekstura, anchor=NW)

        #"spakowanie" napisu i przycisku
        self.label.pack(side="top", fill=X, expand=True)

        self.przyciskA.pack(expand=False)
        self.przyciskB.pack(expand=False)
        self.przyciskC.pack(expand=False)
        self.przycisk.pack(expand=False)

        #presuniecie postaci na pozycje 0,0
        self.canvas.move(self.postac, 0, 0)

        #zmienne konfiguracyjne
        self.pozycja =0
        self.velocity = 0.5
        self.time = 1







class wilk(Nagroda):
    def glos(self):
        muzyka= "wilk.wav"
        winsound.PlaySound(muzyka, winsound.SND_ASYNC | winsound.SND_ALIAS)

    def draw(self):
        if self.pozycja > 300:
            self.velocity = self.velocity * (-1)
        elif self.pozycja < 0:
            self.velocity = self.velocity * (-1)

        self.canvas.move(self.postac, self.velocity, 0)
        self.id = self.canvas.after(self.time, self.draw)  # (time_delay, method_to_execute)
        self.pozycja += self.velocity

    def animacja(self):
        obraz = "wilk.gif"

        a = self.okno(obraz)
        return a

    def pytanie_wilka(self):
        self.glos()
        self.animacja()


        self.draw()  # Changed per Bryan Oakley's comment
        mainloop()
        self.canvas.after_cancel(self.id)
        winsound.PlaySound(None, winsound.SND_PURGE)  # zakończenie odtwarzania muzyki jeśli nie zakończyło się to wcześniej

        #czesc sprawdzajaca poprawnosc pytania
        #print(odp.get())
        #print(self.poprawna_odp)
        if int(self.odp.get() )== int(self.poprawna_odp):
            return 1
        else:
            return 0

if __name__ == "__main__":
    wilk = wilk()
    print(wilk.pytanie_wilka())
