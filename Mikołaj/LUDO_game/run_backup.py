while True:

    if kolejka == 1:  # w sensie numer gracza

        print("Trwa tura gracza nr. ", kolejka)

        if player_1.pionki_stan == [1, 1, 1, 1]:
            max_licznik = 3

        elif (player_1.pionki_stan[0] == 2 or player_1.pionki_stan[1] == 2 or player_1.pionki_stan[2] == 2 or
              player_1.pionki_stan[3] == 2):
            max_licznik = 1

        while True:

            if licznik == max_licznik:
                break

            oczka = player_1.losowanie()
            print("Kostka wylosowała: ", oczka)

            if oczka == 6:
                pionek = player_1.wyborPionka()

                if player_1.pionki_stan[pionek - 1] == 1:
                    player_1.losowyRuchTest(pionek, 1)  # tu daje pionek na start

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                elif player_1.pionki_stan[pionek - 1] == 2:
                    player_1.losowyRuchTest(pionek, oczka)  # tu się ruszam pionkiem

                    licznik = max_licznik - 1

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()


            elif oczka != 6:

                if player_1.pionki_stan == [1, 1, 1, 1]:
                    licznik += 1

                print("wybierz pionek (ale nie z bazy): ")

                while True:
                    pionek = player_1.wyborPionka()
                    if player_1.pionki_stan[pionek - 1] == 2:
                        player_1.losowyRuchTest(pionek, oczka)
                        break

                self.board_draw()
                for i in range(4):
                    player_1.draw(i)
                    player_2.draw(i)
                    player_3.draw(i)
                    player_4.draw(i)
                pygame.display.update()

                break

            self.board_draw()
            for i in range(4):
                player_1.draw(i)
                player_2.draw(i)
                player_3.draw(i)
                player_4.draw(i)
            pygame.display.update()

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)
        pygame.display.update()

        print("Koniec tury gracza nr. ", kolejka)
        kolejka += 1
        os.system("cls")




    elif kolejka == 2:
        print("Trwa tura gracza nr. ", kolejka)

        if player_2.pionki_stan == [1, 1, 1, 1]:
            licznik = 3

        elif (player_2.pionki_stan[0] == 2 or player_2.pionki_stan[1] == 2 or player_2.pionki_stan[2] == 2 or
              player_2.pionki_stan[3] == 2):
            licznik = 1

        while True:

            if licznik == 4:
                break

            oczka = player_2.losowanie()
            print("Kostka wylosowała: ", oczka)

            if oczka == 6:
                pionek = player_2.wyborPionka()

                if player_2.pionki_stan[pionek - 1] == 1:
                    player_2.losowyRuchTest(pionek, 1)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                elif player_2.pionki_stan[pionek - 1] == 2:
                    player_2.losowyRuchTest(pionek, oczka)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()


            elif oczka != 6:
                print("wybierz pionek (ale nie z bazy): ")

                while True:
                    pionek = player_2.wyborPionka()
                    if player_2.pionki_stan[pionek - 1] == 2:
                        player_2.losowyRuchTest(pionek, oczka)
                        break

                self.board_draw()
                for i in range(4):
                    player_1.draw(i)
                    player_2.draw(i)
                    player_3.draw(i)
                    player_4.draw(i)
                pygame.display.update()

                licznik += 1

            self.board_draw()
            for i in range(4):
                player_1.draw(i)
                player_2.draw(i)
                player_3.draw(i)
                player_4.draw(i)
            pygame.display.update()

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)
        pygame.display.update()

        print("Koniec tury gracza nr. ", kolejka)
        kolejka += 1
        os.system("cls")




    elif kolejka == 3:
        print("Trwa tura gracza nr. ", kolejka)

        if player_3.pionki_stan == [1, 1, 1, 1]:
            licznik = 3

        elif (player_3.pionki_stan[0] == 2 or player_3.pionki_stan[1] == 2 or player_3.pionki_stan[2] == 2 or
              player_3.pionki_stan[3] == 2):
            licznik = 1

        while True:

            if licznik == 4:
                break

            oczka = player_3.losowanie()
            print("Kostka wylosowała: ", oczka)

            if oczka == 6:
                pionek = player_3.wyborPionka()

                if player_3.pionki_stan[pionek - 1] == 1:
                    player_3.losowyRuchTest(pionek, 1)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                elif player_3.pionki_stan[pionek - 1] == 2:
                    player_3.losowyRuchTest(pionek, oczka)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()


            elif oczka != 6:
                print("wybierz pionek (ale nie z bazy): ")

                while True:
                    pionek = player_3.wyborPionka()
                    if player_3.pionki_stan[pionek - 1] == 2:
                        player_3.losowyRuchTest(pionek, oczka)
                        break

                self.board_draw()
                for i in range(4):
                    player_1.draw(i)
                    player_2.draw(i)
                    player_3.draw(i)
                    player_4.draw(i)
                pygame.display.update()

                licznik += 1

            self.board_draw()
            for i in range(4):
                player_1.draw(i)
                player_2.draw(i)
                player_3.draw(i)
                player_4.draw(i)
            pygame.display.update()

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)
        pygame.display.update()

        print("Koniec tury gracza nr. ", kolejka)
        kolejka += 1
        os.system("cls")





    elif kolejka == 4:
        print("Trwa tura gracza nr. ", kolejka)

        if player_4.pionki_stan == [1, 1, 1, 1]:
            licznik = 3

        elif (player_4.pionki_stan[0] == 2 or player_4.pionki_stan[1] == 2 or player_4.pionki_stan[2] == 2 or
              player_4.pionki_stan[3] == 2):
            licznik = 1

        while True:

            if licznik == 4:
                break

            oczka = player_4.losowanie()
            print("Kostka wylosowała: ", oczka)

            if oczka == 6:
                pionek = player_4.wyborPionka()

                if player_4.pionki_stan[pionek - 1] == 1:
                    player_4.losowyRuchTest(pionek, 1)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()

                elif player_4.pionki_stan[pionek - 1] == 2:
                    player_4.losowyRuchTest(pionek, oczka)

                    self.board_draw()
                    for i in range(4):
                        player_1.draw(i)
                        player_2.draw(i)
                        player_3.draw(i)
                        player_4.draw(i)
                    pygame.display.update()


            elif oczka != 6:
                print("wybierz pionek (ale nie z bazy): ")

                while True:
                    pionek = player_4.wyborPionka()
                    if player_4.pionki_stan[pionek - 1] == 2:
                        player_4.losowyRuchTest(pionek, oczka)
                        break

                self.board_draw()
                for i in range(4):
                    player_1.draw(i)
                    player_2.draw(i)
                    player_3.draw(i)
                    player_4.draw(i)
                pygame.display.update()

                licznik += 1

            self.board_draw()
            for i in range(4):
                player_1.draw(i)
                player_2.draw(i)
                player_3.draw(i)
                player_4.draw(i)
            pygame.display.update()

        self.board_draw()
        for i in range(4):
            player_1.draw(i)
            player_2.draw(i)
            player_3.draw(i)
            player_4.draw(i)
        pygame.display.update()

        print("Koniec tury gracza nr. ", kolejka)

        kolejka = 1