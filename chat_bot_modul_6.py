from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        
        if not (value.isdigit() and len(value) == 10):
             raise ValueError("Номер телефону повинен містити рівно 10 цифр.")
        super().__init__(value)

    def __str__(self):
         return self.value
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    # реалізація класу
    def add_phone(self, phone: str):
         self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone_obj = self.find_phone(old_phone)

        if phone_obj:
            new_phone_obj = Phone(new_phone)  
            phone_obj.value = new_phone_obj.value
        else:
            raise ValueError(f"Phone number {old_phone} not found.")
    
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
         self.data[record.name.value] = record

    def find(self, name): 
         return self.data.get(name)
    
    def delete(self, name):
         if name in self.data:
            del self.data[name]

    def __str__(self):
        if not self.data:
            return "AddressBook is empty."
        return "\n".join(str(record) for record in self.data.values())
    
def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Error: Please enter valid data."
            except KeyError:
                return "Error: Contact not found"
            except IndexError:
                return "Error: Missing arguments. Please provide enough information."
        return inner

def parse_input(user_input):
            parts = user_input.strip().lower().split()
            cmd = parts[0]
            args = parts [1:]
            return cmd, args

@input_error
def add_contact(contacts, args) :
   
    name, phone = args[0], args[1]
    if not phone.isdigit():
        raise ValueError
    contacts[name] = phone  
    return f"Contact with name {name} and number {phone} added "
        
@input_error
def change_contact(contacts, args):

    name, phone = args[0], args[1]
    if name not in contacts:
        raise KeyError
    if not phone.isdigit():
        raise ValueError
    contacts[name] = phone
    return f"Phone number for {name} changed to {phone}."
        
@input_error
def show_phone(contacts, args) :

    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"Phone number for {name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "Contact list is empty"
    else:    
        result = ["All contacts: "]
        for name, phone in contacts.items():
            result.append(f"{name.title()}: {phone}")
        return "\n".join(result)



def main():
    contacts = {}

    
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result = add_contact(contacts, args)
            print(result)

        elif command == "change":
            result = change_contact(contacts, args)
            print(result)

        elif command == "phone":
            result = show_phone(contacts, args)
            print(result)

        elif command == "all":
            result = show_all(contacts)
            print(result)

        else:
            print("Unknown command. Try: add, change, phone, all, exit")

if __name__ == "__main__":
    ab = AddressBook()

    r1 = Record("Іван")
    r1.add_phone("1234567890")
    r1.add_phone("0987654321")

    r2 = Record("Олена")
    r2.add_phone("1112223333")

    ab.add_record(r1)
    ab.add_record(r2)

    print(ab)

    # Знайти контакт
    rec = ab.find("Іван")
    print(rec)

    # Змінити телефон
    rec.edit_phone("1234567890", "9998887777")
    print(ab)

    # Видалити контакт
    ab.delete("Олена")
    print(ab)
    main()