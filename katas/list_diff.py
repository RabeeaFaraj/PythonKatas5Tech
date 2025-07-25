def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    if not numbers:
        raise ValueError("List is empty")
    
    if len(numbers) == 1:
        return 0
    
    min_num = float('inf')
    max_num = float('-inf')
    for num in numbers:
        if num < min_num:
            min_num=num
        elif num > max_num:
            max_num=num
    diff=max_num-min_num
    return diff


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed