def ConquestCampaign( N, M, L, battalion):
    days = 1
    matrx = [ [ 0 for i in range(M) ] for j in range(N) ]
    num_of_L = 0
    for num_of_L in range (0,L+1,2):
        matrx[battalion[num_of_L]-1][battalion[num_of_L+1]-1] = 1
        num_of_L += 2
    while (min(min(matrx))) < 1:
        new_matrx = [ [ 0 for i in range(M) ] for j in range(N) ]
        for i in range(N):
            for j in range(M):
                if matrx[i][j] > 0:
                    new_matrx[i][j] = 2
                    if j+1 < M and new_matrx[i][j+1] < 2:
                        new_matrx[i][j+1] = 1
                    if i+1 < N and new_matrx[i+1][j] < 2:
                        new_matrx[i+1][j] = 1
                    if j-1 > -1 and new_matrx[i][j-1] < 2:
                        new_matrx[i][j-1] = 1
                    if i-1 > -1 and new_matrx[i-1][j] < 2:
                        new_matrx[i-1][j] = 1
        days +=1
        matrx = new_matrx
    return days

