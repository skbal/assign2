start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
divisor = int(input("Enter the divisor: "))

print(f"Numbers divisible by {divisor} between {start} and {end}:")
for num in range(start, end + 1):
    if num % divisor == 0:
        print(num, end=" ")
