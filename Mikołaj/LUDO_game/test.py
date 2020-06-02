from tkinter import *
import random
import time

class Ball:

    def __init__(self,obraz):
        self.tk = Tk()

        self.tk.title = "Game"
        self.canvas = Canvas(self.tk, width=500, height=300, bd=0, highlightthickness=0)
        self.canvas.pack()

        self.tekstura = PhotoImage(file=obraz)

        # powołanie przycisku i testu
        self.przycisk = Button(self.tk, text="OK", command=self.tk.destroy)  # przycisk zamykający okno
        self.label = Label(self.tk, text="nagrody")

        # powołanie zdjecia
        self.postac = self.canvas.create_image(1, 1, image=self.tekstura, anchor=NW)

        # "spakowanie" napisu i przycisku
        self.label.pack(side="top", fill=X, expand=True)
        self.przycisk.pack(expand=False)

        # presuniecie postaci na pozycje 0,0
        self.canvas.move(self.postac, 0, 0)

        # zmienne konfiguracyjne
        self.pozycja = 0
        self.velocity = 0.5
        self.time = 1

        self.draw()  # Changed per Bryan Oakley's comment
        mainloop()
        print(123)


    def draw(self):
        if self.pozycja > 300:
            self.velocity = self.velocity * (-1)
        elif self.pozycja < 0:
            self.velocity = self.velocity * (-1)

        self.canvas.move(self.postac, self.velocity, 0)
        self.canvas.after(self.time, self.draw)  #(time_delay, method_to_execute)
        self.pozycja += self.velocity


if __name__ == "__main__":
    obraz = "wilk.gif"
    kotek = Ball(obraz)
