class Matrix:
    def __init__(self, matrix_string):
        # create nested lists using \n and whitespace as delimiters
        string_grid = [s.split() for s in matrix_string.split('\n')]
        # convert grid of strings to grid of ints
        self.grid = [[int(val) for val in row] for row in string_grid]
        
    def row(self, index):
        # adjust index
        index -= 1
        return self.grid[index]

    def column(self, index):
        # adjust index
        index -= 1
        return [row[index] for row in self.grid]
