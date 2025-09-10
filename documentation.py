# Example 1
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    pi = 3.14159
    return pi * radius * radius


# Example 2
def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Args:
        numbers (list of int or float): The list of numbers to search.

    Returns:
        int or float: The maximum value in the list.

    Raises:
        IndexError: If the list is empty.
    """
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# Example 3
def bubble_sort(arr):
    """
    Sort a list of numbers in ascending order using the bubble sort algorithm.

    Args:
        arr (list of int or float): The list of numbers to sort.

    Returns:
        list of int or float: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr