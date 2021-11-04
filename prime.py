
# determines whether n is prime
def is_prime(n):
    for i in range(2,n):
        if not n%i:
            return False

    return True
# a new function that generates the prime numbers
# less than or equal to N
def generate_prime_numbers(N):
    result = []
    for i in range(2, N+1):
        if is_prime(i):
            result.append(i)
    return result

