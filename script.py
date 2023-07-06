class TicTacToe:
    def __init__(self):
        self.available_cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        self.players = []
        self.table = """
            A   B   C

        1   A1  B1  C1

        2   A2  B2  C3

        3   A3  B3  C3"""
        self.winner = ''
        self.last_played = ''
        self.combinations_to_win = [
            ['A1', 'A2', 'A3'],
            ['B1', 'B2', 'B3'],
            ['C1', 'C2', 'C3'],
            ['A1', 'B1', 'C1'],
            ['A2', 'B2', 'C2'],
            ['A3', 'B3', 'C3'],
            ['A1', 'B2', 'C3'],
            ['A3', 'B2', 'C1']
        ]

    def start_game(self, phase = 0):
        self.available_cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        self.table = """
            A   B   C

        1   A1  B1  C1

        2   A2  B2  C3

        3   A3  B3  C3"""
        self.winner = ''
        self.last_played = ''
        if phase == 0:
            self.players = []
            print("Welcome to Sebas TicTacToe made in Python 3, hope you enjoy while playing!")
            print("Let's begin by setting your names")
            player1 = Player(input("Player1's name: "), self)
            player2 = Player(input("Player2's name: "), self)
            self.players.extend([player1, player2])
            print("Let's start!")
            self.start_game(1)
        if phase == 1:
            player1 = self.get_player(1)
            player2 = self.get_player(2)
            while self.check_winner() == False:
                self.draw_table()
                if self.last_played == self.get_player(1):
                    player2.play_round()
                else:
                    player1.play_round()
            self.draw_table()
            print("We have a winner!")
            print("Congratulations on winning {winner_name}".format(winner_name=self.winner))
            play_again = input("Do you wish to play again? (Y/N) ")
            if play_again == 'Y':
                for player in self.players:
                    player.played_cells = []
                self.start_game(1)
            else:
                print("Okay! Have a great day.")

    def get_player(self, index):
        return self.players[index - 1]

    def draw_table(self):
        table_to_draw = self.table
        for cell in self.available_cells:
            table_to_draw = table_to_draw.replace(cell, ' ')
        print(table_to_draw)

    def check_winner(self):
        for player in self.players:
            for combination in self.combinations_to_win:
                if all(cell in player.played_cells for cell in combination):
                    self.winner = player.name
                    return True
        return False
    
class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.played_cells = []

    def is_o(self):
        return self == self.game.players[0]
    
    def is_x(self):
        return self == self.game.players[1]

    def play_round(self):
        print("{player_name} it's your turn".format(player_name=self.name))
        selected_cell = input("Select one cell (Ex: A1, B2, C3): ")
        while selected_cell not in self.game.available_cells:
            print("Please select a valid cell")
            selected_cell = input("Select one cell (Ex: A1, B2, C3): ")
        self.played_cells.append(selected_cell)
        self.game.available_cells.remove(selected_cell)
        if self.is_o():
            self.game.table = self.game.table.replace(selected_cell, 'O ')
        elif self.is_x():
            self.game.table = self.game.table.replace(selected_cell, 'X ')
        self.game.last_played = self

game = TicTacToe()

game.start_game()