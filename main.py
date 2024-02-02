import random
import tkinter as tk

def create_grid(rows, cols):
    """Create a new grid of the given size."""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def draw_grid(grid, canvas, tileSize):
    """Draw the grid to the console."""
    rows, cols = len(grid), len(grid[0])
    canvas.delete('all')
    for row in range(rows):
        for col in range(cols):
            color = 'black' if grid[row][col] else 'white'
            canvas.create_rectangle(col*tileSize, row*tileSize, (col+1)*tileSize, (row+1)*tileSize, outline=color, fill=color)

def count_neighbors(grid, row, col):
    """Count the number of live neighbors around the given cell."""
    rows, cols = len(grid), len(grid[0])
    return sum(grid[(row + i) % rows][(col + j) % cols]
               for i in range(-1, 2) for j in range(-1, 2)
               if (i, j) != (0, 0))

def update_grid(grid):
    """Update the grid for the next generation."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col]:
                new_grid[row][col] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[row][col] = 1 if neighbors == 3 else 0
    return new_grid

def next_generation(window, canvas, grid, tileSize, n_gen):
    draw_grid(grid, canvas, tileSize)
    new_grid = update_grid(grid)
    if new_grid == grid:
        n_gen=-1
    grid[:] = new_grid
    if n_gen>=0:
        window.after(200, lambda:next_generation(window, canvas, grid, tileSize, n_gen-1))

def run_game(rows=20, cols=20, generations=50, tileSize=10):
    """Run Conway's Game of Life."""
    window = tk.Tk()
    window.geometry("+0+0")
    canvas = tk.Canvas(window, width=cols*tileSize, height=rows*tileSize)
    canvas.pack()
    grid = create_grid(rows, cols)
    next_generation(window, canvas, grid, tileSize, generations)
    window.mainloop()

if __name__ == '__main__':
    run_game()