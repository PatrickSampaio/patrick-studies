import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]

matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input().strip())
    matrix.append(matrix_t)

un_encoded_matrix = []
    
for j in range(0, len(matrix[0])):
    for i in range(0,len(matrix)):
        try:
            un_encoded_matrix.append(matrix[i][j])
        except:
            pass
        
print(re.sub(r"\w\W\w", "", ''.join(un_encoded_matrix)))
