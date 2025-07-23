# Overview
This project is a new and improved version of my previous `Python` game project, `shiphead`. The game `Shiphead` was a playing card game from my childhood, which often goes by a less family-friendly [name](https://en.wikipedia.org/wiki/Shithead_(card_game)).

The previous version of this project used [Pygame](https://www.pygame.org/wiki/about) to create a `GUI` layer for the game. In creating the `GUI` layer, some of the game logic became entangled with the `GUI` logic and the project became quite hard to maintain. This version aims to create the game purely for a `CLI`. This has meant that the game logic is much more maintainable.

To attempt to create compatibility with future iterations, a directed effort has been made to define a `snapshot` object for each player turn, containing the game state, and available decisions. I hope that in future this version will form the base logic of future iterations, possibly with a `GUI` layer, or even be used to train a computer player via [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)

# Installing the Game
> [!TIP]
> Before starting, ensure your system `PATH` is correctly configured and ensure that `git` and `python` are installed. The steps below are for for `Windows`, using `Command Prompt`. The game should be installable via any shell and on any system that runs `Python` so you may need to adapt the steps for your system!

## Cloning this Repository
Open your terminal and navigate to the location where you want a clone of this repository to be created
- Clone the repository to your system
    - `git clone https://github.com/scarletti-ben/shiphead-py`

## Creating the Virtual Environment and Installing Dependencies
The steps below are used to set up a virtual environment with the correct dependencies for the game, and separate it from your global `Python` installation
- Change directory into the `shiphead-py` directory
    - `cd shiphead-py`
- Create the virtual environment within the directory
    - `python -m venv venv`
- Activate the virtual environment
    -  `.\venv\Scripts\activate`
- Install dependencies defined in `requirements.txt`
    - `pip install -r requirements.txt`

> [!NOTE]
> You will need to activate the virtual environment again, via `.\venv\Scripts\activate`, if you leave the virtual environment and come back

# Playing the Game
Assuming the [install](#installing-the-game) steps were successful and you are in the virtual environment then you can run `python -m shiphead` to start the game. This will run the entry point script of the package, `__main__.py`

# Game Controls
The game is a simple `CLI` and, by default, should start you in a game against a computer-controlled player. 

Each turn you should be presented with a simple list of choices, as seen below, and can make your decision by typing in a valid number and pressing the `Enter` key
```text
------------------------------
>>> Decision
------------------------------
Available: [A·♠, T·♣]
Center: [8·♠, Q·♠, Q·♣, K·♦, K·♠]
[0] take
[1] play [A·♠]
[2] play [T·♣]
Selection [0 - 2]:
```

# Game Rules
The rules for `shiphead`, as well as the name, vary quite significantly between different people. The rules I have been playing for a while now are built into this version, and are defined below. I am sure there are better ways to write the rules for a beginner, but these rules are mainly aimed as a refresher for people who have played before

The general premise of the game is to get rid of all of your cards by playing them onto a central pile. To play a card, or set of cards, you will need to follow the [rules](#rule-list) for playing a card . You will also notice that you have two other piles, other than your hand, that you will also need to get rid of!

## Rule List
- On your turn you can decide to play any number of a single rank of card that is playable, see [card reference guide](#card-reference-guide)
- If you cannot play, and there is not a special rule in play such as "eight-or-wait", then you must pick up the central pile and end your turn
- You may also decide to pick up the center pile voluntarily, which you may wish to do for tactical reasons. This assumes that there are cards to pickup and that there is not a special rule in play such as "eight-or-wait"
- If you played cards from your hand and there is still a deck left to pick up from, then you must re-fill your hand back to 5 cards
- Once you have finished your turn, the game moves onto the next player
- If, on your turn, you complete a "four-in-a-row", where there are four of a single card rank in a row on top of the pile, the pile is burned and you take another turn
- If, on your turn, you play a `10`, the pile is burned and you take another turn
- If, at the start of your turn, there is an `7` on top of the pile you must follow the rule "invisible-sevens"
- If, at the start of your turn, there is an `8` on top of the pile you must follow the rule "eight-or-wait"
    - If the `8` has already been "waited" then the "eight-or-wait" rule no longer applies
- If, at the start of your turn, there is an `9` on top of the pile you must follow the rule "nine-or-lower"
    - If the `9` has had a `7` played on top of it then the "nine-or-lower" rule no longer applies
- Once you run out of cards in hand you play from your cards in your "shown" pile
    - If you pick up cards they still go to hand, and you will need to empty your hand again to use "shown" cards
    - You cannot combine the last cards in your hand with cards within your "shown" pile eg. a `2` in hand and `2` from "shown"
- Once you run out of cards in your hand and "shown" pile you can play from your "hidden" pile
    - You will play exactly one card from your "hidden" pile on your turn
    - You play the card entirely blind, if the card was not playable then you pick up the central pile and end your turn

## Card Reference Guide
The `[ ]` and `< >` symbols are symbols to denote different states for cards on top of the pile. `[ ]` denotes that the default state applies, and `< >` suggests a "deactivated" state for the card. Some examples are listed below
- An `[8]` is a "normal" `8` that has just been played, and requires the player to follow the "eight-or-wait" rule, whereas an `<8>` has already been "waited" and the "eight-or-wait" rule no longer applies to it
- A `[9]` is a "normal" `9` that has just been played, and requires the player to follow the "nine-or-lower" rule, whereas a `<9>` has had a `7` played on top and the "nine-or-lower" rule no longer applies to it
```text
# What Can be Played on a...
    [2]   => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [3]   => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [4]   => 2, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [5]   => 2, 5, 6, 7, 8, 9, 10, J, Q, K, A
    [6]   => 2, 6, 7, 8, 9, 10, J, Q, K, A
    [7]   => Look at the number on the pile before the 7
    [8]   => 8
    <8>   => 2, 7, 8, 9, 10, J, Q, K, A
    [9]   => 2, 3, 4, 5, 6, 7, 8, 9
    <9>   => 2, 7, 9, 10, J, Q, K, A
    [10]  => Clears the pile, should never be face up on the pile
    [J]   => 2, 7, 10, J, Q, K, A
    [Q]   => 2, 7, 10, Q, K, A
    [K]   => 2, 7, 10, K, A
    [A]   => 2, 7, 10, A

# What Can it Play On?
    2   => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
    3   => 2, 3, 9
    4   => 2, 3, 4, 9
    5   => 2, 3, 4, 5, 9
    6   => 2, 3, 4, 5, 6, 9
    7   => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
    8   => 2, 3, 4, 5, 6, 8, <8>, 9
    9   => 2, 3, 4, 5, 6, <8>, 9, <9>
    10  => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
    J   => 2, 3, 4, 5, 6, <8>, <9>, J
    Q   => 2, 3, 4, 5, 6, <8>, <9>, J, Q
    K   => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K
    A   => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
```

# Project Structure
The general structure of this project / repository is outlined below. It is subject to change, and may not reflect the exact structure of the project. It is mainly to give an idea of where the important files should be. For the average user the only files that really matter, once the project is [installed](#installing-the-game), reside within the `shiphead` directory.

```text
shiphead-py/
│
├── shiphead
│   ├── __init__.py
│   ├── __main__.py
│   ├── card.py
│   ├── core.py
│   ├── lookups.py
│   ├── player.py
│   ├── rank.py
│   ├── settings.py
│   ├── snapshot.py
│   ├── suit.py
│   └── utils.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

# Miscellaneous
- The computer player is not especially adept and will often make sub-par decisions

# Project Metadata
```yaml
---
title: "shiphead-py"
date: "2025-07-01"
last_modified_at: "2025-07-23"
description: "Streamlined version of my previous Python-based game project, shiphead"
categories: [
  miscellaneous
]
tags: [
  coding, dev, gamedev, game development, python, python packages, venv, virtual environment, cli, command line interface, terminal, command prompt, gaming, card game, playing cards, shiphead
]
---
```