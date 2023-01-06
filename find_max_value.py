def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    values=data.values()
    list1=list(values)
    max=0
    for i in list1:
        if max<i:
            max=i
    return max
print(find_max_value({1:25, 9.1:40, 30:60.5}))