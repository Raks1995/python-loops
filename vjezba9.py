import random

secret = random.randint(1, 30)
broj_pokusaja = 0

while True:
    guess = int(input("Number: "))

    broj_pokusaja = broj_pokusaja + 1

    if guess == secret:
        print("You've guessed it - congratulations!")
        print("Broj pokusaja: " + str(broj_pokusaja))
        break
    elif broj_pokusaja > 10:
        print("premasio si broj pokusaja")
        break
    elif 30 < guess < 1:
        print("Neispravno")
    elif guess > secret:
        print("Probaj manji broj")
    elif guess < secret:
        print("Probaj veci broj")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

