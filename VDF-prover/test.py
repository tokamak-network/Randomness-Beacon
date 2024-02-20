from Pietrzak_VDF import optimized_proof
import time
import math

if __name__ == '__main__':
    p = 123456211
    q = 123384263
    N = p * q
    x = pow(509, 23, N)
    t = 25
    τ = pow(2, t)
    δ = 8
    s = round((math.log(τ) - δ) / (2 * math.log(2)))

    print("Starting optimized proof generation...")
    start_time = time.time()
    y, π = optimized_proof(N, x, τ, δ, s)
    print(f"Optimized proof generated in {time.time() - start_time:.2f} seconds.")
    print(f"Result y: {y}")
    print(f"Proof π: {π}")

    start_time = time.time()
    verification_time = time.time() - start_time
