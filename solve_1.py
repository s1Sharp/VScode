def squirrel(n):
    x=n
    result = 1
    while x > 1:
        result *= x
        x+=-1
    print (result)
    while result > 10:
        result = result // 10
    return result
