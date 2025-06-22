from config import *

class Game:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.current_player = 'X'
        self.game_over = False

    def reset(self):
        self.__init__()

    def mark_square(self, row, col):
        if self.board[row][col] is None and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_win(self.current_player):
                self.game_over = True
                return f"{self.current_player} wins!"
            elif self.is_full():
                self.game_over = True
                return "Tie!"
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        return None

    def check_win(self, player):
        # Horizontal
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Vertical
        for col in range(BOARD_COLS):
            if all(self.board[row][col] == player for row in range(BOARD_ROWS)):
                return True
        # Diagonal
        if all(self.board[i][i] == player for i in range(BOARD_ROWS)):
            return True
        if all(self.board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)):
            return True
        return False

    def is_full(self):
        return all(all(cell is not None for cell in row) for row in self.board)
    
    def reset(self):
        self.__init__()
