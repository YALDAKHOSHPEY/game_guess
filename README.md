# 🎯 Advanced Guess the Number - Python Game

A feature-rich number guessing game written in Python. Includes difficulty levels, attempt limits, a timer, and high score tracking! 🏆

---

## 📜 Description

The computer randomly selects a number between **1 and 100**.  
You must guess the number in the **fewest attempts** possible and beat the **high score**.

Features:
- 🌟 Difficulty modes: Easy, Medium, Hard
- ⏱️ Timer to measure how fast you win
- ❌ Limited attempts on Medium/Hard
- 🏅 High score tracking (saved to file)

---

## 🛠️ Tech Stack

- Python 3.x
- No external libraries needed

---

## ▶️ How to Run

1. Ensure you have Python 3 installed.
2. Save the game as `guess_number.py`
3. Create a blank file named `highscore.txt` in the same directory.
4. Run the game:

```bash
python guess_number.py
🎯 Welcome to the Advanced 'Guess the Number' Game!
Choose difficulty:
1 - Easy (Unlimited attempts)
2 - Medium (10 attempts)
3 - Hard (5 attempts)
Enter 1, 2, or 3: 2
I'm thinking of a number between 1 and 100...

Enter your guess: 50
🔽 Too low!
Enter your guess: 75
🔼 Too high!
Enter your guess: 62
🎉 Congratulations! You guessed the number in 3 attempts and 12.5 seconds.
🏆 New High Score! Well done!
