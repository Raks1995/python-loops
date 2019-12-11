print("Hello, this program converts kilometers into miles.")


while True:
    km = int(input("Kilometers: "))
    mi = 1.6 * km
    print("Miles: " + str(mi))
    pitanje = input("Wanna try again? (yes/no): ")
    if pitanje != "yes":
        break



