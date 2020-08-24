def MadMax(N, tele):
    my_list = [0]*N
    middle_of_list = int((N-1)/2)

    for j in range(0,middle_of_list):
        local_min = tele[j]
        for i in range(j,N):
            if tele[i] < local_min:
                local_min = tele[i]
                tele[j],tele[i]= tele[i], tele[j]
        my_list[j] = local_min
    for j in range(middle_of_list,N):
        local_max = tele[j]
        for i in range(j,N):
            if tele[i] > local_max:
                local_max = tele[i]
                tele[j],tele[i]= tele[i], tele[j]
        my_list[j] = local_max
    return my_list