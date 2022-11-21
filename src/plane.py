class Plane:

    def __init__(self, length):
        self.length = length
        self.__activate_cells()
        super().__init__()

    def __activate_cells(self):
        self.__plane = []
        for i in range(self.length):
            col = []
            for j in range(self.length):
                col.append('_')
            self.__plane.append(col)

    def printInstance(self):
        for col in self.__plane:
            for i in col:
                print(i, end=' ')
            print()

    def markCell(self, row, col, mode):
        if(self.length < row or self.length < col):
            raise Exception(f"{row} {col} is not inside plane")

        # checking if the point is already taken
        if(not self.cellIsEmpty(row, col)):
            raise Exception(f"{row} {col} is already taken")

        row -= 1
        col -= 1

        self.__plane[row][col] = 'X' if mode == "bot" else 'O'

    def clearCell(self, row, col):
        if(self.length < row or self.length < col):
            return "Invalid Move"
        row -= 1
        col -= 1
        self.__plane[row][col] = '_'

    def cellIsEmpty(self, row, col):
        return self.__plane[row-1][col-1] == '_'

    def isComplete(self):
        plane = self.__plane

        # checking column wise
        for col in plane:
            if(col.count(col[0]) == len(col)) and col[0] != '_':
                return col[0] == 'X'

        # generating rows
        rows = []
        for col in plane:
            for i in range(len(col)):
                if(col is plane[0]):
                    rows.append([col[i]])
                else:
                    rows[i].append(col[i])

        # checking for rows
        for row in rows:
            if(row.count(row[0]) == len(row)) and row[0] != '_':
                return row[0] == 'X'

        # generating diagonals
        diagonals = [[], []]
        for i in range(len(plane)):
            n = len(plane)-1
            diagonals[0].append(plane[i][n-i])
            diagonals[1].append(plane[n-i][n-i])

        # checking for diagonals
        for diagonal in diagonals:
            if(diagonal.count(diagonal[0]) == len(diagonal)) and diagonal[0] != '_':
                return diagonal[0] == 'X'

        for col in plane:
            if('_' in col):
                return None

        return 'DRAW'
