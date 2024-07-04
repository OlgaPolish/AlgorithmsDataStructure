def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iter(n):
    if n <= 1:
        return n

    F_0 = 0  # F(0)
    F_1 = 1  # F(1)
    current = 0

    for i in range(2, n + 1):
        current = F_1 + F_0
        F_0 = F_1
        F_1 = current

    return current

F_n = int(input("Enter index: "))
print("Recursively: ",fibonacci(F_n))
print("Iteratively: ",fibonacci_iter(F_n))