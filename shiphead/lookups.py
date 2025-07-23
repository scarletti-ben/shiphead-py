"""
Defines the lookup tables for card playability

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Lookup Dictionaries
# < ========================================================

standard: dict[str | None, list[str] | None] = {
    None: ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '2': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '3': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '4': ['2', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '5': ['2', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '6': ['2', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '7': None,
    '8': ['8'],
    '9': ['2', '3', '4', '5', '6', '7', '8', '9'],
    '10': None,
    'jack': ['2', '7', '10', 'jack', 'queen', 'king', 'ace'],
    'queen': ['2', '7', '10', 'queen', 'king', 'ace'],
    'king': ['2', '7', '10', 'king', 'ace'],
    'ace': ['2', '7', '10', 'ace'],
}
"""Lookup for playable ranks for a given rank during standard table state"""

alternate: dict[str | None, list[str] | None] = {
    None: None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    '7': None,
    '8': ['2', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '9': ['2', '7', '9', '10', 'jack', 'queen', 'king', 'ace'],
    '10': None,
    'jack': None,
    'queen': None,
    'king': None,
    'ace': None
}
"""Lookup for playable ranks for a given rank during alternate table state"""