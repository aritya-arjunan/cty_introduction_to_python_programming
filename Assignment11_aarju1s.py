def get_integer():
    number = input("Enter number:")
    # Check if there is any non-spaced characters in the input
    if not bool(number.rstrip()):
        number = get_integer()
        return number
    # Delete any spaces then convert input to float and then convert to an
    # integer
    else:
        number = number.strip()
        number = float(number)
        number = int(number)
        return number


print("What number should we start with?")
first_number = get_integer()
print("What number should we end with?")
second_number = get_integer()
print("What number should we count by?")
step_number = get_integer()

list_of_numbers = list(range(first_number, second_number, step_number))
print('List of numbers:')
print(list_of_numbers)
sum_of_numbers = sum(list_of_numbers)
print('Sum of numbers:')
print(sum_of_numbers)
