import random
import codecs
from tkinter import *
import winsound


# klasa Nagroda (z niej dziedziczone beda tresci nagórd i wartosci, które one przyjmuja)
class Nagroda:
    def __init__(self, data_string):  # wczytuje dane ze stringa, dane musza być ustawione w odpowiedzniej kolejnosci, jak nizej i oddzielone znakiem "|"
        tmp_1 = data_string.split("|")
        self.nr_nagrody = tmp_1[0]
        self.wartosc = tmp_1[1]
        self.nagrody = tmp_1[2]

    def display_nagroda(self):  # metoda odpowiadajaca za zwrócenie warosci a odpowiadajacej tresci nagrody
        a = str(self.nagrody)
        return a

    def display_wartosc(self):  # metoda odpowiadajaca za zwrócenie warosci a odpowiadajacej tresci wartosci
        a = int(self.wartosc)
        return a

    def load_nagrody():  # funkcja ladujaca tresci nagród z pliku
        # ladowanie bazy pytan o nazwie pytania.txt
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
    nagroda_1 = []  # lista obiektów Nagroda, nawazniejszy element, przechowuje najwiaznejsze dane dotyczace tresci nagród
    nagroda_1 = Nagroda.load_nagrody()  # ladowanie tresci nagród do tablicy

    def choice_nagroda():  # metoda zwracajaca losowa wartosć z przedzialu od 1 do 8
        choice_number = random.randint(1, 8)
        choice_number = str(choice_number)
        return choice_number

    def nagroda_wys(choice_number):  # metoda zwracajaca wartosć a odpowiadajaca tresci nagrody z wylosowanej nagrody
        for nagroda in Okna.nagroda_1:
            if (nagroda.wartosc == choice_number):
                a = nagroda.display_nagroda()
                return a

    def nagroda_wartosc(choice_number):  # metoda zwracajaca wartosć a odpowiadajaca wartosci z wylosowanej nagrody
        for nagroda in Okna.nagroda_1:
            if (nagroda.wartosc == choice_number):
                a = nagroda.display_wartosc()
                return a

    def okno(muzyka, obraz):  # metoda wyswietlajaca okno z terscia nagrody, obrazkiem oraz rozpoczyna odtwarzanie muzyki

        choice_number = Okna.choice_nagroda()
        a = Okna.nagroda_wys(choice_number)
        b = Okna.nagroda_wartosc(choice_number)

        winsound.PlaySound(muzyka, winsound.SND_ASYNC | winsound.SND_ALIAS)  # rozpoczecie odtwarzania muzyki

        okno = Tk()
        okno.geometry("500x350+700+300")  # wyswietlenie okna o rozmiarze 500x500 pikseli
        img = PhotoImage(file=obraz)
        label_grafika = Label(okno, image=img)
        label = Label(okno, text=a)
        okno.title("Nagroda")  # nadanie tytulu okna po lewej stronie pasku stanu

        przycisk = Button(okno, text="OK", command=okno.destroy)  # przycisk zamykajacy okno

        # pakowanie przycisków i grafik
        label_grafika.pack(side="top", fill=X, expand=True)
        label.pack(side="top", fill=X, expand=True)
        przycisk.pack(expand=False)
        okno.mainloop()  # petla która uniemozliwia zamkniecie okna
        winsound.PlaySound(None, winsound.SND_PURGE)  # zakonczenie odtwarzania muzyki jesli nie zakonczylo sie to wczesniej
        return b


class krolik(Okna):  # klasa krolik, dziedziczada z klasy Okna
    def nagroda_krolika():
        obraz = "krolik.gif"  # wyswietlenie obrazka krasnala
        muzyka = "krolik.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


class swMikolaj(Okna):  # klasa swMikolaj, dziedziczada z klasy Okna
    def nagroda_swMikolaja():
        obraz = "swMikolaj.gif"  # wyswietlenie obrazka sw Mikolaja
        muzyka = "swMikolaj.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


class kotek(Okna):  # klasa kotek, dziedziczada z klasy Okna
    def nagroda_kota():
        obraz = "kotek.gif"  # wyswietlenie obrazka kotka
        muzyka = "kotek.wav"  # odtworzenie muzyki
        k = Okna.okno(muzyka, obraz)  # wyswietlenie okna i przypisanie k wartosci logicznej
        return k


"""
print(krolik.nagroda_krolika())

print(swMikolaj.nagroda_swMikolaja())

print(kotek.nagroda_kota())
"""