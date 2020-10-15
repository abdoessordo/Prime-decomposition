from collections import Counter

def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0: count +=1
    if count > 2 :return False
    else: return True  

def primeFactors(n):
    fact = []
    result = []
    a = n
    while a>1:
        for i in range(2,n+1):
            if isPrime(i) and a%i == 0:
                fact.append(i)
                a = a/i
                break
    
    counted = dict(Counter(fact))

    for num in counted:
        result.append("(")
        result.append(str(num))
        if(counted[num] > 1):
            result.append("^")
            result.append(str(counted[num]))
            result.append(")")
        else:
            result.append(")")

    return ''.join(result)
