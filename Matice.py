class Matice:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._matrix = [[0] * self._columns for _ in range(self._rows)]

    @property
    def rows(self) -> int:
        return self._rows

    @rows.setter
    def rows(self, row: int):
        if row < 0:
            raise ValueError("Invalid row coordinate!")
        self._rows = row

    @property
    def columns(self) -> int:
        return self._columns

    @columns.setter
    def columns(self, col: int):
        if col < 0:
            raise ValueError("Invalid col coordinate!")
        self._columns = col

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, m):
        self._matrix = m

    def set_value(self, row: int, col: int, value):
        if row < 0 or row >= self._rows or col < 0 or col >= self._columns:
            raise ValueError("Invalid row or column coordinates!")
        self._matrix[row][col] = value

    def get_value(self, row: int, col: int):
        if row < 0 or row >= self._rows or col < 0 or col >= self._columns:
            raise ValueError("Invalid row or column coordinates!")
        return self._matrix[row][col]

    def get_values_count(self, value=None) -> int:
        if value is None:
            return self._rows * self._columns - self.get_empty_values_count()
        return sum(row.count(value) for row in self._matrix)

    def get_empty_values_count(self) -> int:
        return sum(row.count(0) for row in self._matrix)

    def __contains__(self, value):
        return any(value in row for row in self._matrix)

    def get_pocet_radku(self) -> int:
        return self._rows

    def get_pocet_sloupcu(self) -> int:
        return self._columns

    def transponovat(self):
        self._rows, self._columns = self._columns, self._rows
        self._matrix = [list(row) for row in zip(*self._matrix)]
