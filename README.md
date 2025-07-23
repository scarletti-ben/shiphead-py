# Overview
This project is a new and improved version of my previous `Python`-based game project, `shiphead`. The game "Shiphead" was a playing card game from my childhood, which often goes by a less family-friendly [name](https://en.wikipedia.org/wiki/Shithead_(card_game))

The previous version of this project used [Pygame](https://www.pygame.org/wiki/about) to create a `GUI` layer for the game. In creating the `GUI` layer, some of the game logic became entangled with the `GUI` logic and the project became quite hard to maintain. This version aims to create the game purely for a `CLI`. This has meant that the game logic is much more maintainable

I hope that in future this version will form the base logic of future iterations, possibly with a `GUI` layer, or even be used to train a computer player via `reinforcement learning` (`RL`). To attempt to create compatibility with future iterations, a directed effort has been made to define a `snapshot` object for each player turn, containing the game state, and available decisions

# Installing the Game
Before starting, ensure your system `PATH` is correctly configured and ensure that `git` and `python` are installed. The steps below are for for `Windows`, using `Command Prompt`. The game should be installable via any shell and on any system that runs `Python` so you may need to adapt the steps for your system!

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
Assuming the [install](#installing-the-game) steps were successful and you are in the virtual environment then you can run `python -m shiphead` to start the game

## Game Controls
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

## Game Rules [WIP]

The rule "8 or wait" means that if an 8 is on the pile you can either play an 8 or you must wait, if you wait then you skip your turn, but do not pick up the pile, and the player that played the 8 plays again, but now the 8 is disabled, effectively the waiting has disabled the 8's power

The rule "9 or lower" means that if a 9 is on the pile you must play a card that is lower than it, and once you do, play returns to normal, this also means that if you play a 7 on a 9, the next card will not have to play lower than a 9, effectively the 7 has disabled the 9's power

2s essentially reset the table and play on most
7s are invisible and keep the value of the card beneath then, and play on most
8s start "8 or wait" which is described above
9s start "9 or lower" and are described above
10s clear the table and play on mose

Suits do not matter

Four of a kind burns the deck


Ignoring most of the "why" of each rule, a simple reference of what can be played on what is below. This should be handled by the game logic without you having to remember it all!

- The AI is not especially adept and will make sub-par decisions

```text
# What Can be Played on a...
-  [2]  => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
-  [3]  => 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
-  [4]  => 2, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
-  [5]  => 2, 5, 6, 7, 8, 9, 10, J, Q, K, A
-  [6]  => 2, 6, 7, 8, 9, 10, J, Q, K, A
-  [7]  => Look at the number on the pile before the 7
-  [8]  => 8
-  <8>  => 2, 7, 8, 9, 10, J, Q, K, A
-  [9]  => 2, 3, 4, 5, 6, 7, 8, 9
-  <9>  => 2, 7, 9, 10, J, Q, K, A
- [10]  => Clears the pile, should never be face up on the pile
-  [J]  => 2, 7, 10, J, Q, K, A
-  [Q]  => 2, 7, 10, Q, K, A
-  [K]  => 2, 7, 10, K, A
-  [A]  => 2, 7, 10, A
```

# What Can it Play On?
```text
-  2  => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
-  3  => 2, 3, 9
-  4  => 2, 3, 4, 9
-  5  => 2, 3, 4, 5, 9
-  6  => 2, 3, 4, 5, 6, 9
-  7  => 2, 3, 4, 5, 6, <8>, 9, <9>, J, Q, K, A
-  8  => 2, 3, 4, 5, 6, 8, <8>, 9
-  9  => 2, 3, 4, 5, 6, <8>, 9, <9>
- 10  => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
-  J  => 2, 3, 4, 5, 6, <8>, <9>, J
-  Q  => 2, 3, 4, 5, 6, <8>, <9>, J, Q
-  K  => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K
-  A  => 2, 3, 4, 5, 6, <8>, <9>, J, Q, K, A
```

# Project Structure

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

Currently the repository structure means that there is a `Python` package named `shiphead` accessible from the project root

# Project Metadata
```yaml
---
title: "shiphead-py"
date: "2025-07-01"
last_modified_at: "2025-07-23"
description: "Streamlined version of my previous Python-based game project, shiphead. The game "Shiphead" was a playing card game from my childhood"
categories: [
  miscellaneous
]
tags: [
  coding, dev, gamedev, game development, python, python packages, venv, virtual environment, cli, command line interface, terminal, command prompt, gaming, card game, playing cards, shiphead
]
---
```