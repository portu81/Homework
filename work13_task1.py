import random

def create_matrix(X, Y): # Функция для создания матрицы 10x10 со случайными числами
    return [[random.randint(-200, 200) for i in range(Y)] for i in range(X)]


def sum_matrices(matrix1, matrix2): # Функция для сложения двух матриц
    return [[matrix1[x][y] + matrix2[x][y] for y in range(len(matrix1[0]))] for x in range(len(matrix1))]


matrix_1 = create_matrix(10, 10) # Создаем две матрицы 10x10
matrix_2 = create_matrix(10, 10)

matrix_3 = sum_matrices(matrix_1, matrix_2) # Складываем матрицы

print("        Matrix 1 =") # Вывод результатов
for x in matrix_1:
    print(*x)

print("        Matrix 2 =")
for x in matrix_2:
    print(*x)

print("        Matrix 3 =")
for x in matrix_3:
    print(x)
