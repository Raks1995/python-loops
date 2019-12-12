print("Hello, this program converts kilometers into miles.")


while True:
    km = int(input("Kilometers: "))
    mi = 1.6 * km
    print("Miles: " + str(mi))
    pitanje = input("Wanna try again? (yes/no): ")
    if pitanje.lower() == "no":
        break
    elif pitanje.lower() == "yes":
        print("Ok. Here you go!")
    else:
        print("Can't recognize this input.")
        break





