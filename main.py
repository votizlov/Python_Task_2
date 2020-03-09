n1, m1 = [int(i) for i in input("Введите n1, m1").split()]
a = [[int(j) for j in input("Input a").split()] for i in range(n1)]
n2, m2 = [int(i) for i in input("Введите n2, m2").split()]
b = [[int(j) for j in input("input b").split()] for i in range(n2)]


def check(a, b, i, j):
    for i1 in range(len(b)):
        for j1 in range(len(b[0])):
            if not a[i1 + i][j1 + j] == b[i1][j1]:
                return 0
    return 1


def main(a, b):
    if len(a) >= len(b) or len(a[0]) >= len(b[0]):
        for i in range(len(b)):
            for j in range(len(b[0])):
                if a[i][j] == b[0][0]:
                    if check(a, b, i, j):
                        print(i,j)
    return 0


main(a, b)
