import numpy

n1, m1 = [int(i) for i in input("Введите n, m").split()]
a = [[int(j) for j in input("Input a").split()] for i in range(n1)]


def check(a1, i, j, count, visited):
    visited[i][j] = 1
    if j + 1 < len(a1[0]):
        if a1[i][j + 1] == a1[i][j] and visited[i][j + 1] == 0:
            count += 1
            print(count)
            count = check(a1, i, j + 1, count, visited)
    if j - 1 >= 0:
        if a1[i][j - 1] == a1[i][j] and visited[i][j - 1] == 0:
            count += 1
            print(count)
            count = check(a1, i, j - 1, count, visited)
    if i - 1 >= 0:
        if a1[i - 1][j] == a1[i][j] and visited[i - 1][j] == 0:
            count += 1
            print(count)
            count = check(a1, i - 1, j, count, visited)
    if i + 1 < len(a1):
        if a1[i + 1][j] == a1[i][j] and visited[i + 1][j] == 0:
            count += 1
            print(count)
            count = check(a1, i + 1, j, count, visited)
    return count


def main(a):
    b = numpy.zeros(shape=(n1, m1))
    visited = numpy.zeros(shape=(n1, m1))
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j] = check(a, i, j, 0, visited)
            visited = numpy.zeros(shape=(n1, m1))
    print(b)
    return 0


main(a)
