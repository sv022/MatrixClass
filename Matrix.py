class Matrix:
    def __init__(self, r, c, unitary=False) -> None:
        self.rw = r
        self.cl = c
        self.issquare = (r if r == c else -1)
        if self.issquare == -1 and unitary: raise Exception("Only square matrix can be unitary.")
        self.__items__ = [ [0 for i in range(c + 1)] for j in range(r + 1) ]
        if unitary:
            for i in range(1, r + 1):
                self.__items__[i][i] = 1

    def __getitem__(self, n):
        return self.__items__[n]
    
    def __add__(self, obj):
        if isinstance(obj, Matrix):
            if self.rw != obj.rw or self.cl != obj.cl: raise Exception('Can only add matrixes of similar sizes.')
            else:
                res = Matrix(self.rw, self.cl)
                for i in range(1, self.rw + 1):
                    for j in range(1, self.cl + 1):
                        res[i][j] = self[i][j] + obj[i][j]
            return res
        else: raise Exception('Can only add matrix to another matrix.')
    
    def __mul__(self, obj):
        if isinstance(obj, int) or isinstance(obj, float):
            res = Matrix(self.rw, self.cl)
            for i in range(1, self.rw + 1):
                for j in range(1, self.cl + 1):
                    res[i][j] = self[i][j] * obj
            return res
        elif isinstance(obj, Matrix):
            if self.cl != obj.rw: raise Exception('Unmatched matrixes dimensions.')
            ci = 1
            cj = 1
            res = Matrix(self.rw, obj.cl)
            while ci < self.cl:
                print(f'{ci=}, {cj=}')
                s = 0
                for i in range(1, self.cl + 1):
                    s += self[ci][i] * obj[i][cj]
                res[ci][cj] = s
                cj += 1
                if cj > obj.cl:
                    cj = 1
                    ci += 1
            return res
        raise TypeError('Can only multiply Matrix by int, or Matrix by Matrix.')

    def _extend(self):
        res = Matrix(self.rw + 1, self.cl + 1)
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                res[i][j] = self[i][j]
        return res
    
    def insert(self, val, r, c):
        self.__items__[r][c] = val
    
    def show(self):
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                print(self.__items__[i][j], end=' ')
            print()
            
    def fill(self, *args):
        try: 
            a = args[0]
            if a and (isinstance(a, list) or isinstance(a, tuple)):
                if len(a) < self.rw * self.cl: raise BaseException('Iterable is too short for this matrix.')
                k = 0
                crow = 1
                ccol = 1
                while k < self.rw * self.cl:
                    self[crow][ccol] = a[k]
                    ccol += 1
                    k += 1
                    if ccol == self.cl + 1:
                        ccol = 1
                        crow += 1
                return
            elif a:
                raise BaseException('Can only fill matrix with List / Tuple.')
        except IndexError: pass
        except Exception: return

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
    
    def items(self):
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                yield self[i][j]

    # calculations stuff
    
    def transpose(self):
        res = Matrix(self.cl, self.rw)
        for i in range(1, self.rw + 1):
            for j in range(1, self.cl + 1):
                res[j][i] = self[i][j]
        return res
    
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
    
    def solve(self, b, raw=False):
        res = []
        det = self.det()
        if det == 0: return {1 : [], 0 : "det A = 0, can't be solved."}[int(raw)]
        for i in range(1, self.rw + 1):
            d = self.copy()
            for j in range(1, self.cl + 1):
                d[j][i] = b[j - 1]
            # d.show()
            # self.show()
            res.append(d.det() / det)
        if raw: return res
        else:
            rs = ''
            for i in range(len(res)):
                rs += f'x{i + 1} = {res[i]} '
            return rs[:-1:]
