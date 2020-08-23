def squirrel(x):
    n=x
    result = 1
    while n > 1:
        result *=n
        n+=-1
    return int(str(result)[0])
