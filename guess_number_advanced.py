import random
import time
import os

def get_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return None

def set_highscore(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def choose_difficulty():
    print("Choose difficulty:")
    print("1 - Easy (Unlimited attempts)")
    print("2 - Medium (10 attempts)")
    print("3 - Hard (5 attempts)")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        return "easy", None
    elif choice == "2":
        return "medium", 10
    elif choice == "3":
        return "hard", 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        return "medium", 10

def play_game():
    print("🎯 Welcome to the Advanced 'Guess the Number' Game!")
    print("I'm thinking of a number between 1 and 100... 🤔")

    difficulty, max_attempts = choose_difficulty()
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("🔽 Too low!")
            elif guess > number:
                print("🔼 Too high!")
            else:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts and {total_time} seconds.")

                highscore = get_highscore()
                if highscore is None or attempts < highscore:
                    print("🏆 New High Score! Well done!")
                    set_highscore(attempts)
                else:
                    print(f"⭐ Current High Score: {highscore} attempts")

                break

            if max_attempts is not None and attempts >= max_attempts:
                print(f"\n💥 Game Over! You've used all {max_attempts} attempts. The number was {number}.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    play_game()
