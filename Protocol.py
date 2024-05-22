from Modified_Semiring import multiply_matrices
from Modified_Semiring import add_constant
from Modified_Semiring import matrix_power
from Modified_Semiring import generate_X_Y 
from Modified_Semiring import randomise
from Modified_Semiring import generate_exponent
import time

start = time.time()

X,Y = generate_X_Y() 
c = randomise()
k = generate_exponent() 
l = generate_exponent()
p = randomise()
d = randomise()
r = generate_exponent() 
s = generate_exponent()
q = randomise()

Xk = matrix_power(X, k, c)
Yl = matrix_power(Y, l, c)
A = multiply_matrices(Xk,Yl,0)
Ap = add_constant(A,p)
Xk_p = add_constant(Xk,p)

Xr = matrix_power(X, r, d)
Ys = matrix_power(Y, s, d)
B = multiply_matrices(Xr,Ys,0)
Bq = add_constant(B,q)
Xr_q = add_constant(Xr,q)

Alice_key = multiply_matrices(Xk_p,multiply_matrices(Bq,Yl,0),0)

Bob_key = multiply_matrices(Xr_q,multiply_matrices(Ap,Ys,0),0)

end = time.time()

Time_taken = end - start

print("The following are the generated public parameters\n")
print("X = " + str(X))
print("Y = " + str(Y))
print("\nThe private parameters of Alice are:\n")
print("c = " + str(c))
print("k = " + str(k))
print("l = " + str(l))
print("p = " + str(p))
print("\nThe private parameters of Bob are:\n")
print("d = " + str(d))
print("r = " + str(r))
print("s = " + str(s))
print("q = " + str(q))
print("\nThe public matrix A_p :")
print("A_p = " + str(Ap))
print("\nThe public matrix B_q :")
print("B_q = " + str(Bq))
print("\nThe Secret key of Alice :")
print("Alice key = " + str(Alice_key))
print("\nThe Secret key of Bob :")
print("Bob key = " + str(Bob_key))

print("\nThe time taken to generate the secret key :")
print(str(Time_taken) + " seconds")
