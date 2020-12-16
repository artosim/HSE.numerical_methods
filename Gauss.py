import numpy as np



def gauss(M, b):
    # Прямой ход
    for k in range(M.shape[0] - 1):
        # Тут Частичный выбор главного элемента (т.е. каждый раз на месте kk наибольший по модулю элемент,
        #                                           переставляю только строки)
        index_max = np.where(abs(M[k:, k]) == max(abs(M[k:, k])))[0][0] + k
        if index_max != k:
            str1 = np.copy(M[k])
            str2 = np.copy(M[index_max])
            M[k], M[index_max] = str2, str1
            b[k], b[index_max] = b[index_max], b[k]
        # Построчно выбираю с на которое делить
        for i in range(k + 1, M.shape[0]):
            c = -1 * M[i][k] / M[k][k]
            # Меняю элементы
            for j in range(k, M.shape[0]):
                M[i][j] += c * M[k][j]
            b[i] += c * b[k]

    answer = np.zeros(M.shape[0])  # Тут сохраняю иксы

    # Обратный ход
    n = M.shape[0] - 1
    answer[n] = b[n] / M[n][n]
    for k in range(M.shape[0] - 2, -1, -1):
        sum_Ux = 0
        for i in range(k+1, M.shape[0]):
            sum_Ux += M[k][i] * answer[i]
        result = b[k] - sum_Ux
        answer[k] = result / M[k][k]

    return answer


# M = np.array([[4., 2., 1.],
#               [7., 8., 9.],
#               [9., 1., 3.]])
# b = np.array([1.,1.,2.])
M = np.array([[1., 2., 3., -2.],
              [2., -1., -2., -3.],
              [3., 2., -1., 2.],
              [2., -3., 2., 1.]])
b = np.array([1.,2.,-5.,11.])

print(gauss(M, b))