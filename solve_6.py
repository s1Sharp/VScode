def PatternUnlock(N, hits):
    mas = [ [6 , 1 , 9],
            [5 , 2 , 8],
            [4 , 3 , 7]]
    for k in range(3):
        for j in range(3):
            if  mas[k][j] == hits[0]:
                prevk = k
                prevj = j
    inrange = 0.0
    different = 0.0
    for i in range(1,N):
        for k in range(3):
            for j in range(3):
                if mas[k][j] == hits[i]:
                    different = abs(prevk - k) + abs(prevj - j)
                    inrange += round(pow(different,0.5),10)
                    prevk = k ; prevj = j
    inrange = round(inrange,5)
    solve = 0
    inrange *=100000
    inrange = int(round(inrange))
    localconst = 1
    while inrange//10 > 1:
        solve += localconst * (inrange % 10)
        if inrange % 10 !=0:
            localconst *=10
        inrange = inrange // 10
    solve += inrange*localconst
    strsolve = str(solve)
    return solve