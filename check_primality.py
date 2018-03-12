'''
check for primality
'''

import math

def check_primality(n):
    if n < 2:
        return False
        
    for i in range(2, int(math.ceil(math.sqrt(n)))): #a*b = n and a<b, we do not need check b
        if n%i == 0:
            return False
    return True
    
print check_primality(1)

#Sieve of eratosthenes: generate a list of primes: all non-prime number is dividable by a prime number
def gen_prime_list(n):
    ''' generate a list of prime up to n'''
    flags = [True]*(n+1)
    flags[0] = flags[1] = False
    
    prime = 2
    while prime <= int(math.ceil(math.sqrt(n))):
        crossoff(flags, prime)
        
        prime = get_next_prime(flags, prime)
    
    prime_list = []
    for i, item in enumerate(flags):
        if item:
            prime_list.append(i)
            
    return prime_list
    
def crossoff(flags, prime):
    i = prime*prime # for k*prime where K < prime, we already took care of it 
    while i < len(flags):
        flags[i] = False
        i += prime
        
    return 
    
def get_next_prime(flags, prime):
    for i in range(prime+1, len(flags)):
        if flags[i] == True:
            return i
            
    return
    
print gen_prime_list(20)