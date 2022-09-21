class Matrix:
    def __init__(self, r, c) -> None:
        self.rw = r
        self.cl = c
        self.issquare = (r if r == c else -1)
        self.__items__ = [ [None for i in range(c + 1)] for j in range(r + 1) ]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.__items__[i][j] = 0
                
    def __getitem__(self, n):
        try:
            return self.__items__[n]
        except:
            raise AttributeError
    
    def insert(self, val, r, c):
        self.__items__[r][c] = val
    
    def show(self):
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                print(self.__items__[i][j], end=' ')
            print()
            
    def fill(self):
        print('Введите элементы матрицы построчно, каждый элемент с новой строки: ')
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                x = int(input())
                self.__items__[i][j] = x
            
    def copy(self):
        cp = Matrix(self.rw, self.cl)
        for i in range(1, cp.rw + 1):
            for j in range(1, cp.cl + 1):
                cp[i][j] = self[i][j]
        return cp

    # calculations stuff
    
    def min(self, r, c):
        M = Matrix(self.rw - 1, self.cl - 1)
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                if i == r or j == c:
                    continue
                if i > r:
                    if j > c:
                        M.insert(self[i][j], i - 1, j - 1)
                    else:
                        M.insert(self[i][j], i - 1, j)
                else:
                    if j > c:
                        M.insert(self[i][j], i, j - 1)
                    else:
                        M.insert(self[i][j], i, j)
        return M.det()
    
    def ad(self, r, c):
        return ((-1) ** (r + c)) * self.min(r, c)
    
    def det(self):
        if self.issquare == 1:
            return self.__items__[1][1]
        elif self.issquare == 2:
            return self[1][1] * self[2][2] - self[1][2] * self[2][1]
        elif self.issquare == 3:
            return self[1][1] * self[2][2] * self[3][3] + \
                self[2][1] * self[3][2] * self[1][3] + \
                self[1][2] * self[2][3] * self[3][1] - \
                self[1][3] * self[2][2] * self[3][1] - \
                self[1][1] * self[2][3] * self[3][2] - \
                self[1][2] * self[3][3] * self[2][1]
        else:
            s = 0
            for i in range(1, self.rw + 1):
                s += self[i][1] * self.ad(i, 1)
            return s
    
    def solve(self, b):
        res = []
        det = self.det()
        if det == 0: return "det A == 0, can't be solved"
        for i in range(1, self.rw + 1):
            d = self.copy()
            for j in range(1, self.cl + 1):
                d[j][i] = b[j - 1]
            # d.show()
            # self.show()
            res.append(d.det() / det)
        rs = ''
        for i in range(len(res)):
            rs += f'x{i + 1} = {res[i]} '
        return rs[:-1:]
