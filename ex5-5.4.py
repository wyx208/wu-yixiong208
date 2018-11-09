def mulit(*args):
    res=args[0]
    for i in range(1,len(args)):
        res*=args[i]
    return res
