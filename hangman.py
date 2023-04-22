import random

wordBank = ["tofu", "moon", "computer", "wifi", "octopus"]
word = random.choice(wordBank)
size = len(word)
wordArray = list(word)
counter = 0
wordOut = ["_"] * size

while counter < 5:
    letter = input("choose a letter: ")
    if letter in wordArray:
        for i in range(size):
            if wordArray[i] == letter:
                wordOut[i] = letter
        print(" ".join(wordOut))
        if "_" not in wordOut:
            print("You win!")
            break
    else:
        print("Wrong letter, try again.", " ".join(wordOut))
        counter += 1
else:
    print("You lose. The word was", word)