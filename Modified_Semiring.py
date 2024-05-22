import secrets


def pro(x, y, c):
    return [min(c + x[0] + y[0], c + x[1] + y[1]), min(c + x[0] + y[1],c +  x[1] + y[0])]

def add(x, y):
    return [min(x[0], y[0]) , min(x[1], y[1]) ]

def multiply_matrices(matrix1, matrix2, c):
    n = len(matrix1)
    if len(matrix2) != n:
        raise ValueError("The number of rows in matrix1 must be equal to the number of rows in matrix2.")
    result = [[(float('inf'), float('inf')) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = add(result[i][j], pro(matrix1[i][k], matrix2[k][j],c))
    return result

def sum(x,y):
    return [x[0]+y[0],x[1]+y[1]]

def add_constant(matrix, c):
    n = len(matrix)
    result = [[sum(matrix[i][j],[c, c]) for j in range(n)] for i in range(n)]
    return result

def matrix_power(matrix, n, c):
    if n <= 0:
        raise ValueError("The power 'n' must be a positive integer.")
    if n == 1:
        return matrix
    result = matrix
    for _ in range(n - 1):
        result = multiply_matrices(result, matrix, c)
    return result

def sub(x,y):
    S = [[[0,0] for _ in range(len(x))] for _ in range(len(y))]
    for i in range(len(x)):
        for j in range(len(y)):
            S[i][j][0] = x[i][j][0]-y[i][j][0]
            S[i][j][1] = x[i][j][1]-y[i][j][1]
    return S

def sum_matrix(x,y):
    S = [[[0,0] for _ in range(len(x))] for _ in range(len(y))]
    for i in range(len(x)):
        for j in range(len(y)):
            S[i][j][0] = x[i][j][0]+y[i][j][0]
            S[i][j][1] = x[i][j][1]+y[i][j][1]
    return S

def constant_matrix(matrix):
    constant_value = matrix[0][0]
    for row in matrix:
        for element in row:
            if element != constant_value:
                return 0
    return 1           
          
def find_exponent(X,Y,A,lim = 20):
    AB = [[[0,0] for _ in range(lim)] for _ in range(lim)]
    for i in range(lim):
        for j in range(lim):
            AB[i][j] = sub(A,multiply_matrices(matrix_power(X,i+1,0),matrix_power(Y,j+1,0),0))
            T = constant_matrix(AB[i][j])
            [k,l] = [0,0]
            if T == 1:
                k = i+1
                l = j+1
                return [k,l]
    return [1,1]            
                
            
def generate_X_Y(order=2, x_min=-10**2, x_max=10**2, y_min=-10**2, y_max=10**2):
    X = [[[secrets.randbelow((x_max - x_min) + 1) + x_min,secrets.randbelow((x_max - x_min) + 1) + x_min] for i in range(order)] for j in range(order)]
    Y = [[[secrets.randbelow((y_max - y_min) + 1) + y_min,secrets.randbelow((y_max - y_min) + 1) + y_min] for i in range(order)] for j in range(order)]
    return X, Y

def randomise(x_min=-10**2, x_max=10**2):
    x = secrets.randbelow((x_max - x_min) + 1)
    return x

def generate_exponent(x_min=1, x_max=10**3):
    x = secrets.randbelow((x_max - x_min) + 1) 
    return x

