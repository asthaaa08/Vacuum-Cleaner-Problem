class VacuumCleaner:
    def __init__(self, grid_size):
        
        self.grid_size = grid_size
        
        self.grid = [['dirty' for _ in range(grid_size)] for _ in range(grid_size)]
        self.position = (0, 0)

    def display_grid(self):
        for row in self.grid:
            print(row)

    def clean(self):
        if self.grid[self.position[0]][self.position[1]] == 'dirty':

            print("Cleaning the current cell...")
            self.grid[self.position[0]][self.position[1]] = 'clean'

    def move(self, direction):
        x, y = self.position
        if direction == 'left' and y > 0:

            self.position = (x, y - 1)
        elif direction == 'right' and y < self.grid_size - 1:
            self.position = (x, y + 1)
        elif direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < self.grid_size - 1:
            self.position = (x + 1, y)
        else:
            print("Invalid move!")

    def is_clean(self):
        for row in self.grid:
            if 'dirty' in row:
                return False
        return True

if __name__ == "__main__":
    grid_size = int(input("Enter the size of the grid: "))

    vacuum = VacuumCleaner(grid_size)

    while not vacuum.is_clean():
        vacuum.clean()
        
        print("\nCurrent grid status:")
        vacuum.display_grid()

        print("\nVacuum cleaner position:", vacuum.position)

        action = input("\nEnter action (left/right/up/down/exit): ").lower()

        if action == 'exit':

            print("Exiting...")
            break
        elif action in ['left', 'right', 'up', 'down']:

            vacuum.move(action)
        else:

            print("Invalid action!")

    print("Cleaning complete! Final grid status:")

    vacuum.display_grid()
