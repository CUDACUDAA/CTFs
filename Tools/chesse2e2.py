from chess import Board
from math import log2
import ast

# Чтение последовательности ходов из файла
with open("moves.txt", "r") as file:
    moves_list = ast.literal_eval(file.read().strip())

# Инициализация шахматной доски
output_data = ""

# Обработка каждой игры
for moves in moves_list:
    chess_board = Board()
    for move_index, move in enumerate(moves):
        legal_move_ucis = [legal_move.uci() for legal_move in chess_board.legal_moves]
        if move not in legal_move_ucis:
            print(f"Warning: Move {move} not found in legal moves at move {move_index + 1}, skipping this move.")
            continue

        # Получаем индекс хода и преобразуем его в двоичный формат
        move_index_in_legal = legal_move_ucis.index(move)
        move_binary = bin(move_index_in_legal)[2:]

        # Определяем длину необходимой двоичной строки
        max_binary_length = int(log2(len(legal_move_ucis)))
        required_padding = max(0, max_binary_length - len(move_binary))
        move_binary = ("0" * required_padding) + move_binary

        # Выполняем ход на доске
        chess_board.push_uci(move)
        output_data += move_binary

# Преобразование двоичных данных в текст
ascii_output = ""
for i in range(0, len(output_data), 8):
    byte = output_data[i:i+8]
    if len(byte) == 8:
        ascii_output += chr(int(byte, 2))

print("Decoded ASCII Output:", ascii_output)
