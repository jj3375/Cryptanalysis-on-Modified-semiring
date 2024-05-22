from Modified_Semiring import multiply_matrices
from Modified_Semiring import matrix_power
from Modified_Semiring import sub
from Modified_Semiring import sum_matrix
from Modified_Semiring import find_exponent
import Protocol
import time

X = Protocol.X
Y = Protocol.Y
Ap = Protocol.Ap
Bq = Protocol.Bq
start = time.time()
[k,l] = find_exponent(X,Y,Ap)
[r,s] = find_exponent(X,Y,Bq)
D1 = multiply_matrices(matrix_power(X,k+r,0),matrix_power(Y,l+s,0),0)
D2_1 = multiply_matrices(matrix_power(X,k,0),matrix_power(Y,l,0),0)
D2_2 = multiply_matrices(matrix_power(X,r,0),matrix_power(Y,s,0),0)
D2 = multiply_matrices(D2_1,D2_2,0)
D = sub(D1,D2)
Key = sum_matrix(multiply_matrices(Ap,Bq,0),D)
end = time.time()
Time_taken = end - start
print("\nThe recovered exponents are :")
print("k = "+str(k))
print("l = "+str(l))
print("r = "+str(r))
print("s = "+str(s))
print("\nThe recovered secret key is :")
print(Key)
print("\nThe time taken to attack the secret key :")
print(str(Time_taken) + " seconds")
if Protocol.Alice_key == Key:
    print("\nAttack Successful")
else:
    print("Attack failed")    