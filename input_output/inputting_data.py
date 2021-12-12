user_input = input("Enter your name, surname and birth year.Please separate values by comma and space. \n> ")
try:
    name, surname, birth_year = user_input.split(", ")
except ValueError:
    print("Wrong data provided")
else:
    print(f"Name: {name.capitalize()}, surname: {surname.capitalize()}, birth year: {birth_year}")