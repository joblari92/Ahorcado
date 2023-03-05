import random

print("Comienza el juego del ahorcado!\n")

words = ["cueva","perro","arquitectura","plumero","cachalote","camello"]

game_word = list(words[random.randint(0,len(words)-1)])

print(game_word)

lives = 7

letters = []

for letter in game_word:
    letters.append("_")



while lives != 0:

    print(letters)

    user_letter = input("Introduce una letra: ").lower()

    print(user_letter)

    count = 0
    position = 0
    count_spaces = 0

    for letter in letters:
        if user_letter == game_word[position]:
            count+=1
            letters[position] = user_letter
        position += 1


    if count > 0:
        print("Letra correcta!")
    else:
        lives -= 1
        print(f"Te quedan {lives} vidas.")

    for letter in letters:
        if letter == "_":
            count_spaces+=1

    if count_spaces == 0:
        break


if lives == 0:
    print("Has perdido!")
else:
    print("Victoria!")