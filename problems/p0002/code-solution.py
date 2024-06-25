def sum_even_fibonacci(limit):
    a, b = 1, 2  # Starting values of the Fibonacci sequence
    sum_even = 0

    while a <= limit:
        if a % 2 == 0:
            sum_even += a
        a, b = b, a + b  # Generate the next Fibonacci number
    return sum_even


# Set the limit to four million and print the solution
print("The sum is:", sum_even_fibonacci(4000000))
