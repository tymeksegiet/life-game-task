Oto implementacja gry w życie w Pythonie, z naciskiem na czytelność i jasność kodu. Skrypt zawiera funkcję `game_of_life`, która oblicza kolejne pokolenia oraz funkcję `display_board`, która wizualizuje planszę.

```python
import time

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

# Przykładowa plansza początkowa
initial_board = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Uruchom grę w życie na 5 pokoleń
game_of_life(initial_board, 5)
```

### Wyjaśnienie kodu:
1. **`count_live_neighbors`** - Funkcja ta liczy żywych sąsiadów dla danej komórki, sprawdzając wszystkie 8 możliwych kierunków (boki, góra, dół i przekątne).

2. **`next_generation`** - Tworzy nową planszę na podstawie aktualnego stanu, stosując zasady gry w życie.

3. **`display_board`** - Wizualizuje planszę, używając 'x' dla żywych komórek i 'o' dla martwych.

4. **`game_of_life`** - Uruchamia grę dla określonej liczby pokoleń, wyświetlając planszę i mierząc czas obliczeń dla każdego pokolenia.

Kod jest napisany w sposób czytelny, z komentarzami wyjaśniającymi działanie każdej funkcji, co ułatwia przyszłe modyfikacje.