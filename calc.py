import sys
import logging

i = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
x = int(input("Podaj składnik 1. "))
y = int(input("Podaj składnik 2. "))

# od tąd
def print_calc(operation):
    if operation == 1:
        logging.info(f"Dodaję", (x), "i", (y))
    elif operation == 2:
        logging.info(f"Odejmuję", (y), "od", (x))
    elif operation == 3:
        logging.info(f"Mnożę", (x), "i", (y))
    elif operation == 4:
        logging.info("Dzielę", (x), "przez", (y))

# do tąd 
# nie wiem co wyprintować (i czy) i jak

# tutaj nie mam pomysłu na użycie if __name__ == "__main__":

operators = {"1": x+y, "2": x-y, "3": x*y, "4": x/y}

if i == "1":
    print("Wynik to ", operators["1"])
elif i == "2":
    print("Wynik to ", operators["2"])
elif i == "3":
    print("Wynik to ", operators["3"])
elif i == "4":
    print("Wynik to ", operators["4"])