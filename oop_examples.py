'''
Cat: color, eye_color, name, gender: 'male', 'female'
'''
from collections import UserDict

class Cat:
    def __init__(self, color, eye_color, name, gender) -> None:
        self.color = color
        self.eye_color = eye_color
        self.name = name
        self.gender = gender

    def meow(self):
        if self.gender == 'female':
            print('meow!')
        else:
            print('Meow!')

# cat_one = Cat()
# cat_one.name = 'Vasya'

cat_one = Cat('black', 'green', 'Vasya', 'female')
cat_one.name = 'Musya'
# cat_one.meow()

# print(dir(cat_one))

cat_two = Cat('grey', 'blue', 'Petya', 'male')
cat_three = Cat('grey', 'blue', 'Petya', 'male')
# cat_two.meow()

str_one = "one"
str_two = "two"
lst = [str_one, str_two]

# print(lst)

cat_lst = [cat_one, cat_two]
# print(cat_lst)

print(cat_two)
print(cat_three)
print(cat_two == cat_three)

print(cat_two.color == cat_three.color and cat_two.eye_color == cat_three.eye_color)
