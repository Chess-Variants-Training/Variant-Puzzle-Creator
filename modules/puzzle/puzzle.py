from modules.puzzle.position_list import position_list
from modules.bcolors.bcolors import bcolors
import json
import logging
import os

class puzzle:
    def __init__(self, last_pos, last_move, variant, engine, info_handler):
        self.last_pos = last_pos.copy()
        self.last_move = last_move
        self.variant = variant
        last_pos.push(last_move)
        self.positions = position_list(last_pos, engine, info_handler, variant)

    def to_dict(self):
        return {
            'variant': self.variant,
            'category': self.positions.category(),
            'last_pos': self.last_pos.fen(),
            'last_move': self.last_move.uci(),
            'move_list': " ".join(self.positions.move_list())
            }

    def color(self):
        return self.positions.position.turn

    def is_complete(self):
        return (self.positions.is_complete(
                self.positions.category(), 
                self.color(), 
                True, 
                self.positions.material_difference()
            )
            and not self.positions.ambiguous()
            and len(self.positions.move_list()) > 2)

    def generate(self):
        self.positions.generate()
        if self.is_complete():
            logging.debug(bcolors.OKGREEN + "Puzzle is complete" + bcolors.ENDC)
        else:
            logging.debug(bcolors.FAIL + "Puzzle incomplete" + bcolors.ENDC)

    def category(self):
        return self.positions.category()
