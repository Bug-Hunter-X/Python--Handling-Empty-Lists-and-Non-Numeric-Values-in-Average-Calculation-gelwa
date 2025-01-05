def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of empty list is: {average_empty}")

my_list_with_zero = [10, 0, 20]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero in list is: {average_with_zero}")

my_list_with_strings = [10, '20', 30]
average_with_strings = calculate_average(my_list_with_strings) 
print(f"The average with strings in list is: {average_with_strings}")

my_list_with_all_strings = ['a', 'b', 'c']
average_all_strings = calculate_average(my_list_with_all_strings)
print(f"The average of list with all strings is: {average_all_strings}" )