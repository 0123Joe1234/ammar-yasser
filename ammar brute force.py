import time

def brute_force_private_exponent(N, e, C, M):
    """Brute force method to find private exponent d by trying all possible values."""
    start_time = time.time()
    
    # Brute force all possible values of d
    for d in range(1, N):
        # Compute the decrypted message: M' = C^d mod N
        M_prime = pow(C, d, N)
        if M_prime == M:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Private exponent found: d = {d}")
            print(f"Elapsed time: {elapsed_time:.6f} seconds")
            return d, elapsed_time
    
    print("Failed to find private exponent d.")
    return None, None

# Testing the brute force function with small key sizes (8-bit and 16-bit)
def test_brute_force_rsa():
    test_cases = [
        {"N": 187, "e": 7, "C": 11, "M": 88},  # 8-bit example: N = 11 * 17, M = 88
        {"N": 391, "e": 5, "C": 29, "M": 147},  # 8-bit example: N = 17 * 23, M = 147
        {"N": 3233, "e": 17, "C": 2790, "M": 123},  # 16-bit example: N = 61 * 53, M = 123
        {"N": 6557, "e": 3, "C": 97, "M": 450}   # 16-bit example: N = 71 * 97, M = 450
    ]
    
    for case in test_cases:
        print(f"\nBrute-forcing RSA with N = {case['N']}, e = {case['e']}, C = {case['C']}, M = {case['M']}")
        brute_force_private_exponent(case["N"], case["e"], case["C"], case["M"])

# Run the test
test_brute_force_rsa()
