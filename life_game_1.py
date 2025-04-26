import time
import random

def count_live_neighbors(board, row, col):
    """Liczy żywych sąsiadów dla komórki na pozycji (row, col)."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neighbors = 0
    rows, cols = len(board), len(board[0])

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            live_neighbors += board[r][c]

    return live_neighbors

def next_generation(board):
    """Oblicza stan planszy dla następnego pokolenia."""
    rows, cols = len(board), len(board[0])
    new_board = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(board, row, col)
            if board[row][col] == 1:
                # Komórka żywa pozostaje żywa, jeżeli ma 2 lub 3 żywych sąsiadów
                new_board[row][col] = 1 if live_neighbors in (2, 3) else 0
            else:
                # Komórka martwa staje się żywa, jeżeli ma dokładnie 3 żywych sąsiadów
                new_board[row][col] = 1 if live_neighbors == 3 else 0

    return new_board

def display_board(board):
    """Wizualizuje planszę w formie tekstowej."""
    for row in board:
        print(''.join('x' if cell else 'o' for cell in row))
    print()

def game_of_life(initial_board, generations):
    """Uruchamia grę w życie na zadanej planszy przez określoną liczbę pokoleń."""
    current_board = initial_board

    for generation in range(generations):
        print(f"Pokolenie {generation + 1}:")
        display_board(current_board)

        start_time = time.time()
        current_board = next_generation(current_board)
        end_time = time.time()

        print(f"Czas obliczeń: {end_time - start_time:.6f} sekund\n")

        user_input = input("Naciśnij Enter, aby kontynuować, lub wpisz 'stop', aby zakończyć: ").strip().lower()
        if user_input == 'stop':
            print("Symulacja została zatrzymana.")
            break

def generate_random_board(rows, cols):
    """
    Generuje losową planszę początkową o wymiarach rows x cols.
    Komórki są losowo ustawiane jako żywe (1) lub martwe (0).
    """
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Przykład użycia
rows, cols = 5, 5  # Wymiary planszy
initial_board = generate_random_board(rows, cols)

game_of_life(initial_board, 500)