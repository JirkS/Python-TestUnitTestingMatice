class Matice:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(rows)]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def get_value(self, row, col):
        return self.matrix[row][col]

    def get_values_count(self, value=None):
        if value is None:
            return self.rows * self.columns - self.get_empty_values_count()
        return sum(row.count(value) for row in self.matrix)

    def get_empty_values_count(self):
        return sum(row.count(0) for row in self.matrix)

    def __contains__(self, value):
        return any(value in row for row in self.matrix)

    def get_pocet_radku(self):
        return self.rows

    def get_pocet_sloupcu(self):
        return self.columns

    def transponovat(self):
        self.rows, self.columns = self.columns, self.rows
        self.matrix = [list(row) for row in zip(*self.matrix)]
