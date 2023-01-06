def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    k=0
    for i in data:
        if i['age']==age:
            k+=1
    return k
print(count_users_with_age([{'name': 'John','age': 20},{ 'name': 'Mary','age': 23},{'name': 'Ban','age': 23}],23)) 