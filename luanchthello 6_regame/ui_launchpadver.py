""" Othello game GUI
    Humberto Henrique Campos Pinheiro
"""

import pygame
import sys
from pygame.locals import *
import time
from config import BLACK, WHITE, DEFAULT_LEVEL, HUMAN, COMPUTER
import os

class Gui:
    def __init__(self):
        """ Initializes graphics. """

        pygame.init()
        try:
            import launchpad_py as launchpad
        except ImportError:
            try:
                import launchpad
            except ImportError:
                sys.exit("error loading launchpad.py")
        self.lp = launchpad.LaunchpadMk2()
        self.mode = "Mk2"
        self.lp.Open(0,"Mk2")
        self.lp.ButtonFlush()
        self.lp.Reset()

        # colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (128, 128, 0)
        self.ShowmovesOn = 'On'

    def show_options(self):
        """ Shows game options screen and returns chosen options
        """
        player1 = HUMAN
        player2 = COMPUTER
        level = DEFAULT_LEVEL
        self.lp.ButtonFlush()
        self.lp.Reset()
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 2, 2, 3, 3, 0], 
                 [1, 0, 0, 1, 2, 0, 3, 3, 0], 
                 [1, 0, 0, 1, 2, 0, 3, 0, 0], 
                 [1, 1, 1, 1, 2, 2, 3, 0, 0], 
                 [8, 8, 9, 9, 4, 4, 6, 6, 0], 
                 [8, 0, 9, 9, 4, 4, 6, 6, 0], 
                 [8, 0, 9, 0, 5, 5, 7, 7, 0],
                 [8, 8, 9, 0, 5, 5, 7, 7, 0]]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.put_stone((j, i-1), board[i][j])
        print(level,'111')
        while True:
            but = self.lp.ButtonStateXY()
            if but != []:
                print(level,'111')
                if board[but[1]][but[0]]==1:
                    print(1)
                    print(level,'111')
                    return (player1, player2, level)
                elif board[but[1]][but[0]]==2:
                    player1 = COMPUTER
                    print(2)
                    for i in range(0,5):
                        for j in range(5,9):
                            if board[i][j-1] == 3:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==3:
                    player1 = HUMAN
                    print(3)
                    for i in range(0,5):
                        for j in range(5,9):
                            if board[i][j-1] == 2:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==8:
                    player2 = COMPUTER
                    print(8)
                    for i in range(5,9):
                        for j in range(0,5):
                            if board[i][j-1] == 9:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==9:
                    player2 = HUMAN
                    print(9)
                    for i in range(5,9):
                        for j in range(0,5):
                            if board[i][j-1] == 8:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==4:
                    print(4)
                    level=1
                    for i in range(5,9):
                        for j in range(4,9):
                            if board[i][j-1] in [5,6,7]:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==5:
                    print(5)
                    level=2
                    for i in range(5,9):
                        for j in range(4,9):
                            if board[i][j-1] in [7,6,4]:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==6:
                    print(6)
                    level=3
                    for i in range(5,9):
                        for j in range(4,9):
                            if board[i][j-1] in [5,7,4]:
                                self.put_stone((j-1, i-1), 0)
                elif board[but[1]][but[0]]==7:
                    print(7)
                    level=3
                    for i in range(5,9):
                        for j in range(4,9):
                            if board[i][j-1] in [5,6,4]:
                                self.put_stone((j-1, i-1), 0)
        return (player1, player2, level)

    def show_winner(self, player_color):
        if player_color == BLACK:
            coloring = 8
        elif player_color == WHITE:
            coloring = 16
        self.lp.LedAllOn(coloring)
        
    def get_chosen_player(self):
        """ Asks for a player
        """

    def get_chosen_level(self):
        """ Level options
        """
        
    def show_game(self):
        """ Game screen. """
        self.put_stone((3, 3), WHITE)
        self.put_stone((4, 4), WHITE)
        self.put_stone((3, 4), BLACK)
        self.put_stone((4, 3), BLACK)

    def put_stone(self, pos, color):
        """ draws piece with given position and color """
        if pos == None:
            return

        if color == BLACK:
            coloring = 9
        elif color == WHITE:
            coloring = 17
        elif color == 3:
            coloring = 24
        elif color == 4:
            coloring = 32
        elif color == 5:
            coloring = 40
        elif color == 6:
            coloring = 48
        elif color == 7:
            coloring = 56
        elif color == 8:
            coloring = 64
        elif color == 9:
            coloring = 72
        elif color == 10:
            coloring = 8
        else:
            coloring = 0

        self.lp.LedCtrlXYByCode(pos[0],pos[1]+1,coloring)

    def pulse_stone(self, pos, color):
        """ draws piece with given position and color """
        if pos == None:
            return

        if color == BLACK:
            coloring = 11
        elif color == WHITE:
            coloring = 19
        else:
            coloring = 0

        self.lp.LedCtrlPulseXYByCode(pos[0],pos[1]+1,coloring)

    def clear_square(self, pos):
        """ Puts in the given position a background image, to simulate that the
        piece was removed.
        """

    def get_mouse_input(self):
        """ Get place clicked by mouse
        """
        while True:
            but = self.lp.ButtonStateXY()
            if  but!=[]:
                if but[2] == 127:
                    position=(but[0],but[1]-1)
                    print(position)
                    return position

            time.sleep(.05)

    def update(self, board, blacks, whites, current_player_color, valid_moves):
        """Updates screen
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        self.whose_turn(current_player_color)
        self.put_stone((8, 0), 9)
 
        if current_player_color == BLACK:
            current_player_color = WHITE
        elif current_player_color == WHITE:
            current_player_color = BLACK
        if self.ShowmovesOn == 'On':
            self.put_stone((8, 7), 10)
            self.show_places(valid_moves, board, current_player_color)

    def showScore(self, blackStr, whiteStr, current_player_color):
        return 0

    def whose_turn(self, color):
        if color == BLACK:
            color = WHITE
        elif color == WHITE:
            color = BLACK
  
        for i in range(8):
            self.put_stone((i, -1), color)

    def show_places(self, valid_moves, board, current_player_color):
        print(valid_moves)
        for i in range(8):
            for j in range(8):
                if (i,j) in valid_moves:
                    self.pulse_stone((i, j), current_player_color)
                elif board[i][j] == 0:
                    self.put_stone((i, j), 0)

    def Showmove(self, moves, current_player_color, board):
        if self.ShowmovesOn == 'Off':
            self.ShowmovesOn = 'On'
            self.put_stone((8, 7), 10)
            self.show_places(moves, board, current_player_color)
        else:
            self.ShowmovesOn = 'Off'
            self.put_stone((8, 7), 0)
            for i in range(8):
                for j in range(8):
                    if (i,j) in moves:
                        self.put_stone((i, j), 0)

    def wait_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break

