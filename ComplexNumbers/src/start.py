#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#problem 1 deadline week 9

from ui import *
from functions import *

def start():
    while True:
        try:
            command = get_user_input()
            action, args = parse_command(command)
            if action == 'add':
                try:
                    append_number(' '.join(args), complex_numbers)
                except ValueError as ve:
                    print("There was an error")
                    print(ve)

            elif action == "insert":
                try:
                    data_before = complex_numbers.copy()
                    check_insert(args, complex_numbers)
                    insert_number(complex_numbers, args)
                    data_after = complex_numbers.copy()  # Save the state after modification
                    add_to_history('insert_number', data_before, data_after)
                except ValueError as ve:
                    print("There was an error")
                    print(ve)

            elif action == "remove":
                try:
                    check_remove(args, complex_numbers)
                    if len(args) == 1:
                        remove_number(complex_numbers, args[0])
                    else:
                        remove_interval(complex_numbers, args)
                except ValueError as ve:
                    print("There was an error")
                    print(ve)

            elif action == "replace":
                try:
                    check_replace(complex_numbers, args)
                    replace(complex_numbers, args)
                except ValueError as ve:
                    print("There was an error")
                    print(ve)

            elif action == "list":
                if len(args) == 0:
                    display(complex_numbers)
                elif len(args) == 4:
                    try:
                        check_list_real(args)
                        display(print_real(complex_numbers, args))
                    except ValueError as ve:
                        print("There was an error")
                        print(ve)
                elif len(args) == 3:
                    try:
                        check_print_modulus(args)
                        display(print_modulus(complex_numbers, args))
                    except ValueError as ve:
                        print("There was an error")
                        print(ve)
                else:
                    display_error("Invalid syntax")

            elif action == "filter":
                if len(args) == 1:
                    try:
                        check_filter(args)
                        filter_real(complex_numbers)
                    except ValueError as ve:
                        print("There was an error")
                        print(ve)
                elif len(args) == 3:
                    try:
                        check_filter(args)
                        filter_modulo(complex_numbers, args)
                    except ValueError as ve:
                        print("There was an error")
                        print(ve)

                else:
                    display_error("Invalid syntax")
            elif action == 'undo':
                undo_operation(complex_numbers)

            elif action == "test":
                test_append_number()
                test_insert_number()
                test_remove_number()
                test_remove_interval()
                test_replace()
            else:
                display_error("Invalid command")
        except ValueError as ve:
            print("There was an error")
            print(ve)



if __name__ == "__main__":
    generate_random_complex_numbers(complex_numbers)
    start()
