"""
Main entry point for the game
- Imports relevant modules from the game's package
- Staging area for experimental code

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
    Optional,
    Any,
    Literal,
    LiteralString,
    TypedDict, 
    Iterable,
    Callable,
    TypeVar,
    Dict,
    List
)
if TYPE_CHECKING:
    from .core import Core
    from .rank import Rank
    from .suit import Suit
    from .card import Card
    from .player import Player
    from .snapshot import Snapshot

# < ========================================================
# < External Imports
# < ========================================================

import random
from pprint import (
    pprint, 
    pformat
)

# < ========================================================
# < Package Imports
# < ========================================================

from .utils import (
    cprint,
    index_input,
)
from . import settings
from .core import core
from .rank import (
    RANK_NAMES, 
    RANK_DATA
)
from .suit import SUIT_NAMES
from .card import Card
from .player import Player
from .snapshot import Result

# < ========================================================
# < Create Deck Function
# < ========================================================

def create_deck(
    suits: list[str], 
    ranks: list[str], 
    shuffle: bool = True
) -> list[Card]:
    """Create a card list with all combinations of suits / ranks"""

    cards: list[Card] = []
    for suit in suits:
        for rank in ranks:
            card = Card(rank, suit)
            cards.append(card)
    if shuffle:
        random.shuffle(cards)
    return cards

# < ========================================================
# < Assess Pending Function
# < ========================================================

def assess_pending(
    pending: list[Card], 
    valid_ranks: list[str], 
    hidden: bool
) -> bool:
    """Assess pending list of cards"""

    size: int = len(pending)

    if size < 1:
        raise UserWarning('No cards in pending')

    if size > 4:
        raise UserWarning('More than 4 cards in pending')
    
    target_rank: str = pending[0].rank

    if not all([card.rank  == target_rank for card in pending]):
        raise UserWarning('Pending cards do not share the same rank')

    if target_rank not in valid_ranks:
        if not hidden:
            raise UserWarning('Pending cards are not playable')
        else:
            return False

    return True

# < ========================================================
# < Assess Pending Function
# < ========================================================

def assess_result(
        result: Result
) -> bool:
    """Assess result"""

    if result.option == 'play' and not result.cards:
        raise UserWarning('Cards must be submitted with play option')
        
    return True

# < ========================================================
# < Process Snapshot Function
# < ========================================================

def process_snapshot(snapshot: Snapshot) -> Result:
    """Process a Snapshot instance to add result"""

    options: list[str] = snapshot.options
    combos: list[list[Card]] = snapshot.playable_combinations
    option: str = ''
    cards: list[Card] = []

    ranks_sorted: list[str] = core.sort_ranks_by_importance(set([card.rank for card in snapshot.playable_cards]))

    if snapshot.human:

        index: int = 0
        entries: list[tuple[str, str, list[Card]]] = []

        if 'wait' in options:
            entries.append((f"[{index}] wait", 'wait', []))
            index += 1

        if 'take' in options:
            entries.append((f"[{index}] take", 'take', []))
            index += 1

        if 'play' in options:
            for combo in combos:
                entries.append((f"[{index}] play {combo}", 'play', combo))
                index += 1

        for text, _, _ in entries:
            print(text)

        chosen_index: int = index_input(entries)
        _, option, cards = entries[chosen_index]

    else:

        if 'play' in options:
            option = 'play'
            behaviour: str = random.choices(*zip(*settings.behaviours.items()))[0]
            choices: list[list[Card]]
            print(combos)

            match behaviour:
                case 'random':
                    cards = random.choice(combos)
                case 'good':
                    chosen_rank: str = ranks_sorted[0]
                    choices = [combo for combo in combos if combo[0].rank == chosen_rank]
                    cards = random.choice(choices)
                case 'better':
                    chosen_rank: str = ranks_sorted[0]
                    choices = [combo for combo in combos if combo[0].rank == chosen_rank]
                    cards = sorted(choices, key = len)[-1]
                case 'best':
                    quads: list[list[Card]] = []
                    for combo in combos:
                        proposed = core.deck + combo
                        if core.has_quad(proposed):
                            quads.append(combo)
                    if quads:
                        choices = quads
                        sorter: Callable[[list[Card]], int] = lambda quad: quad[0].importance
                        cards = sorted(choices, key = sorter)[0]
                    else:
                        chosen_rank: str = ranks_sorted[0]
                        choices = [combo for combo in combos if combo[0].rank == chosen_rank]
                        cards = sorted(choices, key = len)[-1]
                
        else:
            option = options[0]

    result: Result = Result(
        option = option,
        cards = cards
    )
    snapshot.result = result
    return result

# < ========================================================
# < Printout Functions
# < ========================================================

def printout_snapshot(snapshot: Snapshot) -> None:
    """Print a given snapshot instance"""
    
    print(
        # f'Turn: {snapshot.turn}',
        f'Player: {snapshot.player}',
        f'Human: {snapshot.human}',
        f'Pile: {snapshot.pile_name}',
        f'Center: {snapshot.center}',
        f'Burned: {snapshot.burned}',
        f'Deck: {snapshot.deck}',
        f'Standard: {snapshot.standard}',
        f'Actual rank: {snapshot.actual_rank}',
        f'Anchor rank: {snapshot.anchor_rank}',
        f'Valid ranks: [{", ".join(RANK_DATA[rank].short_upper for rank in snapshot.valid_ranks)}]',
        f'Accessible cards: {snapshot.pile}',
        f'Playable cards: {snapshot.playable_cards}',
        f'Waitable: {snapshot.waitable}',
        f'Takeable: {snapshot.takeable}',
        f'Playable: {snapshot.playable}',
        f'Playable combinations: {
            pformat(snapshot.playable_combinations, indent = 2, compact = False)
        }',
        sep = '\n'
    )

# < ========================================================
# < Entry Point
# < ========================================================

def main() -> None:
    """Entry point for the game, containing main game loop"""

    settings.delay = False

    core.init(
        deck = create_deck(
            SUIT_NAMES, 
            RANK_NAMES, 
            settings.shuffled
        ),
        players = [
            Player('Ben', True, 1), 
            Player('PC', False, 2)
        ]
    )

    while True:

        snapshot: Snapshot = core.create_snapshot()

        print("=" * 79)
        print(f'Turn {snapshot.turn}')
        print("=" * 79)

        printout_snapshot(snapshot)
        print("-" * 30)
        print('>>> Decision')
        print("-" * 30)
        print(f"Available: {snapshot.pile}")
        print(f"Center: {core.center}")

        result: Result = process_snapshot(snapshot)
        assess_result(result)

        player: Player = snapshot.player
        pending: list[Card] = []
        option: str = result.option
        cards: list[Card] = result.cards

        print(f'\nOption: {option}')
        print(f'Cards: {cards}\n')

        switching: bool = True
        deactivating: bool = False

        match option:

            case 'play':
                for card in cards:
                    snapshot.pile.remove(card)
                    pending.append(card)

                if not assess_pending(pending, snapshot.valid_ranks, snapshot.hidden):
                    player.hand.extend(core.center)
                    core.center.clear()
                else:
                    while pending:
                        core.center.extend(pending)
                        pending.clear()

                if core.should_burn(core.center):
                    core.burned.extend(core.center)
                    core.center.clear()
                    switching = False

                while core.deck and len(player.hand) < settings.hand_size:
                    card = core.deck.pop()
                    player.hand.append(card)
                    print(f'Drew {card}')
                
                if player.winning():
                    print(f'Player {player} has won')
                    break

                deactivating = core.get_top_rank(core.center) == '7' and core.get_anchor_rank(core.center) == '9'

            case 'take':
                player.hand.extend(core.center)
                core.center.clear()

            case 'wait':
                deactivating = True

        core.turn += 1
        if switching:
            core.next_player()
        core.standard = not deactivating

        if settings.delay:
            input(f'End of {player} turn, press Enter to continue...')
        
        print()

# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":    
    main()

    # POSTIT - Move printout functions to __repr__ or as class methods
    # POSTIT - Find correct homes for functions defined in shiphead.__main__.py
    # POSTIT - Humans can see hidden cards
    # POSTIT - Consider removing certain attributes  from Snapshot that you only want to acess via Core