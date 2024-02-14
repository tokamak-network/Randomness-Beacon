import math
from web3 import Web3


def append_hex(a, b):
  sizeof_b = 0
  # get size of b in bits
  while ((b >> sizeof_b) > 0):
    sizeof_b += 1
  # every position in hex in represented by 4 bits
  sizeof_b_hex = math.ceil(sizeof_b / 4) * 4
  return (a << sizeof_b_hex) | b


# keccack hash function outputs int for strings
def mod_hash_eth(n, strings):
  r = Web3.keccak(strings)
  r = int(r.hex(), 16)
  print(hex(r))
  r = r % n
  return r

def generate_optimized_proof(N, x, τ, δ, s):
  start_time = time.time()
  checkpoints = make_checkpoints(τ, s)
  powers = repeated_squarings(N, x, checkpoints)
  y = powers[τ]
  π = generate_proof(x, τ, δ, y, N)
  print(f"Proof generated in {time.time() - start_time:.2f} seconds")
  return y, π


print(hex(mod_hash_eth(1099153, append_hex(5994085, 3615553))))