
# Blackjack Game

A simple terminal-based Blackjack game written in Python. This game simulates a game of Blackjack where the user competes against the computer (dealer). The goal is to get as close to 21 without exceeding it. If you score exactly 21 with the first two cards, you get a **Blackjack**!

## Features

- Deals cards to the player and the computer.
- Allows the player to draw additional cards (hit) or stop (stand).
- Computer draws cards until its score reaches at least 17.
- Handles special conditions like Blackjack and exceeding 21.
- Interactive gameplay with score comparisons.

## Game Rules

- Cards are drawn from a deck with values: `[11 (Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 (Jack), 10 (Queen), 10 (King)]`.
- **Blackjack** is achieved when the player’s first two cards sum to 21.
- If the player or computer exceeds 21, they lose.
- The computer will keep drawing cards until its score reaches 17 or more.
- If both player and computer have the same score, it's a draw.

## How to Play

1. Clone this repository.
    ```bash
    git clone https://github.com/yourusername/blackjack-game.git
    ```
   
2. Navigate to the project directory.
    ```bash
    cd blackjack-game
    ```

3. Run the Python file to start the game.
    ```bash
    python blackjack.py
    ```

4. Follow the on-screen prompts to draw cards or stand.

## Code Breakdown

- **deal_card()**: Randomly draws a card from the deck.
- **calculate_score()**: Calculates the score of a hand, adjusting for the Ace's value if necessary.
- **compare()**: Compares the scores between the player and computer, determining the winner.
- **play_game()**: The main game loop, allowing the player to play against the computer.

## Requirements

- Python 3.x
- [art](https://pypi.org/project/art/) library for displaying the game logo.

You can install the required dependencies using:
```bash
pip install art
```

Feel free to customize the content as per your project and GitHub setup!
