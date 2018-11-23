def isPrime(x):
    for i in range(2,x):
        if x % i ==0:
            return False
            break
    else:
        return True
while True:
    try:
        n = eval(input("Enter an Integer: "))
    except:
        print("Enter error! Please enter again: ")
        continue
    
    if type(n) is not int:
        print("Please enter an Integer: ")
        continue
    if n == -1:
        break
        
    if isPrime(n):
        print("{} is prime.".format(n))
    else:
        print("{} is not prime.".format(n))

