from tkinter.constants import DISABLED
from typing import Literal, Union


class Game():

    WIN_SITUATION: list[list[str]] = [
        ['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'],
        ['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22'],
        ['00', '11', '22'], ['02', '11', '20']
    ]

    def __init__(self, first_color: str) -> None:
        self.first_color: str = first_color
        self.second_color: Literal['blue',
                                   'red'] = 'blue' if first_color == 'red' else 'red'
        self.amount_of_moves: int = 0
        self.squares: dict[str, str] = {str(x)+str(y): str(x)+str(y)
                                        for x in range(3) for y in range(3)}
        self.winner: Union[None, Literal['blue', 'red']] = None
        self.winner_squares: Union[None, list[str]] = None
        self.draw: bool = False

    def restart(self):
        self.first_color = self.second_color
        self.__init__(self.first_color)

    def move(self, square):
        self.__update_square(square)
        self.amount_of_moves += 1
        self.__update_square_dict(square)
        if self.__is_possible_to_win():
            self.__check_if_over()

    def __update_square(self, square):
        square['state'] = DISABLED
        square['bg'] = self.second_color if self.amount_of_moves % 2 != 0 else self.first_color

    def __update_square_dict(self, square):
        square_id = str(square['textvariable'])[-2:]
        self.squares[square_id] = square['bg']

    def __is_possible_to_win(self) -> bool: return self.amount_of_moves >= 3

    def __check_if_over(self):
        for situation in self.WIN_SITUATION:
            if self.squares[situation[0]] == self.squares[situation[1]] == self.squares[situation[2]]:
                self.winner = self.squares[situation[0]]
                self.winner_squares = situation
        if self.amount_of_moves == 9:
            self.draw = True
