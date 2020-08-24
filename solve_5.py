def SynchronizingTables( N, ids, salary):
    current_id = [0]*N
    result = [0]*N
    ids_local_min = max(ids)
    ids_prev_local_min = 0
    for i in range(N):
        for k in range(N):
            if ids[k] < ids_local_min and ids[k] > ids_prev_local_min:
                ids_local_min = ids[k]
                current_id[i] = k
        ids_prev_local_min = ids_local_min
        ids_local_min = max(ids) + 1
    for i in range(N-1):
        for j in range(N-i-1):
            if salary[j] > salary[j+1]:
                salary[j], salary[j+1] = salary[j+1], salary[j]
    for i in range(N):
        result[current_id[i]] = salary [i]
    return result
