from random import randint

def print_matrix(C):
    for row in C:
        for n in row:
            print(f'{n:4d}', end='')
        print()
    print()


def row_sum(row):
    return sum(n for n in row if n < 0 and not n & 1)


n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))
a = [[randint(-5, 5) for j in range(m)] for i in range(n)]


def firstNull1(matrix):
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            if (matrix[j][i] == 0):
                print('Первый столбец с нулём ', i + 1)
                return
            else:
                k += 1
            if (k == n * m):
                print('нет нулей')


print_matrix(a)
firstNull1(a)

a.sort(reverse=True, key=row_sum)
print("Упорядоченная таблица: ")
print_matrix(a)
