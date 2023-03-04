import random


class Game:
    game = False

    def __init__(self):
        print('Game name:' + type(self).__name__)

    def start_game(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def new_game(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class TicTacToe(Game):
    board = []
    players = []
    marker = ''

    def get_board(self):
        return self.board

    def create_board(self):
        self.board = [' '] * 10
        self.board[0] = '#'

    def show_board(self):
        k = 1
        for x in range(0, 3):
            print(self.board[x + k] + ' | ' + self.board[x + k + 1] + ' | ' + self.board[x + k + 2])
            if x < 2:
                print('--| - |--')
            k += 2

    @staticmethod
    def read_user_input():
        user_input = 0
        check_user_input = True
        acceptable_values = range(1, 10)
        while check_user_input:
            user_input = input('Please enter number in range of [1-9]: ')
            if not user_input.isdigit():
                print('That is not a digit!')
            elif int(user_input) not in acceptable_values:
                print('Number is not in [1-9] range!')
            elif new_game_TicTacToe.read_board_cell(int(user_input)) != ' ':
                print('This cell already have a marker!')
            else:
                check_user_input = False
        return int(user_input)

    def update_board(self, cell_number, marker):
        self.board[cell_number] = str(marker)

    def read_board_cell(self, cell_number):
        return self.board[cell_number]

    @staticmethod
    def choose_marker():
        marker = ''
        while marker != 'X' and marker != 'O':
            marker = input('Player 1, choose X or O: ')
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        print('Player 1 is', player1)
        return player1, player2

    def win_check(self):
        k = 1
        y = 3
        z = 3
        result = False
        for x in range(0, 3):
            if self.board[x + k] == self.marker and self.board[x + k + 1] \
                    == self.marker and self.board[x + k + 2] == self.marker:
                result = True
            elif self.board[x + 1] == self.marker and self.board[k + y] \
                    == self.marker and self.board[z + y + k] == self.marker:
                result = True
            if x == 1:
                if self.board[x] == self.marker and self.board[z + z - 1] \
                        == self.marker and self.board[x + k + z + y] == self.marker:
                    result = True
            if x == 2:
                if self.board[x + 1] == self.marker and self.board[z + z - 1] \
                        == self.marker and self.board[k + x] == self.marker:
                    result = True
            k += 2
            y -= 1
        return result

    @staticmethod
    def first_turn():
        return random.randint(0, 1)

    def change_player(self):
        if self.marker == 'X':
            return 'O'
        else:
            return 'X'

    def board_have_place(self):
        if ' ' in self.board:
            return False
        else:
            return True

    def new_game(self):
        self.create_board()
        self.players = self.choose_marker()
        self.marker = self.players[self.first_turn()]
        print(self.marker, 'goes first')
        self.show_board()
        self.game_process()

    @staticmethod
    def start_game(**kwargs):
        user_exit_input = ''
        while user_exit_input not in ['Y', 'N']:
            user_exit_input = input('Start game? (Y or N) ')
            if user_exit_input not in ['Y', 'N']:
                print('Sorry invalid input, please choose Y or N')
        if user_exit_input == 'Y':
            return True
        else:
            return False

    def game_process(self):
        while self.game:
            print(self.marker, ' Turn')
            cell_number = self.read_user_input()
            self.update_board(cell_number, self.marker)
            self.show_board()
            if self.win_check() or self.board_have_place():
                if self.board_have_place():
                    print('TIE!')
                else:
                    print(self.marker, 'WIN!')
                self.game = self.start_game()
                if self.game is not True:
                    break
                else:
                    self.new_game()
            else:
                self.marker = self.change_player()


new_game_TicTacToe = TicTacToe()
new_game_TicTacToe.game = new_game_TicTacToe.start_game()
if new_game_TicTacToe.game:
    new_game_TicTacToe.new_game()
