#Complete the print_full_name function in the editor below.
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))

first_name = input('Print first name.\n')
last_name = input('Print last name.\n')
print_full_name(first_name, last_name)