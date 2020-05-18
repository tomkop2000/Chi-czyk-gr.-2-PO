# coding=utf-8
# coding: utf-8
import random
import codecs
from tkinter import *
import winsound


# klasa Nagroda (z niej dziedziczone będą treści nagórd i wartości, które one przyjmują)
class Nagroda:
    def __init__(self, data_string):  # wczytuje dane ze stringa, dane muszą być ustawione w odpowiedzniej kolejności, jak niżej i oddzielone znakiem "|"
        tmp_1 = data_string.split("|")
        self.nr_nagrody = tmp_1[0]
        self.wartosc = tmp_1[1]
        self.nagrody = tmp_1[2]

    def display_nagroda(self):  # metoda odpowiadająca za zwrócenie warości a odpowiadającej tresci nagrody
        a = str(self.nagrody)
        return a

    def display_wartosc(self):  # metoda odpowiadająca za zwrócenie warości a odpowiadającej tresci wartości
        a = int(self.wartosc)
        return a

    def load_nagrody():  # funkcja ładująca treści nagród z pliku
        # ładowanie bazy pytań o nazwie pytania.txt
        file_name = "nagrody.txt"
        f = codecs.open(file_name, "r", encoding="utf-8")
        lines = f.readlines()
        nagroda_1 = []
        for line in lines:
            if line != "\n":
                nagroda_1.append(Nagroda(line[0:-1]))
        f.close()
        return nagroda_1

    # klasa Okna, która dziedziczy z klasy Nagroda


class Okna(Nagroda):
    nagroda_1 = []  # lista obiektów Nagroda, naważniejszy element, przechowuje najwiażnejsze dane dotyczące treści nagród
    nagroda_1 = Nagroda.load_nagrody()  # ładowanie treści nagród do tablicy

    def choice_nagroda():  # metoda zwracająca losową wartość z przedziału od 1 do 8
        choice_number = random.randint(1, 8)
        choice_number = str(choice_number)
        return choice_number

    def nagroda_wys(choice_number):  # metoda zwracająca wartość a odpowiadającą treści nagrody z wylosowanej nagrody
        for nagroda in Okna.nagroda_1:
            if (nagroda.wartosc == choice_number):
                a = nagroda.display_nagroda()
                return a

    def nagroda_wartosc(choice_number):  # metoda zwracająca wartość a odpowiadającą wartości z wylosowanej nagrody
        for nagroda in Okna.nagroda_1:
            if (nagroda.wartosc == choice_number):
                a = nagroda.display_wartosc()
                return a

    def okno(muzyka, obraz):  # metoda wyświetlająca okno z terścią nagrody, obrazkiem oraz rozpoczyna odtwarzanie muzyki

        choice_number = Okna.choice_nagroda()
        a = Okna.nagroda_wys(choice_number)
        b = Okna.nagroda_wartosc(choice_number)

        winsound.PlaySound(muzyka, winsound.SND_ASYNC | winsound.SND_ALIAS)  # rozpoczęcie odtwarzania muzyki

        okno = Tk()
        okno.geometry("500x350+700+300")  # wyświetlenie okna o rozmiarze 500x500 pikseli
        img = PhotoImage(file=obraz)
        label_grafika = Label(okno, image=img)
        label = Label(okno, text=a)
        okno.title("Nagroda")  # nadanie tytułu okna po lewej stronie pasku stanu

        przycisk = Button(okno, text="OK", command=okno.destroy)  # przycisk zamykający okno

        # pakowanie przycisków i grafik
        label_grafika.pack(side="top", fill=X, expand=True)
        label.pack(side="top", fill=X, expand=True)
        przycisk.pack(expand=False)
        okno.mainloop()  # pętla która uniemożliwia zamknięcie okna
        winsound.PlaySound(None, winsound.SND_PURGE)  # zakończenie odtwarzania muzyki jeśli nie zakończyło się to wcześniej
        return b


class krolik(Okna):  # klasa krolik, dziedzicząda z klasy Okna
    def nagroda_krolika():
        obraz = "krolik.gif"  # wyświetlenie obrazka krasnala
        muzyka = "krolik.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyświetlenie okna i przypisanie k wartości logicznej
        return k


class swMikolaj(Okna):  # klasa swMikolaj, dziedzicząda z klasy Okna
    def nagroda_swMikolaja():
        obraz = "swMikolaj.gif"  # wyświetlenie obrazka sw Mikołaja
        muzyka = "swMikolaj.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyświetlenie okna i przypisanie k wartości logicznej
        return k


class kotek(Okna):  # klasa kotek, dziedzicząda z klasy Okna
    def nagroda_kota():
        obraz = "kotek.gif"  # wyświetlenie obrazka kotka
        muzyka = "kotek.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyświetlenie okna i przypisanie k wartości logicznej
        return k


"""
print(krolik.nagroda_krolika())

print(swMikolaj.nagroda_swMikolaja())

print(kotek.nagroda_kota())
"""