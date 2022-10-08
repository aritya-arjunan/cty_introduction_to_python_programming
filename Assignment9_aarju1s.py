# Get the input about how many numbers and get the numbers from the user.
number_list = []
total_numbers = int(input('How many numbers would you like to enter? \n'))
for x in range(total_numbers):
    number_list.append(int(input('Enter a number (%s of %s): \n' %(x + 1, total_numbers))))
# Sort the numbers into odd and even lists.
print('The number list:', number_list)
odd_list = []
even_list = []
for x in number_list:
    if (x % 2) == 1:
        odd_list.append(x)
    else:
        even_list.append(x)
# Print the odd and even lists.
print('The even list:', even_list)
print('The odd list:', odd_list)
