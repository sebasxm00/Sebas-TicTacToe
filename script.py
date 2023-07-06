available_cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
played_cells = {}
table = """
    A   B   C

1   A1  B1  C1

2   A2  B2  C3

3   A3  B3  C3"""
winner = ''

def draw_table():
    draw_table = table
    for cell in available_cells:
        draw_table = draw_table.replace(cell, '')
    print(draw_table)

def play_round(name):
    global table
    print(name + " it's your turn")
    player_cell = input("Select one cell (Ex: A1, B2, C3): ")
    played_cells[name].append(available_cells.pop(available_cells.index(player_cell)))
    if name == player1_name:
        table = table.replace(player_cell, 'O')
    else:
        table = table.replace(player_cell, 'X')

def check_win():
    global winner
    combinations_to_win = [
        ['A1', 'A2', 'A3'],  # Filas
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'],  # Columnas
        ['A2', 'B2', 'C2'],
        ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'],  # Diagonales
        ['A3', 'B2', 'C1']
    ]

    for player_name, cells in played_cells.items():
        for combination in combinations_to_win:
            if all(cell in cells for cell in combination):
                winner = player_name
                return True

    return False


print("Welcome to Sebas TicTacToe made in Python 3, hope you enjoy while playing!")
print("Let's begin by setting your names")
player1_name = input("Player1's name: ")
player2_name = input("Player2's name: ")
played_cells.update({player1_name:[], player2_name:[]})
print("Great! Let's start")

last_played = ''

while(check_win() == False):
    draw_table()
    if last_played == player1_name:
        play_round(player2_name)
        last_played = player2_name
    else:
        play_round(player1_name)
        last_played = player1_name

draw_table()
print("Winner: " + winner)