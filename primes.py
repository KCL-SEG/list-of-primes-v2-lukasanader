"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i=0
    primenumber=1
    prime =False
    if(number_of_primes>0):
        while (i<number_of_primes):
            for x in range(2,int(primenumber/2)+2):
                if(primenumber%x!=0):
                    prime=True
                else:
                    if(primenumber==x):
                        prime=True
                        break
                    prime=False
                    break
                
            if(prime):
                list.append(primenumber)
                i=i+1
            primenumber=primenumber+1
    else:
        raise ValueError

    return list

print(primes(10))
