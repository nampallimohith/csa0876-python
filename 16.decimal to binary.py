def is_prime(n):
   
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_non_primes(A, B):
   
    for num in range(A, B + 1):
        if not is_prime(num):
            print(num, end=' ')

# Example usage
A = 12
B = 19
print(f"Non-prime numbers between {A} and {B}:")
print_non_primes(A, B)
