available_cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
played_cells = {}
table = """
    A   B   C

1   A1  B1  C1

2   A2  B2  C3

3   A3  B3  C3"""

print("Welcome to Sebas TicTacToe made in Python 3, hope you enjoy while playing!")
print("Let's begin by setting your names")
player1_name = input("Player1's name: ")
player2_name = input("Player2's name: ")
played_cells.update({player1_name:[], player2_name:[]})
print("Great! Let's start")