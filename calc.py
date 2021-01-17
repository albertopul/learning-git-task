i = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
x = int(input("Podaj składnik 1. "))
y = int(input("Podaj składnik 2. "))


def make_calculation(i,x,y):
    if i == 1:
        print(f"Dodaję", (x), "i", (y))
        wynik = x + y
        print(f"Wynik to {wynik}")
    elif i == 2:
        print(f"Odejmuję", (y), "od", (x))
        wynik = (x) - (y)
        print(f"Wynik to {wynik}")
    elif i == 3:
        print(f"Mnożę", (x), "i", (y))
        wynik = (x) * (y)
        print(f"Wynik to {wynik}")
    elif i == 4:
        if y == 0:
            print("Nie dzieli się przez zero!")
        elif y != 0:
            print(f"Dzielę", (x), "przez", (y))
            wynik = (x) / (y)
            print(f"Wynik to {wynik}")

make_calculation(i,x,y)