def print_factors(n):
    print(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Example usage
num = int(input("Enter a number to find its factors: "))
print_factors(num)
