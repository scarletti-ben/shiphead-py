"""
Defines Snapshot and Result classes

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Any,
    TypedDict
)
if TYPE_CHECKING:
    from .card import Card
    from .player import Player
    from .core import Core

# < ========================================================
# < External Imports
# < ========================================================

from dataclasses import (
    dataclass, 
    field
)
from pprint import (
    pprint,
    pformat
)

# < ========================================================
# < Result Class
# < ========================================================

@dataclass
class Result:
    option: str = ''
    cards: list[Card] = field(default_factory = list)

# ~ ========================================================
# ~ Snapshot Class
# ~ ========================================================

@dataclass
class Snapshot:
    """Snapshot of game state for the current turn"""
    turn: int
    player: Player
    human: bool
    pile: list[Card]
    pile_name: str
    hidden: bool
    center: list[Card]
    deck: list[Card]
    burned: list[Card]
    standard: bool
    actual_rank: str | None
    anchor_rank: str | None
    valid_ranks: list[str]
    playable_cards: list[Card]
    playable_combinations: list[list[Card]]
    options: list[str]
    result: Result | None = None

    @property
    def waitable(self) -> bool:
        """Check if 'wait' is in options"""
        return 'wait' in self.options

    @property
    def takeable(self) -> bool:
        """Check if 'take' is in options"""
        return 'take' in self.options

    @property
    def playable(self) -> bool:
        """Check if 'play' is in options"""
        return 'play' in self.options