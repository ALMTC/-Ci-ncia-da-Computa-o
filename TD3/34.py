m1 = []
DiagonalP = []
DiagonalS = []
for i in range(5):
    m1.append([])
    for j in range(5):
        print 'Digite o elemento', i, 'x', j
        m1[i].append(input())
for i in range(4):
    for j in range(i+1,5):
        DiagonalP.append(m1[i][j])
for i in range(1,5):
    for j in range(5-i,5):
        DiagonalS.append(m1[i][j])
print DiagonalS