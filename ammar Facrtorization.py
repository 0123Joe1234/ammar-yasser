import math
import time

def factorize_N(N):
    """Function to factorize the modulus N into its prime factors p and q."""
    for p in range(2, math.isqrt(N) + 1):
        if N % p == 0:
            q = N // p
            return p, q
    return None, None

def compute_private_exponent(p, q, e):
    """Function to compute the private exponent d using Euler's Totient Function."""
    phi_N = (p - 1) * (q - 1)
    # Compute d, the modular inverse of e mod phi(N)
    d = pow(e, -1, phi_N)
    return d

def rsa_cracking(N, e):
    """Main function to crack the private exponent by factorizing N."""
    start_time = time.time()
    
    # Factorize N
    p, q = factorize_N(N)
    if p is None or q is None:
        print(f"Failed to factorize N = {N}")
        return None
    
    print(f"Factorization successful: p = {p}, q = {q}")
    
    # Compute private exponent d
    d = compute_private_exponent(p, q, e)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Private exponent d = {d}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    
    return d, elapsed_time

# Testing the function with small key sizes (8-bit and 16-bit)
def test_rsa_cracking():
    test_cases = [
        {"N": 187, "e": 7},  # 8-bit modulus example, N = 11 * 17
        {"N": 391, "e": 5},  # 8-bit modulus example, N = 17 * 23
        {"N": 3233, "e": 17},  # 16-bit modulus example, N = 61 * 53
        {"N": 6557, "e": 3}   # 16-bit modulus example, N = 71 * 97
    ]
    
    for case in test_cases:
        print("\nCracking RSA with N = {}, e = {}".format(case["N"], case["e"]))
        rsa_cracking(case["N"], case["e"])

# Run the test
test_rsa_cracking()
