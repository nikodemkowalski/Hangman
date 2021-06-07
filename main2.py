import random
used_letters = []
user_word = []
word_list = []
lifes = 5


def decor(func):
    def wrapp():
        print("-----------------------")
        func()
    return wrapp


def list_creator(word_list):
    print("Wpisz 3 proponowane hasła: ")
    for i in range(0, 3):
        word_list.append(input("-").upper())


def random_word(list_creator):
    list_creator(word_list)
    word_random = random.choice(word_list)
    return word_random


def letters_change(word, user_input):
    index = []
    word = enumerate(word)
    for i, letter in word:
        if user_input == letter:
            index.append(i)
    return index


@decor
def print_output():
    connected_word = "".join(user_word)
    print(F"Odgadnięte słowo: {connected_word}")
    print(F"Zastosowane litery:{used_letters}")


def hidden(word):
    len(word) * " _ "
    for _ in word:
        user_word.append("_")


def letter_replace(found_indexes, user_input):
    if len(found_indexes) != 0:
        for index in found_indexes:
            user_word[index] = user_input


def life_modulation(user_input, found_indexes):
    used_letters.append(user_input.upper()[0])
    if used_letters.count(user_input.upper()) > 1:
        used_letters.remove(user_input)
        print("\nPodano już taką literę\n")

    else:
        if len(found_indexes) == 0:
            print("\nBrak takiej litery")
            return True


def loose(lifes):
    if lifes == 0:
        print()
        print("Koniec gry")
        quit()


def win(word):
    if user_word == word:
        password = "".join(user_word)
        print("\nOdgadłeś slowo! - ", password)
        quit()


def main_loop(lifes):
    word = list(random_word(list_creator))
    hidden(word)

    while True:
        print_output()
        user_input = input("Wpisz literę: ").upper()
        found_indexes = letters_change(word, user_input)
        letter_replace(found_indexes, user_input)
        
        if life_modulation(user_input, found_indexes):
            lifes -= 1
            print("Pozostałe życie: ", lifes)
            
        loose(lifes)
        win(word)


main_loop(lifes)
