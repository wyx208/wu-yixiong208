def isNum(n):
    n=type(eval(n))
    if n==type(1):
        return True
    elif n==type(1,0):
        return True
    elif n==type(1+1j):
        return True
    else:
        return False
isNum(input("输入:"))
