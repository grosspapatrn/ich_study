from pydantic import *
import json
import re


frame = "--------------------------------------------------"
print(frame)


def user_sign_up(new_user):

    # creating class Address for register user's address
    class Address(BaseModel):
        city: str = Field(min_length=2)
        street: str = Field(min_length=3)
        house_number: int = Field(gt=0)

        # creating output
        def __str__(self):
            return f'\tCity: {self.city}\n\tStreet: {self.street}\n\tHouse number: {self.house_number}'


    # creating class User for register user's data
    class User(BaseModel):
        name: str = Field(min_length=2)
        age: int = Field(gt=0, lt=120)
        email: EmailStr
        is_employed: bool
        address: Address

        # creating output
        def __str__(self):
            return f'Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\nIs employed: {self.is_employed}\nAddress: \n{self.address}'


    # creating an age and employee status checker
    def age_employee_checker(age, is_employed):
        if is_employed:
            if 18 <= age < 65:
                print(' SAVED DATAS '.center(50, "="), user, sep='\n')
            else:
                print(f'\033[1mStatus of Employee\033[0m cannot be \033[1m"is employed"\033[0m \nif user "{user.name}" is younger than 18 \nor older than 65 years old.')
        else:
            print(user)


    # creating try:except to troubleshoot user's input with age
    try:
        user = User.model_validate_json(new_user)
        age_employee_checker(user.age, user.is_employed)
    except ValidationError as e:
        print(f'\033[1mUser cannot be registered.\033[0m\nError by entering age. It can be \nbetween 0 and 120 years old.')

    print(frame)

def input_user_data():
    user_name = input(f'{frame}\nSo, than type some info here\n\nEnter your name: ').capitalize().strip()

    user_age = int
    while True:
        user_age = input('Enter your age: ')
        try:
            user_age = int(user_age)
            break
        except ValueError:
            print(' Please enter a number, not letters '.center(50, "="))

    user_email = str
    while True:
        input_email = input('Enter your email: ').strip()

        email_template = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if email_template.match(input_email):
            user_email = input_email
            break
        else:
            print('Please enter a valid email address')

    user_is_employed = bool
    while True:
        user_is_employed = input('Are you employed? (true/false): ').lower().strip()
        if user_is_employed == 'true' or user_is_employed == '+' or user_is_employed == 'y':
            user_is_employed = True
            break
        elif user_is_employed == 'false' or user_is_employed == '-' or user_is_employed == 'n':
            user_is_employed = False
            break
        else:
            print('Please enter "true" or "false"')

    user_city = input('Enter your city: ').capitalize().strip()
    user_street = input('Enter your street: ').capitalize().strip()

    user_house_number = int
    while True:
        input_house_number = input('Enter your house number: ')
        try:
            user_house_number = int(input_house_number)
            break
        except ValueError:
            print(' Please enter a number, not letters '.center(50, "="))

    raw_new_user = {
        'name': user_name,
        'age': user_age,
        'email': user_email,
        'is_employed': user_is_employed,
        'address': {
            'city': user_city,
            'street': user_street,
            'house_number': user_house_number}}

    new_user = json.dumps(raw_new_user, indent=4)
    return new_user

print('Do you want to register a new user?')
choose_option = ""
while not choose_option:
    print('\n1 - Register new user from template users\n2 - Register new user from your own data\n')
    new_user_register = input('Enter a number or press enter to quit: ').strip()

    if new_user_register == '':
        choose_option = True
        print('', ' Goodbye! '.center(50, "="), sep="\n")
        break

    if new_user_register == '1':
        json_input1 = """{
            "name": "Max",
            "age": 30,
            "email": "max@mustermann.de",
            "is_employed": true,
            "address": {
                "city": "Berlin",
                "street": "Bahnhofstrasse",
                "house_number": 12
            }}"""

        user_sign_up(json_input1)

        json_input2 = """{
            "name": "Pablo",
            "age": 18,
            "email": "pabb.lo@gmx.de",
            "is_employed": false,
            "address": {
                "city": "Berlin",
                "street": "Alte Strasse",
                "house_number": 12
            }}"""

        user_sign_up(json_input2)

        json_input3 = """{
            "name": "John Doe",
            "age": 70,
            "email": "john.doe@example.com",
            "is_employed": true,
            "address": {
                "city": "New York",
                "street": "5th Avenue",
                "house_number": 123
            }}"""

        user_sign_up(json_input3)

        # creating extra false "json" input to check usability
        json_input4 = """{
            "name": "Manu",
            "age": 123,
            "email": "emmanu@gmx.de",
            "is_employed": false,
            "address": {
                "city": "Baden-Baden",
                "street": "Hauptstrasse",
                "house_number": 312
            }}"""

        user_sign_up(json_input4)

        re_ask = ""
        while not re_ask:
            reg_new_user = input('Do you want to register a new user? [+/-]: ').strip()
            if reg_new_user == '+':
                choose_option = False
                break
            elif reg_new_user == '-':
                choose_option = True
                print('', ' Goodbye! '.center(50, "="), sep="\n")
                break
            else:
                print(' Please enter "+" or "-" '.center(50, "="))

    if new_user_register == '2':
        user_sign_up(input_user_data())

        re_ask = ""
        while not re_ask:
            reg_new_user = input('Do you want to register a new user? [+/-]: ').strip()
            if reg_new_user == '+':
                choose_option = False
                break
            elif reg_new_user == '-':
                choose_option = True
                print('', ' Goodbye! '.center(50, "="), sep="\n")
                break
            else:
                print(' Please enter "+" or "-" '.center(50, "="))

    if new_user_register != '1' and new_user_register != '2':
        print(' Please enter a number between 1 and 2 '.center(50, "="))
