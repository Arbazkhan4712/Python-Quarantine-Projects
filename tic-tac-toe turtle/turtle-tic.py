from ttt_util import TicTacToeUI, HumanPlayer, BotPlayer
from random import shuffle


class TicTacToe:
    def __init__(self, player1, player2):
        """Initialize a game of tic tac toe with the given players
        (HumanPlayer or BotPlayer objects). The player with the first
        move alternates each game, starting with player1.
        """
        if player1.mark == player2.mark:
            raise ValueError("players must not use the same mark")
        self.p1 = player1
        self.p2 = player2
        self.turn_order = [self.p1, self.p2]
        self.board = [None] * 9
        self.ties = 0
        self.win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.UI = TicTacToeUI()
        self.UI.draw_grid()
        self.print_stats()
        self.start_game()
        self.UI.wn.mainloop()

    def start_game(self):
        """Call the correct game function based on the player types."""
        self.players = self.turn_order.copy()
        first = self.players[0]
        if all(player.player_type == 'human' for player in self.players):
            self.UI.display(first.name, 'top', first.color)
            self.UI.wn.onclick(self.human_game)
        elif all(player.player_type == 'bot' for player in self.players):
            self.bot_game()
        else:
            if first.player_type == 'bot':
                self.bot_take_turn(first)
                self.players.reverse()
            self.UI.wn.onclick(self.human_bot_game)

    def human_game(self, x, y):
        """Start a game with two human players. Accepts the coordinates
        of a user click passed by an onclick call.
        """
        # Remove event binding
        self.UI.wn.onclick(None)
        # Get the board section of the clicked point
        pos = self.get_position(x, y)
        # Exit if click is outside the grid or the grid section isn't empty
        if pos is None or self.board[pos] is not None:
            self.UI.wn.onclick(self.human_game)
            return
        player = self.players[0]
        self.take_turn(player, pos)
        if self.check_if_won(self.board, player.mark):
            self.end_game(player)
            return
        elif None not in self.board:
            self.end_game('tie')
            return
        self.players.reverse()
        # Reactivate event binding and display who's turn it is
        self.UI.wn.onclick(self.human_game)
        self.UI.display(self.players[0].name, 'top', self.players[0].color)

    def bot_game(self):
        """Start a game with two bot players. Should result in a tie
        every time.
        """
        while None in self.board:
            self.bot_take_turn(self.players[0])
            if self.check_if_won(self.board, self.players[0].mark):
                self.end_game(self.players[0])
                return
            self.players.reverse()
        self.end_game('tie')

    def human_bot_game(self, x, y):
        """Start a game with a human and bot player. Accepts the
        coordinates of a user click passed by an onclick call.
        """
        self.UI.wn.onclick(None)
        usr_pos = self.get_position(x, y)
        if usr_pos is None or self.board[usr_pos] is not None:
            self.UI.wn.onclick(self.human_bot_game)
            return
        for player in self.players:
            if player.player_type == 'human':
                self.take_turn(player, usr_pos)
            else:
                self.bot_take_turn(player)
            if self.check_if_won(self.board, player.mark):
                self.end_game(player)
                return
            elif None not in self.board:
                self.end_game('tie')
                return
        self.UI.wn.onclick(self.human_bot_game)

    def print_stats(self):
        """Print or update the stats text."""
        stats_text = (
            f"{self.p1.name} ({self.p1.mark}): {self.p1.wins}   Ties: "
            f"{self.ties}   {self.p2.name} ({self.p2.mark}): {self.p2.wins}")
        self.UI.display(stats_text, 'bottom')

    def get_position(self, x, y):
        """Return the grid section (0-8) of the given coordinates."""
        if x > -225 and x < -75 and y > 75 and y < 225:
            position = 0
        elif x > -75 and x < 75 and y > 75 and y < 225:
            position = 1
        elif x > 75 and x < 225 and y > 75 and y < 225:
            position = 2
        elif x > -225 and x < -75 and y > -75 and y < 75:
            position = 3
        elif x > -75 and x < 75 and y > -75 and y < 75:
            position = 4
        elif x > 75 and x < 225 and y > -75 and y < 75:
            position = 5
        elif x > -225 and x < -75 and y > -225 and y < -75:
            position = 6
        elif x > -75 and x < 75 and y > -225 and y < -75:
            position = 7
        elif x > 75 and x < 225 and y > -225 and y < -75:
            position = 8
        else:
            position = None
        return position

    def take_turn(self, player, position):
        """Update the board with player's move at the given position."""
        self.board[position] = player.mark
        print(player.name, "marks section", position)
        self.UI.mark(player.mark, position, player.color)

    def bot_take_turn(self, player):
        """Take a turn with the given player at the position chosen by
        the minimax algorithm.
        """
        self.minimax_calls = 0
        pos, score = self.minimax_choose_pos(self.board, player.mark)
        print(f"Minimax score: {score}, function calls: {self.minimax_calls}")
        self.take_turn(player, pos)

    def minimax_choose_pos(self, board, turn):
        """Return a tuple with the best position for the player with the
        given mark to play on the given board and the score associated
        with that move. A score of 1 means the player has a guaranteed
        win, -1 indicates a loss if the opponent plays well, and 0 means
        the game will end in a tie.
        How it works:
        1. Play in each empty position on a copy of the board.
        2. If the board is at a terminal state, score it for the current
           player: 1 for a win, -1 for a loss, 0 for a tie.
        3. If the board is not at a terminal state, recursively run the
           function on the new board for the opponent until a terminal
           state is reached.
        4. Return the maximum score along with the position that
           resulted in that score.
        """
        self.minimax_calls += 1
        opponent = 'o' if turn == 'x' else 'x'
        empty_pos = [pos for pos in range(9) if not board[pos]]
        shuffle(empty_pos)
        max_score = -10
        for pos in empty_pos:
            # Play on a new board
            new_board = board.copy()
            new_board[pos] = turn
            # Score the board
            if self.check_if_won(new_board, turn):
                score = 1
            elif self.check_if_won(new_board, opponent):
                score = -1
            elif None not in new_board:
                score = 0
            else:
                # Game is not over, recursively check child nodes
                score = -self.minimax_choose_pos(new_board, opponent)[1]
            # Maximize the score
            if score == 1:
                # 1 is the best possible score so we can stop searching
                return (pos, score)
            if score > max_score:
                best_pos = pos
                max_score = score
        return (best_pos, max_score)

    def check_if_won(self, board, mark):
        """Return True if the player with the given mark has won."""
        return any(all(board[p] == mark for p in l) for l in self.win_lines)

    def end_game(self, winner):
        """Show game over text and update the stats based on the winner
        (a player object or 'tie').
        Bind a screen click event to reset().
        """
        if winner == 'tie':
            self.ties += 1
            msg = "Tie Game"
            color = 'black'
        else:
            winner.wins += 1
            msg = "{} Wins!".format(winner.name)
            color = winner.color
        self.UI.display(msg, 'top', color)
        print(msg, "\n")
        self.print_stats()
        self.UI.wn.onclick(self.reset)

    def reset(self, *_):  # Ignore coordinates from onclick call
        """Clear game over text, reset board, and start a new game."""
        self.UI.wn.onclick(None)
        self.UI.t_top_text.clear()
        self.UI.t_marks.clear()
        self.board = [None] * 9
        self.turn_order.reverse()
        self.start_game()


def main():
    """Initialize two players and a game of tic tac toe."""
    p1 = HumanPlayer("Player", 'x')
    p2 = BotPlayer("Bot", 'o')
    game = TicTacToe(p1, p2)


if __name__ == '__main__':
    main()