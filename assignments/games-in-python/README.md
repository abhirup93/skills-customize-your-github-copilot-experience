# 📘 Assignment: Hangman Game

## 🎯 Objective

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Initialize the game by selecting a random word from a predefined list and setting up the game state to track the player's progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Initialize a display format showing underscores (_ _ _ _) for each letter
- Track the number of incorrect guesses remaining
- Set up tracking for letters already guessed


### 🛠️ Letter Guessing and Progress Display

#### Description
Implement the core game loop that accepts letter guesses from the player, validates input, and updates the game display with correct guesses.

#### Requirements
Completed program should:

- Accept letter input from the player
- Check if the guessed letter is in the hidden word
- Update the display to show correctly guessed letters in their positions
- Track guessed letters to prevent duplicate entries
- Display the current progress in underscores and letters format (e.g., `_ _ p l e`)


### 🛠️ Game End Conditions

#### Description
Implement logic to determine when the game ends with either a win or loss, and display appropriate messages.

#### Requirements
Completed program should:

- End the game when the player guesses the complete word (win condition)
- End the game when the player runs out of incorrect guesses (lose condition)
- Display a winning message when the word is correctly guessed
- Display a losing message and reveal the word when attempts are exhausted
- Show the final game state before ending
