# Function to find the sum of first n prime numbers
def sum_of_primes(n):
    if n <= 0:
        return 0  # If n is 0 or negative, return 0 (no primes to add)

    # To get the first n prime numbers, we need to guess a number range big enough.
    # it's just an estimate based on math formulas.
    import math
    if n < 6:
        limit = 15  # Small value for small n
    else:
        # This formula gives a rough idea of how big we should go to find n primes
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    # Now we make a list (sieve) to mark if a number is prime or not.
    # initially, assume all numbers are prime (True)
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # since 0 and 1 are not prime numbers

    primes = []  # This list will store the prime numbers we find

    # This is the main part where we use the Sieve of Eratosthenes
    # Here's how it works:
    # it starts with 2 (the first prime), and marks all multiples of 2 as not prime
    # Then it moves to the next unmarked number (like 3), and marks all its multiples
    # Keep doing this until we've found n prime numbers
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)  # If the number is still marked as True, it's a prime
            if len(primes) == n:
                break  # If we got enough primes, stop
            for j in range(i * i, limit + 1, i):
                sieve[j] = False  # Mark all multiples of i as not prime

    return sum(primes)  # Add all primes in the list and return the total

def main():
    # taking input from the user and call our function
    n = int(input("Enter how many prime numbers to sum: "))
    if n < 0:
        print("Please enter a positive integer.")
        main()
    # calling the function
    total = sum_of_primes(n)
    print(f"Sum of first {n} prime numbers: {total}")

main()