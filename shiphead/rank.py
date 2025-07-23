"""
Defines the Rank class
- Populates RANK_DATA list
- Populates RANK_NAMES list

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from dataclasses import dataclass

# < ========================================================
# < Rank Class
# < ========================================================

@dataclass
class Rank:
    name: str
    long_title: str
    long_upper: str
    short_lower: str
    short_upper: str
    number_string: str
    order: int
    importance: int
    special: bool
    description: str

# < ========================================================
# < Rank Data Dictionary
# < ========================================================

RANK_DATA: dict[str, Rank] = {
    '2': Rank(
        name = '2',
        long_title = 'Two',
        long_upper = 'TWO',
        short_lower = '2',
        short_upper = '2',
        number_string = '2',
        order = 0,
        importance = 11,
        special = True,
        description = "Special card, it plays on most cards and resets pile value to 2"
    ),
    '3': Rank(
        name = '3',
        long_title = 'Three',
        long_upper = 'THREE',
        short_lower = '3',
        short_upper = '3',
        number_string = '3',
        order = 1,
        importance = 0,
        special = False,
        description = "Regular card, it has the lowest value in the game"
    ),
    '4': Rank(
        name = '4',
        long_title = 'Four',
        long_upper = 'FOUR',
        short_lower = '4',
        short_upper = '4',
        number_string = '4',
        order = 2,
        importance = 1,
        special = False,
        description = "Regular card, it has next to no value"
    ),
    '5': Rank(
        name = '5',
        long_title = 'Five',
        long_upper = 'FIVE',
        short_lower = '5',
        short_upper = '5',
        number_string = '5',
        order = 3,
        importance = 2,
        special = False,
        description = "Regular card, it has very little value"
    ),
    '6': Rank(
        name = '6',
        long_title = 'Six',
        long_upper = 'SIX',
        short_lower = '6',
        short_upper = '6',
        number_string = '6',
        order = 4,
        importance = 3,
        special = False,
        description = "Regular card, it has a little value"
    ),
    '7': Rank(
        name = '7',
        long_title = 'Seven',
        long_upper = 'SEVEN',
        short_lower = '7',
        short_upper = '7',
        number_string = '7',
        order = 5,
        importance = 10,
        special = True,
        description = "Special card, it plays on most cards and keeps the value beneath it active"
    ),
    '8': Rank(
        name = '8',
        long_title = 'Eight',
        long_upper = 'EIGHT',
        short_lower = '8',
        short_upper = '8',
        number_string = '8',
        order = 6,
        importance = 4,
        special = True,
        description = "Special card, it plays as its value but requires opponents to play an 8, or wait"
    ),
    '9': Rank(
        name = '9',
        long_title = 'Nine',
        long_upper = 'NINE',
        short_lower = '9',
        short_upper = '9',
        number_string = '9',
        order = 7,
        importance = 5,
        special = True,
        description = "Special card, it plays as its value but requires opponents to play a card equal to or lower than it"
    ),
    '10': Rank(
        name = '10',
        long_title = 'Ten',
        long_upper = 'TEN',
        short_lower = 't',
        short_upper = 'T',
        number_string = '10',
        order = 8,
        importance = 12,
        special = True,
        description = "Special card, it plays on most cards and burns the pile and gives the player another turn"
    ),
    'jack': Rank(
        name = 'jack',
        long_title = 'Jack',
        long_upper = 'JACK',
        short_lower = 'j',
        short_upper = 'J',
        number_string = '11',
        order = 9,
        importance = 6,
        special = False,
        description = "Regular card, it has a decent value"
    ),
    'queen': Rank(
        name = 'queen',
        long_title = 'Queen',
        long_upper = 'QUEEN',
        short_lower = 'q',
        short_upper = 'Q',
        number_string = '12',
        order = 10,
        importance = 7,
        special = False,
        description = "Regular card, it has a high value"
    ),
    'king': Rank(
        name = 'king',
        long_title = 'King',
        long_upper = 'KING',
        short_lower = 'k',
        short_upper = 'K',
        number_string = '13',
        order = 11,
        importance = 8,
        special = False,
        description = "Regular card, it has a very high value"
    ),
    'ace': Rank(
        name = 'ace',
        long_title = 'Ace',
        long_upper = 'ACE',
        short_lower = 'a',
        short_upper = 'A',
        number_string = '14',
        order = 12,
        importance = 9,
        special = False,
        description = "Regular card, it has the highest value in the game"
    )
}

# < ========================================================
# < Rank Names List
# < ========================================================

RANK_NAMES: list[str] = list(RANK_DATA.keys())