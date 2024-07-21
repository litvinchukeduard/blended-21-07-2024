'''
Написати функцію, яка буде приймати список користувачів та повертати тих користувачів, які народилися цього року
'''
from datetime import datetime

# [{'name': 'John', 'birthday': '21-07-2024'}, {'name': 'Alice', 'birthday': '21-07-2023'}]

# 1 - Для кожного користувача, взяти день народження та перетворити на datetime (map)
# 2 - Відсіяти тих користувачів, які народилися не цього року (filter)

def get_users_born_this_year(users: list[dict]) -> list[dict]:
    # 1 - Для кожного користувача, взяти день народження та перетворити на datetime (map)
    users_with_datetime = []
    for user in users:
        datetime_birthday = datetime.strptime(user['birthday'], '%d-%m-%Y')
        new_user = {'name': user['name'], 'birthday': datetime_birthday}
        users_with_datetime.append(new_user)  

    # print(users_with_datetime)
    # 2 - Відсіяти тих користувачів, які народилися не цього року (filter)
    users_born_this_year = []
    for user in users_with_datetime:
        today = datetime.today()
        if user['birthday'].year == today.year:
            users_born_this_year.append(user)

    return users_born_this_year

def transform_user_birthday_to_datetime(user: dict) -> dict:
    datetime_birthday = datetime.strptime(user['birthday'], '%d-%m-%Y')
    return {'name': user['name'], 'birthday': datetime_birthday}

def is_user_birthday_this_year(user: dict) -> bool:
    # today = datetime.today()
    # if user['birthday'].year == today.year:
    #     return True
    # else:
    #     return False
    # return user['birthday'].year == today.year
    return user['birthday'].year == datetime.today().year

lambda user: user['birthday'].year == datetime.today().year


def get_users_born_this_year_functional(users: list[dict]) -> list[dict]:
    users_with_datetime = map(transform_user_birthday_to_datetime, users)
    # return list(filter(is_user_birthday_this_year, users_with_datetime))
    return list(filter(lambda user: user['birthday'].year == datetime.today().year, users_with_datetime))             

# print(get_users_born_this_year([{'name': 'John', 'birthday': '21-07-2024'}, {'name': 'Alice', 'birthday': '21-07-2023'}]))
print(get_users_born_this_year_functional([{'name': 'John', 'birthday': '21-07-2024'}, {'name': 'Alice', 'birthday': '21-07-2023'}]))
