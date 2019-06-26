from copy import deepcopy

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)


class Grid:
    def __init__(self, size = 4):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)]

    # Make a Deep Copy of This Object||将齐聚进行复制（deep
    def clone(self):
        gridCopy = Grid()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size

        return gridCopy

    # Insert a Tile in an Empty Cell||进行赋值
    def insertTile(self, pos, value):
        self.setCellValue(pos, value)

    def setCellValue(self, pos, value):
        self.map[pos[0]][pos[1]] = value

    # Return All the Empty c\Cells||返回所有的空的位置（值为零）
    def getAvailableCells(self):
        cells = []

        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 0:
                    cells.append((x,y))

        return cells

    # Return the Tile with Maximum Value||返回棋局的最大值
    def getMaxTile(self):
        maxTile = 0

        for x in range(self.size):
            for y in range(self.size):
                maxTile = max(maxTile, self.map[x][y])

        return maxTile

    # Check If Able to Insert a Tile in Position||查看木一个点师傅可以插入
    def canInsert(self, pos):
        return self.getCellValue(pos) == 0

    # Move the Grid||移动棋局
    def move(self, dir):
        dir = int(dir)

        if dir == UP:
            return self.moveUD(False)##上=0
        if dir == DOWN:
            return self.moveUD(True)##下=1
        if dir == LEFT:
            return self.moveLR(False)##左边=0
        if dir == RIGHT:
            return self.moveLR(True)##右边=1

    # Move Up or Down||上下移动
    def moveUD(self, down):
        r = range(self.size -1, -1, -1) if down else range(self.size)
         ##下的时候（3,2,1,0）||上的时候（0，1,2,3）
        moved = False

        for j in range(self.size):
            cells = []                    ##将每一列的非零元素放到cells中

            for i in r:
                cell = self.map[i][j]

                if cell != 0:
                    cells.append(cell)

            self.merge(cells)

            for i in r:                    ##将合并之后的一列放进去
                value = cells.pop(0) if cells else 0

                if self.map[i][j] != value:
                    moved = True

                self.map[i][j] = value

        return moved

    # move left or right
    def moveLR(self, right):##同上下
        r = range(self.size - 1, -1, -1) if right else range(self.size)

        moved = False

        for i in range(self.size):
            cells = []

            for j in r:
                cell = self.map[i][j]

                if cell != 0:
                    cells.append(cell)

            self.merge(cells)

            for j in r:
                value = cells.pop(0) if cells else 0

                if self.map[i][j] != value:
                    moved = True

                self.map[i][j] = value

        return moved

    # Merge Tiles||一行或者一列元素合并，方向有cells中的顺序确定
    def merge(self, cells):
        if len(cells) <= 1:
            return cells

        i = 0

        while i < len(cells) - 1:
            if cells[i] == cells[i+1]:
                cells[i] *= 2

                del cells[i+1]

            i += 1

    def canMove(self, dirs = vecIndex):
        ##vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)
        ##||检索一个点是否可以和周边的点合并，包括和0合并

        # Init Moves to be Checked
        checkingMoves = set(dirs)    ##比如等于{0,1,2,3}

        for x in range(self.size):
            for y in range(self.size):

                # If Current Cell is Filled
                if self.map[x][y]:

                    # Look Ajacent Cell Value
                    for i in checkingMoves:
                        move = directionVectors[i]
##directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
                        adjCellValue = self.getCellValue((x + move[0], y + move[1]))

                        # If Value is the Same or Adjacent Cell is Empty
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True

                # Else if Current Cell is Empty
                elif self.map[x][y] == 0:
                    return True

        return False

    # Return All Available Moves||返回所有可以移动的方向
    def getAvailableMoves(self, dirs = vecIndex):##vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)
        availableMoves = []

        for x in dirs:
            gridCopy = self.clone()

            if gridCopy.move(x):
                availableMoves.append(x)

        return availableMoves

    def crossBound(self, pos):##一些超出边线 的下标
        return pos[0] < 0 or pos[0] >= self.size or pos[1] < 0 or pos[1] >= self.size

    def getCellValue(self, pos):
        if not self.crossBound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None

if __name__ == '__main__':
    g = Grid()
    g.map[0][0] = 2
    g.map[1][0] = 2
    g.map[3][0] = 4

    while True:
        for i in g.map:
            print(i)

        print(g.getAvailableMoves())

        v = input()

        g.move(v)
