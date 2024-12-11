def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor  # Divide n if divisible and continue
        else:
            factor += 1  # Move to the next factor if not divisible
    return n  # The remaining number is the largest prime factor

# Example usage:
number = 600851475143
print(largest_prime_factor(number))  # Returns the largest prime factor
