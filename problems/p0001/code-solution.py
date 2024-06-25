def sum_of_multiples(limit):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum


# Set the limit to 1000 and print the solution
print("The sum of all the multiples of 3 or 5 below 1000 is:", sum_of_multiples(1000))
