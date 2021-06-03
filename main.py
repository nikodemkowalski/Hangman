#GRA W WISIELCA
import random
used_letters = []
user_word = []

word_tupla = []
word_tupla.append(input("Dodaj słowo [1/3]: "))
word_tupla.append(input("Dodaj słowo [2/3]: "))
word_tupla.append(input("Dodaj słowo [3/3]: "))
word_random = random.choice(word_tupla)
word = list(word_random.upper())


def indexes(word, user_input):
    index = []
    for i, letter_in_word in enumerate(word):
        if user_input.upper() == letter_in_word:
            index.append(i)
    return index

def print_output():
    connected_input = "".join(user_word)
    data = "Odgadnięte słowo: {0}\nZastosowane litery:{1}".format(connected_input, used_letters)
    print(data)

def hidden():
    result = (len(word) * " _ ")
    for _ in word:
        user_word.append("_")


def main_loop():
    lifes = 5
    hidden()

    while lifes > 0:
        print_output()
        user_input = input("\nWpisz literę: ")
        user_input.upper()
        used_letters.append(user_input.upper()[0])
        found_indexes = indexes(word, user_input)


        if used_letters.count(user_input.upper()) > 1:
            used_letters.remove(user_input.upper())
            print("\nPodano już taką literę\n")
            continue

        if len(found_indexes) == 0:
            print("-------------\nBrak takiej litery\n-------------")
            lifes -=1
            print("Pozostałe życie: ", lifes)


            if lifes == 0:
                print("Koniec gry")
                quit()
        else:
            for index in found_indexes:
                user_word[index] = user_input.upper()

        if user_word == word:
            password = "".join(user_word)
            print(" ----------------------------\n","Odgadłeś slowo! - ", password ,"\n----------------------------")
            quit()
main_loop()
