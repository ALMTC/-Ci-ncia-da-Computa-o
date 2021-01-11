m1 = []
DiagonalP = []
DiagonalS = []
for i in range(5):
    m1.append([])
    for j in range(5):
        print 'Digite o elemento', i, 'x', j
        m1[i].append(input())
        if i == j:
            DiagonalP.append(m1[i][j])
for i in range(5):
    DiagonalS.append(m1[i][5 - 1 - i])
print 'Doagonal principal:', DiagonalP
print 'Diagonal secundaria:', DiagonalS
print m1[0]
print m1[1]
print m1[2]
print m1[3]
print m1[4]
