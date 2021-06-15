from random import choice
from itertools import islice

password_list = []
used_letters = []
lifes = 7
num = 0


def password_creator():
    print("Wpisz 3 proponowane hasła: ")
    for i in range(0, 3):
        password_list.append(input("-").upper())
    return password_creator


def password_select():
    password_creator()
    password_random = choice(password_list)
    return password_random


password = list(password_select())


def hide_password():
    output = ''
    for letter in password:
        if letter in used_letters:
            output += letter
        else:
            output += "_"
    return output


def illustration():
    global num
    with open('illustration', "r") as text_file:
        for line in islice(text_file, num, num + 7):
            print(line)
        num += 8


def life_subtract(Input):
    global lifes
    if Input[0] not in password:
        illustration()
        lifes -= 1
        print("Brak takiej litery")
        print(F"Pozostałe życie: {lifes}")


def found_repetition(Input):
    if used_letters.count(Input[0]) > 1:
        used_letters.remove(Input[0])
        print('\nPodano już taką litere!')
    else:
        life_subtract(Input)


def game_status():
    if lifes == 0:
        print()
        print("Koniec gry")
        quit()

    elif '_' not in hide_password():
        print()
        print('Wygrana!')
        quit()


def print_data():
    print("=" * 20)
    print(F"\nOdgadnięte słowo: {hide_password()}")
    print(F"Zastosowane litery:{used_letters}")


def main_loop():
    hide_password()
    while True:
        print_data()
        Input = input('Wprowadz wartość: ').upper()
        used_letters.append(Input[0])
        found_repetition(Input)
        game_status()


main_loop()
