"""
Defines the Core class and instantiates core object

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
    Callable,
    Iterable
)
if TYPE_CHECKING:
    from .card import Card
    from .player import Player

# < ========================================================
# < External Imports
# < ========================================================

from pprint import (
    pprint,
    pformat
)

# < ========================================================
# < Package Imports
# < ========================================================

from . import settings
from .utils import (
    group
)
from .rank import (
    RANK_DATA,
    RANK_NAMES
)
from . import lookups
from .snapshot import Snapshot

# < ========================================================
# < Core Class
# < ========================================================

class Core:

    def __init__(self) -> None:
        """Create core instance as a manager for game state"""
        self.players: list[Player] = []
        self.deck: list[Card] = []
        self.center: list[Card] = []
        self.burned: list[Card] = []
        self.standard: bool = True
        self.turn: int = 1
        self.player_index: int = 0

    def init(self, deck: list[Card], players: list[Player]) -> None:
        """Initialise the core, will deal cards to players"""

        self.players.clear()
        self.deck.clear()
        self.center.clear()
        self.burned.clear()
        self.standard = True
        self.turn = 1
        self.player_index = 0

        self.players[:] = players
        self.deck[:] = deck
        self._deal()

        if settings.quick:
            self.deck.clear()

    def _deal(self) -> None:
        """Deal cards in the deck to players"""
        
        for _ in range(settings.hidden_size):
            for player in self.players:
                card = self.deck.pop()
                player.hidden.append(card)

        for _ in range(settings.shown_size):
            for player in self.players:
                card = self.deck.pop()
                player.shown.append(card)

        for _ in range(settings.hand_size):
            for player in self.players:
                card = self.deck.pop()
                player.hand.append(card)

    @property  
    def round(self) -> int:
        """Get the current round from current turn and player count"""
        return (self.turn - 1) // len(self.players) + 1
    
    @property
    def player(self) -> Player:
        """Get current player using current player index"""
        return self.players[self.player_index]

    def next_player(self) -> None:
        """Cycle through player index"""
        self.player_index = (self.player_index + 1) % len(self.players)

    def card_to_rank(self, card: Card | None) -> str | None:
        """Convert card to rank, or return None if card is None"""
        return card.rank if card else None

    def get_top_card(self, cards: list[Card]) -> Card | None:
        """Get the top card of a given card list"""
        return cards[-1] if cards else None

    def get_top_rank(self, cards: list[Card]) -> str | None:
        """Get the top rank of a given card list"""
        card: Card | None = self.get_top_card(cards)
        return self.card_to_rank(card)
    
    def get_anchor_card(self, cards: list[Card]) -> Card | None:
        """Get the top card in a given card list that is not a 7"""

        for card in reversed(cards):
            if card.rank != '7':
                return card
        return None
    
    def get_anchor_rank(self, cards: list[Card]) -> str | None:
        """Get the top rank in a given card list that is not a 7"""
        card: Card | None = self.get_anchor_card(cards)
        return self.card_to_rank(card)
    
    def get_valid_ranks(self, rank: str | None, standard: bool) -> list[str]:
        """Get the valid card ranks that play on the given rank"""

        lookup = lookups.standard if standard else lookups.alternate
        ranks = lookup[rank]
        if ranks is None:
            raise UserWarning(f'Invalid game state detected for [{rank} | {standard}]')
        return ranks
    
    def get_card_combinations(self, cards: list[Card]) -> list[list[Card]]:
        """Get all the different combinations of ways to play a list of cards"""

        groups: dict[str, list[Card]] = group(cards, lambda card: card.rank)
        combinations: list[list[Card]] = []
        for rank, cards in groups.items():
            for i in range(1, len(cards) + 1):
                combinations.append(cards[:i])
        return combinations
    
    def same_rank(self, cards: list[Card]) -> bool:
        """Check if all cards in a card list are the same rank"""
        return all(card.rank == cards[0].rank for card in cards)
    
    def get_consecutive(self, cards: list[Card], ignore_sevens: bool) -> list[Card]:
        """Get consecutive cards of the same rank from the top of a card list"""

        cards = [c for c in cards if c.rank != '7'] if ignore_sevens else cards
        if not cards:
            return []
        
        output: list[Card] = []
        target: str = cards[-1].rank
        for card in reversed(cards):
            if card.rank == target:
                output.append(card)
            else:
                break
        return output
    
    def has_consecutive(self, cards: list[Card], n: int) -> bool:
        """Check if a list of cards has consecutive run of a single rank on top"""

        if len(cards) < n:
            return False
        
        consecutive: list[Card] = self.get_consecutive(cards, False)
        if len(consecutive) >= n:
            return True
        
        consecutive = self.get_consecutive(cards, True)
        return len(consecutive) >= n
    
    def has_quad(self, cards: list[Card]) -> bool:
        """Check if a list of cards has a quad on top"""
        return self.has_consecutive(cards, 4)
    
    def has_ten(self, cards: list[Card]) -> bool:
        """Check if a list of cards has a ten on top"""
        rank: str | None = self.get_top_rank(cards)
        return rank == '10'
    
    def should_burn(self, cards: list[Card]) -> bool:
        """Check if a list of cards has a ten on top or a four of a kind"""
        return self.has_quad(cards) or self.has_ten(cards)
    
    def sort_ranks_by_importance(self, ranks: Iterable[str]) -> list[str]:
        """Sort a given list of ranks by their importance value"""
        sorter: Callable = lambda r: RANK_DATA[r].importance
        return sorted(ranks, key = sorter)
    
    def sort_cards_by_importance(self, cards: Iterable[Card]) -> list[Card]:
        """Sort a given list of cards by their rank importance value"""
        sorter: Callable = lambda card: RANK_DATA[card.rank].importance
        return sorted(cards, key = sorter)
    
    def create_snapshot(self) -> Snapshot:
        """Create a Snapshot instance of the current game state"""
        
        turn: int = self.turn
        player: Player = self.player
        human: bool = player.human
        pile: list[Card] = player.current_pile
        if not pile:
            raise UserWarning('Win condition failed to trigger')
        pile_name: str = player.pile_name(pile)
        hidden: bool = pile_name == 'hidden'
        center: list[Card] = self.center
        deck: list[Card] = self.deck
        burned: list[Card] = self.burned
        standard: bool = self.standard
        actual_rank: str | None = self.get_top_rank(center)
        anchor_rank: str | None = self.get_anchor_rank(center)
        valid_ranks: list[str] = self.get_valid_ranks(anchor_rank, standard)

        playable_cards: list[Card] = []
        playable_combinations: list[list[Card]] = []
        options: list[str] = []

        if not hidden:
            playable_cards = [card for card in pile if card.rank in valid_ranks]
            if playable_cards:
                playable_combinations = self.get_card_combinations(playable_cards)
                options.append('play')
            if anchor_rank == '8' and standard:
                options.append('wait')
            elif len(self.center) > 0:
                options.append('take')

        else:
            playable_cards = pile[:]
            playable_combinations = [[card] for card in playable_cards]
            options.append('play')
        
        return Snapshot(
            turn = turn,
            player = player,
            human = human,
            pile = pile,
            pile_name = pile_name,
            hidden = hidden,
            center = center,
            deck = deck,
            burned = burned,
            standard = standard,
            actual_rank = actual_rank,
            anchor_rank = anchor_rank,
            valid_ranks = valid_ranks,
            playable_cards = playable_cards,
            playable_combinations = playable_combinations,
            options = options
        )

# < ========================================================
# < Core Instance (Singleton)
# < ========================================================

core: Core = Core()