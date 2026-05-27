# Hailstone sequence (Collatz conjecture)

n = int(input("Enter a positive integer: "))

while n != 1:
    if n % 2 == 0:  # check if even
        print(f"{n} is even, so I take half: {n // 2}")
        n = n // 2
    else:  # odd case
        print(f"{n} is odd, so I make 3n + 1: {3 * n + 1}")
        n = 3 * n + 1

print("Reached 1! Sequence complete.")
