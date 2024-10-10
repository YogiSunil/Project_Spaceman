# Spaceman Guessing Game

## Introduction
The Spaceman game is a word guessing game where the player tries to guess a secret word, one letter at a time. The player has 7 incorrect guesses before the game ends. For each incorrect guess, a part of the spaceman is drawn. If the player guesses the word before running out of attempts, they win. If not, the game ends with a complete drawing of the spaceman.

## How to Play

1. **Start the Game**:  
   Run the Python program. The game will load a random secret word from a file called `words.txt`.

2. **Game Flow**:  
   - The game will display how many letters are in the secret word.
   - You have 7 incorrect guesses to figure out the word.
   - For each turn, you will be asked to guess a letter.
   - If the letter is in the word, it will be revealed in its correct position(s).
   - If the letter is not in the word, the spaceman drawing will start to appear, and you will lose one of your 7 incorrect guesses.
   - The game will display the partially guessed word and show underscores (`_`) for letters that haven't been guessed yet.

3. **Winning the Game**:  
   - If you correctly guess all the letters in the word before running out of attempts, you win! The game will display a congratulatory message.

4. **Losing the Game**:  
   - If you use up all 7 incorrect guesses, the full spaceman drawing will appear, and the game will display a message indicating that you lost, along with the correct word.

5. **Playing Again**:  
   - After each game, you will be asked if you want to play again. If you enter `yes`, the game will restart with a new secret word. If you enter `no`, the game will end.

## Input
- You need to enter one letter per turn.
- Only alphabetic characters are accepted.
- If you try to guess the same letter more than once, or input an invalid character, you will be prompted to try again without losing a turn.

## Files
- `spaceman.py`: The main Python program that runs the game.
- `words.txt`: A text file that contains the list of possible secret words. Each word is separated by a space (or you can update the file to have one word per line and modify the code accordingly).

## Sample Output

```
Welcome to Spaceman!
The secret word contains 5 letters.

You have 7 incorrect guesses left.
Current word: _ _ _ _ _

Please guess a letter: a
Oops! a is not in the word.

You have 6 incorrect guesses left.
Current word: _ _ _ _ _
```

## Requirements
- Python 3.x
- `words.txt` file with words for the game

## Running the Game
1. Make sure you have `spaceman.py` and `words.txt` in the same directory.
2. Run the Python program using the command:
   ```
   python spaceman.py
   ```

Enjoy the game, and good luck guessing the secret word before the spaceman is fully drawn!
