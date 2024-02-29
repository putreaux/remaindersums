import matplotlib.pyplot as plt
import numpy as np
import sys
import math

n = sys.argv[1]
subtract_slope = int(sys.argv[2])

n = int(n)



def isprime(num):
    sqroot = math.ceil(math.sqrt(num))
    for i in range(2, sqroot+1):
        if num % i == 0:
            return False
    return True

def calculate_sums(n):
    sums = [0,0]
    primesums = [0,0]
    primecount = 0
    additioncount = 0
    for i in range(2,n):
        sum1 = 0
        sum2 = 0
        prime = False
        if isprime(i):
            prime = True
        for j in range(2,i):
            fr0 = i/j
            fr = math.floor(fr0)
            rem = fr0-fr
            sum1 += rem
            if prime:
                sum2 += rem
                primecount += 1
            additioncount += 1
        sums.append(sum1)
        primesums.append(sum2)
    return sums, primesums, primecount, additioncount



if __name__ == "__main__":
    sums, primesums, primecount, additioncount = calculate_sums(n)
    sumsum = sum(sums)
    primesumsum = sum(primesums)
    primesums = np.array(primesums)
    primesums = np.ma.masked_where(primesums <= 0, primesums)
    slope = sumsum/additioncount
    slope2 = primesumsum/primecount
    x = np.linspace(0,n,n)
    y = slope*x*int(subtract_slope)
    plt.plot(sums-y, 'bo', ms=3, label="sums for composite numbers")
    plt.plot(primesums-y, 'ro', ms=3, label="sums for primes")
    plt.title("Sums of remainders of each x value when divided by all integers between 2 and itself (primes in red)")
    plt.grid()
    plt.legend()
    plt.xlabel("Number to sum remainders for")
    plt.ylabel("Sum of remainders" + ", minus slope times x"*int(subtract_slope))
    print("slope: ", slope,  "\nprime slope: ", primesumsum/primecount, "\npi minus e: ", math.pi-math.e, "\nprime slope and pi-e diff: ", abs((primesumsum/primecount)-(math.pi-math.e)))
    plt.show()
