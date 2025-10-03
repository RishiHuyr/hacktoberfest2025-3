import random

WORDS = ["python", "flask", "github", "hacktoberfest", "developer"]

def play():
    word = random.choice(WORDS)
    guessed = ["_"] * len(word)
    tries = 6
    used = set()

    while tries > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        print(f"Tries left: {tries}, Used: {', '.join(used)}")
        guess = input("Guess a letter: ").lower()

        if guess in used:
            print("Already guessed.")
            continue
        used.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print("You win! Word was:", word)
    else:
        print("You lose! Word was:", word)

if __name__ == "__main__":
    play()
