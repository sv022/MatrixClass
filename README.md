# MatrixClass
Class that implements simple methods of working with matrixes.

Supports matrix addition, multiplication and several other methods.

## Class syntax:

### general methods
  >__A = Matrix(n, m, unitary=False)__  -->  creates a matrix object, size n x m. Set `unitary` to ***True*** to get unitary (identity) matrix. If set to ***True***, throws in Exception if the matrix is not square.
  
  >__A.insert(value, i, j)__  -->  inserts the `value` element into i<sub>th</sub> row, j<sub>th</sub> column.
  
  >__A.show()__  -->  prints the matrix `A` onto your screen.
  
  >__A.copy()__  -->  creates a copy of matrix `A`.
  
  >__A.items()__  -->  returns an iterator over all the objets of the matrix `A` going by rows.
  
  >__A.fill(a)__  -->  allows you to fill the matrix with an iterable object `a` (List / Tuple), or with keyboard input. For iterables: if the length of the given iterable is bigger than n*m, (n, m - dimensions of the matrix), method will only take first n*m elements of the iterable, dumping the rest of the iterable. Throws in Exception if the lenght of the iterable is less than n*m.
 
!  For keyboard input leave function parameters empty  !
  
 ### methods for calculus
 
 >__A.det()__  -->  returns an _int_ value of _det A_.
 
 >__A.transpose()__  -->  returns a transposed matrix `A`.
 
 >__A.min(i, j)__  -->  returns a minor of the element A<sub>ij</sub>.
 
 >__A.ad(i, j)__  -->  returns a cofactor (algebraic addition) of the element A<sub>ij</sub>.
 
 >__A.solve(list : b, (default)raw=False)__  -->  returns a solution to the linear equation system, where `A` is a matrix of x coefficients, and `b` is a __list__ of free components. Set argument `raw` to ***True*** to get results as a list of integers rather than a formatted string.
 
 ## Usage notes 
 
 You can import a python class from different file by adding 
```
from <filename> import <classname>
```
this will allow you to use the given class within you file without having to copy and paste it.

import line for this particular class:
```
from Matrix import Matrix
```
