import rsa_utils
import time

def factorize_n(n):
    """Naive factorization to find p and q [cite: 85]"""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None

def main():
    n = int(input("Enter n: "))
    e = int(input("Enter e: "))
    
    start_time = time.time()
    factors = factorize_n(n)
    end_time = time.time()
    
    print(f"Time taken: {end_time - start_time:.6f} seconds") [cite: 92]
    
    if factors:
        p, q = factors
        phi = (p - 1) * (q - 1)
        d = rsa_utils.mod_inverse(e, phi)
        print(f"Factorization Succeeded! p: {p}, q: {q}, Recovered d: {d}") [cite: 93, 94]
    else:
        print("Factorization Failed.")

if __name__ == "__main__":
    main()