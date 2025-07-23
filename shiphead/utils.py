"""
Defines project-agnostic utility functions

Author: Ben Scarletti
Source: https://github.com/scarletti-ben/shiphead-py
Licence: MIT
"""

# < ========================================================
# < Typing Imports
# < ========================================================

from typing import (
    Iterable,
    Callable,
    TypeVar,
    Dict,
    List,
    Any
)

# < ========================================================
# < External Imports
# < ========================================================

import re

# < ========================================================
# < Custom Types
# < ========================================================

T = TypeVar('T')
K = TypeVar('K')

# < ========================================================
# < Group Function
# < ========================================================

def group(
    iterable: Iterable[T], 
    func: Callable[[T], K]
) -> Dict[K, List[T]]:
    """Group items into lists in a dictionary, using the given function"""

    groups: Dict[K, List[T]] = {}
    for item in iterable:
        key = func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# < ========================================================
# < Coulour String Function
# < ========================================================

def cstring(
    text: str, 
    rgb: tuple[int, int, int] = (0, 255, 255)
) -> str:
    """Get an ANSI coloured string for use in terminal"""

    r, g, b = rgb
    return f'\033[38;2;{r};{g};{b}m{text}\033[39m'

# < ========================================================
# < Coulour Print Function
# < ========================================================

def cprint(
    data: Any, 
    rgb: tuple[int, int, int] = (0, 255, 255), 
    end: str = "\n"
) -> None:
    """Print an ANSI coloured string for use in terminal"""

    text: str = str(data)
    output: str = cstring(text, rgb)
    print(output, end = end)

# < ========================================================
# < ANSI Colour Code Stripping Function
# < ========================================================

def strip_ansi(text: str) -> str:
    """Strip ANSI colour codes from a given string"""

    pattern: re.Pattern[str] = re.compile(
        r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return pattern.sub('', text)

# < ========================================================
# < Integer Selection Function for Terminal
# < ========================================================

def integer_input(maximum: int, minimum: int = 0) -> int:
    """Get valid integer between two values, inclusive, via user input"""

    assert -1 < minimum <= maximum
    message: str = f"Selection [{minimum} - {maximum}]: "
    while True:
        selection: str = input(message)
        if selection.isdigit():
            number: int = int(selection)
            if minimum <= number <= maximum:
                return number

# < ========================================================
# < Index Input
# < ========================================================

def index_input(_iterable: list[Any] | set[Any] | dict[Any, Any] | tuple[Any, ...]) -> int:
    """Get valid index from a given iterable via user input"""
    
    assert len(_iterable) > 0
    return integer_input(len(_iterable) - 1, 0)