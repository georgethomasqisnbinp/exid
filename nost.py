def find_smallest_value(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
my_list = [4, 7, 2, 9, 1, 5]
print("The smallest value in the list is:", find_smallest_value(my_list))
