import numpy as np

a = np.random.random((3,3))
print(f'Исходная матрица 3х3:\n{a}')
a = a.transpose()
print(f'Транспонированная матрица:\n{a}')