"""
Defines the Card class

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from typing import (
    ClassVar
)

# < ========================================================
# < Package Imports
# < ========================================================

from . import settings
from .rank import RANK_DATA
from .suit import SUIT_DATA

# < ========================================================
# < Card Class
# < ========================================================

class Card:

    counter: ClassVar[int] = 0

    def __init__(self, rank: str, suit: str = 'hearts') -> None:
        """Create a card instance"""

        self.rank: str = rank
        self.suit: str = suit
        self.uid: int = Card.counter
        self.order: int = RANK_DATA[rank].order
        self.importance: int = RANK_DATA[rank].importance
        Card.counter += 1

    def __repr__(self) -> str:
        """String representation of a card"""
        
        rank: str = getattr(RANK_DATA[self.rank], settings.rank_style)
        suit: str = getattr(SUIT_DATA[self.suit], settings.suit_style)
        return f"{rank}{settings.separator}{suit}"