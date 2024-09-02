number_range = range(1, 10)

def is_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "not even"

for number in number_range:
    result_is = is_even(number)
    print(f"The number {number} is {result_is}")
