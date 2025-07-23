"""
Defines the Suit class
- Populates SUIT_DATA list
- Populates SUIT_NAMES list

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from dataclasses import dataclass

# < ========================================================
# < Package Imports
# < ========================================================

from .utils import cstring

# < ========================================================
# < Suit Class
# < ========================================================

@dataclass
class Suit:
    name: str
    name_title: str
    name_upper: str
    short_lower: str
    short_upper: str
    symbol: str
    symbol_coloured: str

# < ========================================================
# < Suit Data Dictionary
# < ========================================================

SUIT_DATA: dict[str, Suit] = {
    'hearts': Suit(
        name = 'hearts',
        name_title = 'Hearts',
        name_upper = 'HEARTS',
        short_lower = 'h',
        short_upper = 'H',
        symbol = '♥',
        symbol_coloured = cstring('♥', (255, 0, 0))
    ),
    'diamonds': Suit(
        name = 'diamonds',
        name_title = 'Diamonds',
        name_upper = 'DIAMONDS',
        short_lower = 'd',
        short_upper = 'D',
        symbol = '♦',
        symbol_coloured = cstring('♦', (255, 0, 0))
    ),
    'clubs': Suit(
        name = 'clubs',
        name_title = 'Clubs',
        name_upper = 'CLUBS',
        short_lower = 'c',
        short_upper = 'C',
        symbol = '♣',
        symbol_coloured = cstring('♣', (0, 0, 255))
       
    ),
    'spades': Suit(
        name = 'spades',
        name_title = 'Spades',
        name_upper = 'SPADES',
        short_lower = 's',
        short_upper = 'S',
        symbol = '♠',
        symbol_coloured = cstring('♠', (0, 0, 255))
    )
}

# < ========================================================
# < Suit Names List
# < ========================================================

SUIT_NAMES: list[str] = list(SUIT_DATA.keys())