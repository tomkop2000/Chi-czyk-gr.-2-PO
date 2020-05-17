# coding=utf-8
# coding: utf-8
# importowanie potrzebych bibliotek
import random
import codecs
from tkinter import *
#import tkinter
#import winsound





# klasa przeszkoda (z niej dziedziczone beda pytania i opsoiwedzi)
class Przeszkoda:
    # wczytuje dane ze stringa, dane musza byc ustawione w odpowiedzniej kolejnosci, jak niżej i oddzielone znakiem "|"
    def __init__(self, data_string):
        tmp_1 = data_string.split("|")
        self.nr_pytania = tmp_1[0]
        self.pytanie = tmp_1[1]
        self.odp_A = tmp_1[2]
        self.odp_B = tmp_1[3]
        self.odp_C = tmp_1[4]
        self.poprawna_odp = tmp_1[5]

    # metoda odpowiadajaca za zwrocenie warosci a odpowiadajacej tresci pytania
    def display_pytanie(self):
        a = str(self.pytanie)
        return a

    # metoda odpowiadajaca za zwrocenie warosci a odpowiadajacej tresci odpowiedzi A
    def display_A(self):
        a = str(self.odp_A)
        return a

    # metoda odpowiadajaca za zwrocenie warosci a odpowiadajacej tresci odpowiedzi B
    def display_B(self):
        a = str(self.odp_B)
        return a

    # metoda odpowiadajaca za zwrocenie warosci a odpowiadajacej tresci odpowiedzi C
    def display_C(self):
        a = str(self.odp_C)
        return a

    # metoda odpowiadajaca za zwrocenie warosci poprawnej odpowiedzi od 1 do 3
    def display_poprawna_odp(self):
        a = int(self.poprawna_odp)
        return a

    def load_pytania():  # funkcja ladujaca pytania z pliku
        # ladowanie bazy pytan o nazwie pytania.txt
        file_name = "pytania.txt"
        f = codecs.open(file_name, "r", encoding="utf-8")
        lines = f.readlines()
        przeszkoda_1 = []
        for line in lines:
            if line != "\n":
                przeszkoda_1.append(Przeszkoda(line[0:-1]))
        f.close()
        return przeszkoda_1

    # klasa Okno, ktora dziedziczy z klasy Przeszkoda


class Okno(Przeszkoda):
    przeszkoda_1 = []  # lista obiektow Przeszkoda, naważniejszy element, przechowuje najwiażnejsze dane dotyczace pytan
    przeszkoda_1 = Przeszkoda.load_pytania()

    def choice_pytanie():  # metoda zwracajaca losowa wartosc z przedzialu od 1 do 81
        choice_number = random.randint(1, 81)
        choice_number = str(choice_number)
        return choice_number

    def pytanie(choice_number):  # metoda zwracajaca wartosc a odpowiadajaca tresc pytania z wylosowanego pytania
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                a = przeszkoda.display_pytanie()
                return a

    def odp_A(choice_number):  # metoda zwracajaca wartosc a odpowiadajaca tresci odpowiedzi A z wylosowanego pytania
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                a = przeszkoda.display_A()
        return a

    def odp_B(choice_number):  # metoda zawierajaca wartosc a odpowiadajaca tresci odpowiedzi B z wylosowanego pytania
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                a = przeszkoda.display_B()
                return a

    def odp_C(choice_number):  # metoda zwracajaca wartosc a odpowiadajaca tresci odpowiedzi C z wylosowanego pytania
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                a = przeszkoda.display_C()
                return a

    def poprawna_odp(choice_number):  # metoda zwracajaca wartosc a odpowiadajaca wartosci poprawnej odpowiedzi z przedzialu od 1 do 3
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                a = przeszkoda.display_poprawna_odp()
                return a

    def sprawdzanie(a, choice_number):  # metoda sprawdzajaca poprawnosc udzielonej odpowiedzi i zwracajaca 1 w przypadku dobrej odpowiedzi oraz 0 w przypadku blednej odpowiedzi
        for przeszkoda in Okno.przeszkoda_1:
            if (przeszkoda.nr_pytania == choice_number):
                b = przeszkoda.display_poprawna_odp()
                if (a == b):
                    return 1
                else:
                    return 0

    def okno(muzyka, obraz):  # metoda wyswietlajaca okno z pytaniem, obrazkiem oraz 3 możliwymi do wyboru odpowiedziami oraz rozpoczyna odtwarzanie muzyki

        choice_number = Okno.choice_pytanie()
        a = Okno.pytanie(choice_number)
        b = Okno.odp_A(choice_number)
        c = Okno.odp_B(choice_number)
        d = Okno.odp_C(choice_number)

        #winsound.PlaySound(muzyka, winsound.SND_ASYNC | winsound.SND_ALIAS)  # rozpoczecie odtwarzania muzyki

        okno = Tk()
        okno.geometry("600x500+700+300")  # wyswietlenie okna o rozmiarze 500x500 pikseli
        img = PhotoImage(file=obraz)
        label_grafika = Label(okno, image=img)
        label = Label(okno, text=a)
        okno.title("Pytanie")  # nadanie tytulu okna po lewej stronie pasku stanu

        odp = IntVar()
        przyciskA = Radiobutton(okno, text=b, fg="red", value=1, variable=odp)  # wyswietlenie odpowiedzi A, ktorej wartosc jest rowna 1

        przyciskB = Radiobutton(okno, text=c, fg="red", value=2, variable=odp)  # wyswietlenie odpowiedzi B, ktorej wartosc jest rowna 2

        przyciskC = Radiobutton(okno, text=d, fg="red", value=3, variable=odp)  # wyswietlenie odpowiedzi C, ktorej wartosc jest rowna 3

        przycisk = Button(okno, text="Zapisz odpowiedź", command=okno.destroy)  # przycisk zamykajacy okno

        # pakowanie przyciskow i grafik
        label_grafika.pack(side="top", fill=X, expand=True)
        label.pack(side="top", fill=X, expand=True)
        przyciskA.pack(side="top", fill=X, expand=True)
        przyciskB.pack(side="top", fill=X, expand=True)
        przyciskC.pack(side="top", fill=X, expand=True)
        przycisk.pack(expand=False)
        okno.mainloop()  # petla ktora uniemożliwia zamkniecie okna
        k = Okno.sprawdzanie(odp.get(), choice_number)  # sprawdzenie czy wybrana odpowiedź byla poprawna oraz zwrocenie wartosci logicznej 1 dla poprawnej odpowiedzi i 0 dla blednej
        #.PlaySound(None, winsound.SND_PURGE)  # zakonczenie odtwarzania muzyki jesli nie zakonczylo sie to wczesniej
        return k


class krasnoludek(Okno):  # klasa krasnoludek, dziedziczada z klasy okno
    def pytanie_krasnala():
        obraz = "krasnal.gif"  # wyswietlenie obrazka krasnala
        muzyka = "krasnal.wav"  # odtworzenie muzyki
        k = Okno.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


class wilk(Okno):
    def pytanie_wilka():
        obraz = "wilk.gif"  # wyswietlenie obrazka wilka
        muzyka = "wilk.wav"  # odtworzenie muzyki
        k = Okno.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


class niedzwiedz(Okno):
    def pytanie_niedzwiedzia():
        obraz = "niedzwiedz.gif"  # wyswietlenie obrazka niedźwiedzia
        muzyka = "niedzwiedz.wav"  # odtworzenie muzyki
        k = Okno.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


"""
k=wilk.pytanie_wilka()
print(k)
m=krasnoludek.pytanie_krasnala()
print(m)
l=niedzwiedz.pytanie_niedzwiedzia()
print(l)
"""

