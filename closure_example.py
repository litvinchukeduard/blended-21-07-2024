'''
Написати функцію, яка буде генерувати унікальний ідентифікатор
'''

1, 2, 3, 4
id = 0

def create_unique_id() -> int:
    global id
    id += 1
    return id

# print(create_unique_id())
# print(create_unique_id())
# print(create_unique_id())
# print(create_unique_id())
def create_unique_id_closure():
    id = 0
    def get_next_id():
        nonlocal id
        id += 1
        return id
    return get_next_id

# variable = create_unique_id_closure
# variable()
# variable()

get_new_number = create_unique_id_closure()
print(get_new_number())
print(get_new_number())
print(get_new_number())

get_new_number_two = create_unique_id_closure()
print(get_new_number_two())
print(get_new_number_two())
print(get_new_number_two())
