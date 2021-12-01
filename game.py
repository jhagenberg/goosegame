import random

from typing import Optional, Tuple


class Game:

    """Two players give their names and start the game.
On a player's turn, they roll two 6-sided dice. The player moves their piece the total number of spaces as the total of their dice roll. (e.g. rolling a 3 and 4 means moving 7 spaces.)
Win: A player wins if they land exactly on space 63.
!!! Bounce: If a player rolls past space 63 (e.g. 64), they "bounce", and go back to where they began their turn.
Bridge: If a player lands on space 9, then they go directly to space 16 in the same turn.
Goose: If a player lands on space 4, 8, 13, 18, 23, or 27 (a green space), they get to roll again!
Prank: If a player lands on a space occupied by another player, then they send the other player back to their previous position (e.g. if player 1 was on 20, then lands on player 2 at space 22, then player 2 is moved immediately to space 20.)"""
    
    def __init__(self, player1: str, player2: str) -> None:
        self.player1 = player1  # Save player1 data in self.player1
        self.player2 = player2 # Save player2 data in self.player2
        self.round_number = 1
        self.player1_space = None
        self.player1_space_previous = 0
        self.player2_space = None
        self.player2_space_previous = 0
        self.dice = None
    
    def get_player1_name(self) -> str:
        "Returns the name of Player 1 as a string."

        return self.player1
    
    def get_player2_name(self) -> str:
        "Returns the name of Player 2 as a string."
        return self.player2
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""

        return self.player1_space
    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""

        return self.player2_space
        
    def get_current_player(self) -> str:
        """Returns the name of the current player."""
        if self.round_number % 2 == 1:
            current_player = self.player1
        else:
            current_player = self.player2
        return current_player
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        self.dice = (a, b)
        #self.player2_space += sum(self.dice)
        #self.player1_space += sum(self.dice)
        self.round_number += 1
        print(self.round_number)
        self.set_player_space()
        return None

    def set_player_space(self) ->None:
        """Sets the space of player 1 in place"""
        spaces = [5, 9, 14, 19, 24, 28]
        if self.get_current_player() == self.player1:
            if self.get_player1_space() == None:
                previous_value = 0
            else:
                previous_value = self.get_player1_space()
            self.player1_space_previous = previous_value
            new_space = previous_value + sum(self.dice)
            if new_space <= 63:
                self.player1_space = new_space
            if new_space == 9:
                self.player1_space = 16
            if new_space == self.player2_space:
                self.player2_space = self.player2_space_previous
            if new_space in spaces:
                self.round_number -= 1

        else:
            if self.get_player2_space() == None:
                previous_value = 0
            else:
                previous_value = self.get_player2_space()
            self.player2_space_previous = previous_value
            new_space = previous_value + sum(self.dice)
            if new_space <= 63:
                self.player2_space = new_space
            if new_space == 9:
                self.player2_space = 16
            if new_space == self.player1_space:
                self.player1_space = self.player1_space_previous
            if new_space in spaces:
                self.round_number -= 1

        return None
        
    def get_last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""
        print(self.dice)
        return self.dice
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        if self.player1_space == 63 or self.player2_space == 63:
            return True
        else:
            return False
    
    def get_winner(self) -> Optional[str]:
        """Returns None (if the game is not over) or the name of the winner"""
        if self.is_over():
            return self.get_current_player()
        else:
            return None
    
    
    