'''
Написати функцію, fn(3)(4)(5) -> 3 * 4 * 5 -> 60

Написати функцію, яка буде рахувати обʼєм
'''

# def fn():
#     def fn_2():
#         def fn_3():

def calculate_volume(a: int):
    def get_height(b: int):
        def get_width(c: int):
            return a * b * c
        return get_width
    return get_height

print(calculate_volume(3)(4)(5))

# f(2)(3)
def calculate_area(a: int):
    def get_width(b: int):
        return a * b
    return get_width


def get_width(b: int):
        return b

# print(sum)
print(calculate_area(2)(3))



