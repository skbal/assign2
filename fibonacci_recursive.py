def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

terms = int(input("Enter number of terms: "))
print("Fibonacci series (recursive):")
for i in range(terms):
    print(fibonacci_recursive(i), end=" ")
