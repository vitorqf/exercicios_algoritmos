from handler import string_handle

print("Insert your number")

initial_string = input("> ")

try: 
    print(string_handle(initial_string))

except (ValueError) as e:
    print(e)