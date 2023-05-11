import random


def generate_number():
    return random.randint(1, 100)


def restart():
    user_answer = input("You want to try again?y/n")
    if user_answer == "y":
        return start()
    elif user_answer == "n":
        return start()
    else:
        print("Didnt understand, try again")
        restart()


def start():
    print("Welcome to the Number Guessing Game!\nI`m thinknig of a number between 1 and 100")
    user_choice_diff = input("Chose a difficulty. Type 'easy' or 'hard'")
    attempts = 0
    if user_choice_diff == "easy":
        attempts = 10
    elif user_choice_diff == "hard":
        attempts = 5
    else:
        print("Didnt understand, try again")
        start()
    answer = generate_number()
    while attempts > 0:
        print(f"You have {attempts} attempts to guess number\n")
        user_answer = int(input("Make a guess: "))
        if user_answer > answer:
            print("\nToo high\nGuess again")
            attempts -= 1
        elif user_answer < answer:
            print("\nToo low\nGuess again")
            attempts -= 1
        elif user_answer == answer:
            print(f"\nYou win\nNumber is:{answer}")
            restart()
        if attempts == 0:
            print(f"Game Over, the number is {answer}")
            restart()



def main():
    start()


if __name__ == '__main__':
    main()
