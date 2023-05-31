#Write a program to create a list of numbers and find the sum of all the elements.
list= []
def sum_list_elements(numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)
    return  total


def sum_dictionary_values(dictionary_input):
    total = 0
    for dictionary in dictionary_input:
        for values in dictionary.values():
            print(total)
            total += values
            print(total)
    return total

my_list = [
    {'a': 1, 'b': 2, 'c': 3}
]
result = sum_dictionary_values(my_list)
print("Sum of values:", result)