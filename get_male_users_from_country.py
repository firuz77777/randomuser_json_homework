def get_male_users_from_country(data:dict, country:str)->list:
    """
    Get male users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
    Returns:

        list: A list of users
    """ 
    q=[]
    a = open('users.json').read
    for i in a['users']:
        if i['gender'] == 'male':
            q.append(i)
    return q
print(get_male_users_from_country('data', 'country'))


    