print("Lista zakupów")

zakupy_dict = {
    "piekarnia": ["chleb","pączek","bułki"],
    "warzywniak": ["marchew","seler","rukola"]
}

for sklep, produkty in zakupy_dict.items():
    print(sklep, ":", produkty)

    print(f"Idę do ",(sklep.capitalize()),"kupuję tu następujące rzeczy", (produkty))