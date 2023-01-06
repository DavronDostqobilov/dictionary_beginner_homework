def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    keys=data.keys()
    list1=[]
    for i in keys:
        if i%1==0:
            list1.append(i)
    return list1
print(find_int_keys({1:'davron',2:'asd',3.3:'gfdsa'}))
 