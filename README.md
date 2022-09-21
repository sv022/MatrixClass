# MatrixClass
Class that implements simple methods of working with matrixes

## Class syntax:

### general methods
  >__A = Matrix(n, m)__  -->  creates a matrix object, size n x m 
  
  >__A.insert(value, i, j)__  -->  inserts the _value_ element into i<sub>th</sub> row, j<sub>th</sub> column
  
  >__A.show()__  -->  prints the matrix _A_ onto your screen
  
  >__A.copy()__  -->  creates a copy of matrix _A_
  
 ### methods for calculus
 
 >__A.det()__  -->  return an _int_ value of _det A_
 
 >__A.min(i, j)__  -->  returns a minor of the element A<sub>ij</sub>
 
 >__A.ad(i, j)__  -->  returns a cofactor (algebraic addition) of the element A<sub>ij</sub>
 
 >__A.solve(list : b)__  -->  returns a solution to the linear equation system, where _A_ is a matrix of x coefficients, and _b_ is a __list__ of free components
