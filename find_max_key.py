def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    keys=data.keys()
    list1=list(keys)
    max=0
    for i in list1:
        if max<i:
            max=i
    return max
print(find_max_key({1:'werds',9.1:'asdfgs',30:'dfdsdffdsdfvsd'}))