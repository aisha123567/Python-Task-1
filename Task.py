import random

words = ['Apple', 'Orange', 'Cherry', 'Banana', 'Grapes']
word = random.choice(words).lower()
guessed = ['_'] * len(word)
wrong = 0
guessed_letters = set()

while wrong < 6 and '_' in guessed:
    print(' '.join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter. Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, l in enumerate(word):
            if l == guess:
                guessed[i] = guess
    else:
        wrong += 1
        print(f"Wrong guesses left: {6 - wrong}")

print("You won!" if '_' not in guessed else f"You lost! The word was {word}")