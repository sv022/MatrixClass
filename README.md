# MatrixClass
Class that implements simple methods of working with matrixes

## Class syntax:

### general methods
  >__A = Matrix(n, m)__  -->  creates a matrix object, size n x m 
  
  >__A.insert(value, i, j)__  -->  inserts the _value_ element into i<sub>th</sub> row, j<sub>th</sub> column
  
  >__A.show()__  -->  prints the matrix _A_ onto your screen
  
  >__A.copy()__  -->  creates a copy of matrix _A_
  
  >__A.fill()__  -->  allows you to fill the matrix with keyboard input, accepts n*m elements, where n, m - dimensions of the matrix. Elements should be inputed in lines, line by line from i = 1 to i = n.
  
 ### methods for calculus
 
 >__A.det()__  -->  return an _int_ value of _det A_
 
 >__A.min(i, j)__  -->  returns a minor of the element A<sub>ij</sub>
 
 >__A.ad(i, j)__  -->  returns a cofactor (algebraic addition) of the element A<sub>ij</sub>
 
 >__A.solve(list : b)__  -->  returns a solution to the linear equation system, where _A_ is a matrix of x coefficients, and _b_ is a __list__ of free components
 
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
