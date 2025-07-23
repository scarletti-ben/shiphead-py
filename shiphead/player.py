"""
Defines the Player class

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from __future__ import annotations
from typing import (
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from .card import Card

# < ========================================================
# < Player Class
# < ========================================================

class Player:
    def __init__(self, name: str, human: bool, uid: int, ) -> None:
        """Create a Player instance"""

        self.name: str = name
        self.human: bool = human
        self.uid: int = uid
        self.hand: list[Card] = []
        self.shown: list[Card] = []
        self.hidden: list[Card] = []
        self.piles: dict[str, list[Card]] = {
            'hand': self.hand,
            'shown': self.shown,
            'hidden': self.hidden
        }

    def pile_name(self, pile: list[Card]) -> str:
        """Get pile name reference for a given pile"""

        for name, value in self.piles.items():
            if value is pile:
                return name
        raise ValueError('Unknown pile')

    @property
    def cards(self) -> list[Card]:
        """Get a list of all cards owned by the player"""
        return self.hand + self.shown + self.hidden
    
    def assessment(self) -> str:
        """Get string assessment of player card piles"""

        x = lambda pile: str(len(pile)).zfill(2)
        y = lambda pile: ', '.join(map(str, pile)) or ''
        return (
            f"Player {self.uid} [{self.name}] [{'Human' if self.human else 'Computer'}]\n"
            f"    Hand       ({x(self.hand)}): [{y(self.hand)}]\n"
            f"    Shown      ({x(self.shown)}): [{y(self.shown)}]\n"
            f"    Hidden     ({x(self.hidden)}): [{y(self.hidden)}]\n"
            f"    Total      ({x(self.cards)}): [{y(self.cards)}]\n"
        )

    @property
    def accessible(self) -> list[Card]:
        """Get the list of cards the player can access"""

        if self.hand:
            return self.hand
        elif self.shown:
            return self.shown
        elif self.hidden:
            return self.hidden
        else:
            return []
        
    @property
    def current_pile(self) -> list[Card]:
        """Get the current pile of cards the player can access"""
        
        if self.hand:
            return self.hand
        elif self.shown:
            return self.shown
        elif self.hidden:
            return self.hidden
        else:
            return []
        
    def winning(self) -> bool:
        """Check to see if this player is winning or has won"""
        return not self.current_pile
        
    def __repr__(self) -> str:
        """String representation of a player"""
        return f"P{self.uid} [{self.name}]"