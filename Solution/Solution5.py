# def calculate_factorial(n):
#     factorial = 1
#     for i in range(1, n +1 ):
#     factorial *=i

#     return factorial

# n= int(input("type an integer that is not negative :"))

# answer= calculate_factorial(n)
# print(f"the factorial of {n}is{answer}")

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


n = int(input("Type an integer that is not negative: "))

answer = calculate_factorial(n)


print(f"The factorial of {n} is {answer}")

