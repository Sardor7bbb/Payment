from database import Database
from Class import Users


def balanc():
    pass



def add_money():
    new_data = input("Summni kiriting: ")

    query = f"UPDATE payment SET balanc = '{new_data}' WHERE user_id = '1';"
    return Database.connect(query, "update")
    print("Xizmat yakunlandi ")
    return

def pul_yechish():
    pass

def transfer_money():
    pass


def menu():
    menyu = input("""
    1. Balanc
    2. Pul qoshish
    3. Pul yechish
    4. Pul otqazish
    0. Back 
        >>> """)
    if menyu == "1":
        return balanc()
    elif menyu == "2":
        return add_money()
    elif menyu == "3":
        return pul_yechish()
    elif menyu == "4":
        return transfer_money()
    elif menyu == "0":
        return main()
    else:
        print("Invalid")
        return menu()



def login():
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    tabl = "users"
    query = f"""SELECT * FROM {tabl}"""
    data = Database.connect(query, "select")
    print(data)
    for i in data:
        if i[5] == phone and i[6] == password:
            return menu()
        else:
            print("Telefon raqam yoki password notogri !!!")

            return login()

def registr():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    card_number = input("Enter your card number: ")
    expiration_date = input("Enter your expiration date: ")

    Users.insert(first_name, last_name, phone, password, card_number, expiration_date)
    print("Muvafaqiyatli yakunlandi")
    return login()



def main():
    user = input("""
    1. Login
    2. Registr
        >>> """)

    if user == '1':
        return login()
    elif user == '2':
        return registr()
    else:
        print('Invalid')
        return main()

if __name__ == '__main__':
    main()