def key_check():
    while True:
        event = pygame.event.wait()
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4)) or event.type == pygame.QUIT:
            break
    if event.type == pygame.QUIT:
        print("Wyjście")
        sys.exit(0)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("Wyjście")
            sys.exit(0)
        elif event.key == pygame.K_1:
            print("klawisz_1")
        elif event.key == pygame.K_2:
            print("klawisz_2")
        elif event.key == pygame.K_3:
            print("klawisz_3")
        elif event.key == pygame.K_4:
            print("klawisz_4")
        else:
            print("klawisz_inny")
    else:
        print("inna akcja")