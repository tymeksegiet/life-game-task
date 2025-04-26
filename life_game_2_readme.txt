Oto nowa implementacja gry w życie w Pythonie, napisana od podstaw, z zachowaniem czytelności i jasności kodu:

```python
import time

def calculate_neighbors(grid, x, y):
    """
    Oblicza liczbę żywych sąsiadów dla komórki na pozycji (x, y).
    """
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])

    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx][ny]

    return count

def update_grid(grid):
    """
    Tworzy nową planszę na podstawie aktualnego stanu zgodnie z zasadami gry w życie.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for x in range(rows):
        for y in range(cols):
            live_neighbors = calculate_neighbors(grid, x, y)
            if grid[x][y] == 1:
                # Komórka żywa pozostaje żywa, jeśli ma 2 lub 3 żywych sąsiadów
                new_grid[x][y] = 1 if live_neighbors in (2, 3) else 0
            else:
                # Komórka martwa staje się żywa, jeśli ma dokładnie 3 żywych sąsiadów
                new_grid[x][y] = 1 if live_neighbors == 3 else 0

    return new_grid

def print_grid(grid):
    """
    Wyświetla planszę w formie tekstowej.
    'x' oznacza żywą komórkę, '.' oznacza martwą komórkę.
    """
    for row in grid:
        print(''.join('x' if cell else '.' for cell in row))
    print()

def game_of_life_simulation(initial_grid, generations):
    """
    Symuluje grę w życie dla zadanej liczby pokoleń.
    Wyświetla planszę i mierzy czas obliczeń dla każdego pokolenia.
    """
    current_grid = initial_grid

    for gen in range(1, generations + 1):
        print(f"Pokolenie {gen}:")
        print_grid(current_grid)

        start_time = time.time()
        current_grid = update_grid(current_grid)
        end_time = time.time()

        print(f"Czas obliczeń: {end_time - start_time:.6f} sekund\n")

# Przykładowa plansza początkowa
initial_grid = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Uruchomienie symulacji na 5 pokoleń
game_of_life_simulation(initial_grid, 5)
```

### Wyjaśnienie:
1. **`calculate_neighbors`**: Oblicza liczbę żywych sąsiadów dla danej komórki, iterując po jej sąsiadach.
2. **`update_grid`**: Tworzy nową planszę na podstawie zasad gry w życie.
3. **`print_grid`**: Wyświetla planszę w formie tekstowej, używając `x` dla żywych komórek i `.` dla martwych.
4. **`game_of_life_simulation`**: Zarządza symulacją, wyświetla planszę i mierzy czas obliczeń dla każdego pokolenia.