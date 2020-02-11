n1,m1=[int(i) for i in input("Введите n1, m1").split()]
a = [[int(j) for j in input().split()] for i in range(n1)]
n2,m2=[int(i) for i in input("Введите n1, m1").split()]
b = [[int(j) for j in input().split()] for i in range(n2)]


def check(a,b,i,j):
    for i1 in range(len(b)):
        for j1 in range(len(b[0])):
            if not a[i1+i][j1+j] == b[i1][j1]:
                return 0


for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==b[0][0]:
            check(a,b,i,j)
