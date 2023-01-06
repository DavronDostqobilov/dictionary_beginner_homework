def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    values=data.values()
    list1=list(values)
    sum=0
    for i in list1:
        sum+=len(i)

    return sum
print(find_length_of_values({1:'fdsa',2:'wertgfd'})) 