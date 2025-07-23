"""
Defines settings variables for the game

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Settings Variables
# < ========================================================

debugging: bool = True
player_count: int = 2
hand_size: int = 5
shown_size: int = 3
hidden_size: int = 3
quick: bool = True
separator: str = '·'
suit_style: str = 'symbol_coloured'
rank_style: str = 'short_upper'
shuffled: bool = True
log_mode: str = 'print'
log_file: str = 'game.log'
delay: bool = True
behaviours: dict[str, int] = {
    'random': 10,
    'good': 20, 
    'better': 50,
    'best': 100
}