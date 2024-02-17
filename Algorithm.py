import time
import math
def generatePrime(n): #generates the first n primes
    X = 0
    i = 2
    out = []
    while (X < n):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i % j == 0):
                flag = False
                break
        if (flag):
            out.append(i)
            X += 1
        i += 1
    return out
def SmallestPrimeFactor(N_max): #finds the smallest prime factor of all numbers between 1 and N_max
    output = [i for i in range(0,N_max+1)]
    for i in range(2,N_max+1,2):
        output[i] = 2
    for j in range(3,int(N_max**0.5)+1,2):
        if output[j] == j:
            for k in range(j * j, N_max+1,j):
                if output[k] == k:
                    output[k] = j
    return output
def PrimeFactor(n): #Finds a fully ungrouped prime factorization of n
    out = []
    x = SmallestPrimeFactor(n)
    while (n > 1):
        out.append(x[n])
        n = int(n/x[n])
    return out[::-1]
def MinNumFactor(n,factored = True): #Returns the smallest number with n factors
    out = PrimeFactor(n) #first guess:prime factorization of n as the powers of each prime
    #e.g 40 = 2*2*2*5 --> initial guess is 2^4*3*5*7
    length = len(out)
    prime_list = generatePrime(length)
    if length >= 2: #if 2 or less primes are involved, the initial guess will always be correct
        log_primes = [math.log(x) for x in prime_list]
        for j in reversed(range(int(length/2),length)):
            checking_list = [a * b for a,b in zip(out, log_primes)] #conversion to logarithms to make the math easier
            k = out[j]-1
            minimal = checking_list[j] - log_primes[j]
            count = 0
            for i in range(0,j): #checking step to see if there is a more efficient factorization
                if minimal > k*checking_list[i]:
                    count = i
                    minimal = k*checking_list[i]
            if minimal != checking_list[j]-log_primes[j]: #updating list
                out[count] += k*out[count]
                del out[j]
                del log_primes[j]
    if factored:
        return out
    else:
        c = 1
        for i in range(len(out)):
            c = c*prime_list[i]**(out[i]-1)
        return c
t0 = time.time()
n = 1000000
print(f"The smallest number with {n} factors is {MinNumFactor(n,False)}")
t1 = time.time()
print(f"Time Taken: {round((t1-t0)*1000,8)} milliseconds")
