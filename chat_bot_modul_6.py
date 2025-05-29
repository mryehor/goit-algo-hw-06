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
    main()