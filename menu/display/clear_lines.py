"""Clears terminal"""

import sys
import os

def clear_lines(lines:int = 1) -> None:
    """
    Clears from current line, n lines up.
    * lines (default 1): must be a positive integer.
    * setting lines to -1 clears the entire terminal.
    """
    if lines != -1:
        for _ in range(lines):
            sys.stdout.write('\x1b[1A' )    # Move cursor up.
            sys.stdout.write('\x1b[2K' )    # Erase line at cursor.
    else:
        # Repeated 2 times to get rid of that annoying scroll buffer.
        # Set to a higher value for smaller terminals
        # NOTE: Higher values results in terminal flickering
        for _ in range(2):
            os.system('cls' if os.name == 'nt' else 'clear')