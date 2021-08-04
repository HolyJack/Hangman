import random

print("H A N G M A N")


def hangman_game():
    words_list = ("python", "java", "kotlin", "javascript")
    choice = random.choice(words_list)
    guessed = list("-" * len(choice))
    guesses = set()
    letters = set(choice)
    tries = 8
    while tries > 0:
        print()
        print("".join(guessed))
        c = input("Input a letter:")
        if len(c) != 1:
            print("You should input a single letter")
        elif not c.isascii() or not c.islower():
            print("Please enter a lowercase English letter")
        elif c in letters:
            guesses.add(c)
            letters.remove(c)
            for i in range(len(choice)):
                if choice[i] == c:
                    guessed[i] = c
        elif c in guesses:
            print("You've already guessed this letter")
        else:
            guesses.add(c)
            tries -= 1
            print("That letter doesn't appear in the word")
        if "".join(guessed) == choice:
            print()
            print(choice)
            print("You guessed the word!")
            print("You survived!")
            exit(0)
    print("You lost!")


answer = input("""Type "play" to play the game, "exit" to quit:""")
while answer == "play":
    hangman_game()
    answer = input("""Type "play" to play the game, "exit" to quit:""")
