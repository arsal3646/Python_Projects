import math

# Ask user for a number
n = float(input("Enter a number: "))

# Calculate square root
root = math.sqrt(n)

# Raise n to the power of sqrt(n)
result = n ** root

print(f"{n} raised to the power of its square root ({root}) is: {result}")
