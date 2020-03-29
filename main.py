import numpy

n1, m1 = [int(i) for i in input("Введите n, m").split()]
a = [[int(j) for j in input("Input a[" + str(i) + "]").split()] for i in range(n1)]


def main(a):
    b = numpy.zeros(shape=(n1, m1))
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[j][i] = a[i][j]
    print(b)
    return 0


main(a)
