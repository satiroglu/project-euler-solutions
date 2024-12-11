def is_palindrome(number):
    # Check if a number is a palindrome.
    return str(number) == str(number)[::-1]

def largest_palindrome_product():
    # Find the largest palindrome made from the product of two 3-digit numbers.
    max_palindrome = 0
    factors = (0, 0)

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # Start from 'i' to avoid duplicate pairs.
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                factors = (i, j)

    return max_palindrome, factors

# Run the function and print the result.
if __name__ == "__main__":
    palindrome, (factor1, factor2) = largest_palindrome_product()
    print(f"The largest palindrome is {palindrome}, which is the product of {factor1} and {factor2}.")
