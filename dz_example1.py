class Name:
    def __init__(self, name) -> None:
        self.value = name

class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def edit_phone(self, old_phone, new_phone):
        pass

class AddressBook:
    def __init__(self) -> None:
        self.data = dict()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        # try:
        #     return self.data[name]
        # except KeyError:
        #     raise ValueError('User with this name does not exist')
        return self.data.get(name)

book = AddressBook()
john_record = Record("John")

book.add_record(john_record)

# print(book.data)

# book.data['John'].edit_phone('1234567890', '987654321')

book.find('John 2').edit_phone('1234567890', '987654321')