def squirrel(n):
    x=n
    result = 1
    while x > 1:
        result *= x
        x+=-1
    return int(str(result)[0])
