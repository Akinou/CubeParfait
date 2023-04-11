while True:
    try:
        n = int(input("Entrez un nombre entier positif : "))
        if n < 0:
            raise ValueError
        break
    except ValueError:
        print("Veuillez entrer un nombre entier positif.")

cube_parfait = 0
i = 1

while cube_parfait < n:
    cube_parfait = i ** 3
    if cube_parfait == n:
        print(f"{n} est un cube parfait.")
        break
    i += 1

if cube_parfait != n:
    print(f"{n} n'est pas un cube parfait.")
