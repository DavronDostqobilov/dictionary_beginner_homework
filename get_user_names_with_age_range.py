def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    list1=[]
    for i in data:
        if i['age']>min_age and i['age']<max_age:
            list1.append(i['name'])
    return list1
print(get_user_names_with_age_range([{'name': 'John','age': 20},{ 'name': 'Mary','age': 17},{'name': 'Ban','age': 23}],20,25)) 