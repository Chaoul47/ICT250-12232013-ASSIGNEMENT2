

def gcd(a, b):
   
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def mod_inverse(e, phi):
  
    d, x, y = extended_gcd(e, phi)
    if d != 1:
        return None
    return x % phi

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_primes(limit, start=100):
    primes = []
    num = start
    while len(primes) < limit + 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes