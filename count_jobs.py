def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    k=0
    for i in data:
        if i['job']==job:
            k+=1
    return k
print(count_jobs([{'name': 'John','job': 'Developer'},{'name': 'Mary','job': 'Developer'}],'Developer'))
