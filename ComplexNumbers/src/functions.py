#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random
import math



def generate_random_complex_numbers(complex_numbers):
    """
    Generates a list of random complex numbers.
    :param complex_numbers:A list to which the generated random complex numbers are appended.
    :return: nothing
    """
    for _ in range(10):  # Generate 10 random complex numbers
        real_part = random.randint(0, 10)
        imag_part = random.randint(0, 10)
        complex_numbers.append(create_complex(real_part, imag_part))

history = []

# Function to save data state and operation to history
def add_to_history(operation, data_before, data_after):
    """
    Records the history of operations and their effects on complex_numbers.
    :param operation:A string indicating the operation performed.
    :param data_before:A copy of complex_numbers before an operation is executed.
    :param data_after:A copy of complex_numbers after an operation is executed.
    :return:
    """
    history.append((operation, data_before, data_after))

# Function to undo the last operation
def undo_operation(complex_numbers):
    """
    Reverts the most recent operation on complex_numbers.
    :param complex_numbers:The list of complex numbers to revert an operation.
    :return:nothing
    """
    if history:
        operation, data_before, _ = history.pop()
        # Restore the data state to its previous state
        complex_numbers[:] = data_before
        print(f"Undo: Reverted {operation} operation")
def get_imag(complex_number):
    return complex_number[1]

def get_real(complex_number):
    return complex_number[0]

def create_complex(real_part, imag_part):
    """
    Creates a complex number from given real and imaginary parts.
    :param real_part:An integer representing the real part of the complex number.
    :param imag_part:An integer representing the imaginary part of the complex number.
    :return:A list representing the complex number in the form [real_part, imag_part].
    """
    return [real_part, imag_part]

def check_insert(args, complex_numbers):
    """
    It validates the syntax and correctness of arguments passed for insertion on complex numbers.
    :param args:A list of arguments passed for insertion
    :param complex_numbers:The list of complex numbers on which the operation is to be performed.
    :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if args[1]!="at":
        raise ValueError("Invalid syntax")
    if int(args[2])<0 or int(args[2])>=len(complex_numbers):
        raise ValueError("Position out of bounds")

def check_remove(args, complex_numbers):
    """
        It validates the syntax and correctness of arguments passed for remove on complex numbers.
        :param args:A list of arguments passed for remove
        :param complex_numbers:The list of complex numbers on which the operation is to be performed.
        :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if not args:
        raise ValueError("Please enter the number")
    if len(args)==1:
        if not args[0].isdigit():
            raise ValueError("Please enter a valid number")
        if int(args[0])<0 or int(args[0])>=len(complex_numbers):
            raise ValueError("Position out of bounds")
    else:
        if len(args)>3:
            raise ValueError("Invalid syntax")
        if args[1]!="to":
            raise ValueError("Invalid syntax")
        if not args[0].isdigit() or not args[2].isdigit():
            raise ValueError("Please enter valid positions")
        if args[0]>args[2]:
            raise  ValueError("Invalid positions")
        if int(args[0])<0 or int(args[0])>=len(complex_numbers) or (int(args[2])<0 or int(args[2])>=len(complex_numbers)):
            raise ValueError("Position out of bounds")

def check_complex(complex_nr):
    """
        It validates if the number is of a correct form
        :param complex_nr:A complex number
        :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if '+' in complex_nr and 'i' in complex_nr:
        parts = complex_nr.replace(' ', '').split('+')
        if len(parts) != 2:
            raise ValueError("The number is not of a+bi form")
    else:
        raise ValueError("The number is not of a+bi form")
    return True
def check_replace(complex_numbers, args):
    """
        It validates the syntax and correctness of arguments passed for replace on complex numbers.
        :param args:A list of arguments passed for replace
        :param complex_numbers:The list of complex numbers on which the operation is to be performed.
        :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if not args:
        raise ValueError("Invalid syntax")
    if args[1]!="with":
        raise ValueError("Invalid syntax")
    if len(args)!=3:
        raise ValueError("Invalid syntax")
    if not check_complex(args[0]) or not check_complex(args[2]):
        raise ValueError("Numbers are not complex")

def check_list_real(args):
    """
        It checks if a list is correct.
        :param args:A list of arguments passed
        :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if args[0]!="real" or not args[1].isdigit or args[2]!="to" or not args[3].isdigit:
        raise ValueError("Invalid syntax")

def check_print_modulus(args):
    """
            It checks if the syntax for filter modulus is correct
            :param args:A list of arguments passed
            :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if args[0]!="modulo" or not args[2].isdigit():
        raise ValueError("Invalid syntax")

def check_filter(args):
    """
            It checks if filter function has a correct syntax
            :param args:A list of arguments passed
            :return:If the arguments satisfy the required syntax and conditions, the function completes successfully. Otherwise, it raises a ValueError with an appropriate error message.
    """
    if len(args)==1:
        if args[0]!="real":
            raise ValueError("Invalid syntax")
    elif len(args)==3:
        if args[0]!="modulo" or (args[1]!="<" and args[1]!=">" and args[1]!="=") or not args[2].isdigit:
            raise ValueError("Invalid syntax")
def to_list(complex_nr):
    """
    Converts a string representation of a complex number to a list representation.
    :param complex_nr:A string representation of a complex number in the form "a+bi".
    :return:A list representing the complex number in the form [real_part, imag_part].
    """
    complex_list = complex_nr.split()
    for complex_nr in complex_list:
        if '+' in complex_nr and 'i' in complex_nr:
            parts = complex_nr.replace(' ', '').split('+')
            if len(parts) == 2:
                real_part = int(parts[0])
                imag_part = int(parts[1].replace('i', ''))
            else:
                raise ValueError("The number is not of a+bi form")
        else:
            raise ValueError("The number is not of a+bi form")
    return create_complex(real_part, imag_part)

def append_number(real_number, complex_numbers):
    """
    Adds a complex number to the list of complex numbers.
    :param real_number:A string representation of the complex number to be appended
    :param complex_numbers:The list of complex numbers where the number will be added.
    :return:nothing
    """
    data_before = complex_numbers.copy()
    if not real_number:
        raise ValueError("Please enter the number")
    if '+' in real_number and 'i' in real_number:
        parts = real_number.replace(' ', '').split('+')
        if len(parts)==2:
            real_part = int(parts[0])
            imag_part = int(parts[1].replace('i', ''))
        else:
            raise ValueError("The number is not of a+bi form!")
    else:
        raise ValueError("The number is not of a+bi form")

    complex_numbers.append(create_complex(real_part, imag_part))
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('append_number', data_before, data_after)

def insert_number(complex_numbers, args):
    complex_numbers[int(args[2])] = to_list(args[0])
def remove_number(complex_numbers, position):
    """
    Removes a complex number from the list based on the given position.
    :param complex_numbers:The list of complex numbers from which a number will be removed.
    :param position:The index position of the number to be removed.
    :return:
    """
    data_before = complex_numbers.copy()
    del complex_numbers[int(position)]
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('remove_number', data_before, data_after)

def remove_interval(complex_numbers, args):
    """
    Removes a range of complex numbers from the list based on the given positions.
    :param complex_numbers:The list of complex numbers from which numbers will be removed.
    :param args:A list containing the start and end positions for the removal
    :return:
    """
    data_before = complex_numbers.copy()
    del complex_numbers[int(args[0]):int(args[2])+1]
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('remove_interval', data_before, data_after)

def replace(complex_numbers, args):
    """
    Replaces occurrences of a specific complex number with another.
    :param complex_numbers:The list of complex numbers where the replacement will be performed.
    :param args:A list containing the number to be replaced and the number to replace with
    :return:
    """
    data_before = complex_numbers.copy()
    i=to_list(args[0])
    j=to_list(args[2])
    ok=False
    for index, el in enumerate(complex_numbers):
        if el == i:
            ok=True
            complex_numbers[index] = j
    if ok==False:
        raise ValueError("The number is not in the list")
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('replace_number', data_before, data_after)

def print_real(complex_numbers, args):
    """
    Filters real numbers from the list of complex numbers.
    :param complex_numbers:The list of complex numbers to filter
    :param args:A list containing the range to filter real numbers
    :return:
    """
    list1=[]
    for i in range(int(args[1]), int(args[3])+1):
        nr=complex_numbers[i]
        if get_imag(nr)==0:
            list1.append(nr)
    return list1

def modulus(complex_num):
    """
    Calculates the modulus of a given complex number.
    :param complex_num:The complex number for which the modulus is calculated.
    :return:The modulus value of the given complex number.
    """
    real_part = get_real(complex_num)
    imag_part = get_imag(complex_num)
    return math.sqrt(real_part**2 + imag_part**2)

def print_modulus(complex_numbers, args):
    """
     Filters complex numbers based on modulus comparison.
    :param complex_numbers:The list of complex numbers to filter
    :param args:A list containing the condition to filter modulus
    :return:the filtered list
    """
    list1=[]
    if args[1]=="<":
        for nr in complex_numbers:
            if modulus(nr)<int(args[2]):
                list1.append(nr)
    elif args[1]=="=":
        for nr in complex_numbers:
            if modulus(nr)==int(args[2]):
                list1.append(nr)
    elif args[1] == ">":
        for nr in complex_numbers:
            if modulus(nr) > int(args[2]):
                list1.append(nr)

    else:
        raise ValueError("Invalid syntax")
    if not list1:
        raise ValueError("There are no elements with the desired property")
    return list1

def filter_real(complex_numbers):
    """
    Filters real numbers from the list of complex numbers.
    :param complex_numbers:The list of complex numbers to filter.
    :return:nothing
    """
    data_before = complex_numbers.copy()
    for i in range(len(complex_numbers)-1, -1, -1):
        if get_imag(complex_numbers[i])!=0:
            del complex_numbers[i]
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('filter_real', data_before, data_after)

def filter_modulo(complex_numbers, args):
    """
    Filters complex numbers based on modulus comparison.
    :param complex_numbers:The list of complex numbers to filter.
    :param args:A list containing the condition to filter modulus
    :return: nothing
    """
    data_before = complex_numbers.copy()
    if args[1]=="<":
        for i in range(len(complex_numbers)-1, -1, -1):
            if modulus(complex_numbers[i])>=int(args[2]):
                del complex_numbers[i]

    elif args[1]=="=":
        for i in range(len(complex_numbers)-1, -1, -1):
            if modulus(complex_numbers[i])!=int(args[2]):
                del complex_numbers[i]

    elif args[1]==">":
        for i in range(len(complex_numbers)-1, -1, -1):
            if modulus(complex_numbers[i])<=int(args[2]):
                del complex_numbers[i]
    data_after = complex_numbers.copy()  # Save the state after modification
    add_to_history('filter_modulo', data_before, data_after)


def test_append_number():
    complex_numbers = []

    # Test valid complex number
    try:
        append_number('3+4i', complex_numbers)
        assert len(complex_numbers) == 1
        print("Test passed: Valid complex number was appended.")
    except ValueError:
        print("Test failed: Valid complex number was rejected unexpectedly.")

    # Test invalid complex number format
    try:
        append_number('invalid_complex_number', complex_numbers)
        print("Test failed: Invalid complex number was accepted.")
    except ValueError as e:
        if str(e) == "The number is not of a+bi form":
            print("Test passed: Correctly rejected invalid complex number format.")
        else:
            print("Test failed: Invalid error message.")

    # Test empty input
    try:
        append_number('', complex_numbers)
        print("Test failed: Empty input was accepted.")
    except ValueError as e:
        if str(e) == "Please enter the number":
            print("Test passed: Correctly rejected empty input.")
        else:
            print("Test failed: Invalid error message.")


def test_insert_number():
    complex_numbers = []
    append_number('3+4i', complex_numbers)
    append_number('6+2i', complex_numbers)
    append_number('2+8i', complex_numbers)

    # Test case: Insert a number at an out-of-range index
    args = ['7+5i', 'at', '5']  # '5' is out of range for the list length of 3
    try:
        insert_number(complex_numbers, args)
        print("Test failed: Insertion successful")
    except IndexError:
        print("Test passed: Index out of range")

    # Test case: Insert a number at a valid index
    args = ['7+5i', 'at', '1']
    try:
        insert_number(complex_numbers, args)
        print("Test passed: Insertion successful")
    except IndexError:
        print("Test failed: Index out of range")

def test_remove_number():
    complex_numbers = []
    append_number('3+4i', complex_numbers)
    append_number('6+2i', complex_numbers)
    append_number('2+8i', complex_numbers)

    # Test removing an element at a valid position
    try:
        remove_number(complex_numbers, 1)
        assert len(complex_numbers) == 2
        print("Test passed: Removed element at a valid position.")
    except ValueError:
        print("Test failed: Unexpected error while removing at a valid position.")

    # Test removing an element at an invalid position
    try:
        remove_number(complex_numbers, 5)  # Out of range position
        print("Test failed: Removed element at an invalid position.")
    except IndexError:
        print("Test passed: Tried to remove an element at an invalid position.")


def test_remove_interval():
    complex_numbers = []

    # Test valid removal interval
    try:
        append_number('3+4i', complex_numbers)
        append_number('6+2i', complex_numbers)
        append_number('2+8i', complex_numbers)
        append_number('9+1i', complex_numbers)
        remove_interval(complex_numbers, ['1', "to", '2'])
        assert len(complex_numbers) == 2
        print("Test passed: Removed elements in a valid interval.")
    except:
        print("Test failed: Unexpected error while removing a valid interval.")

    # Test invalid removal interval
    try:
        check_remove(['5',"to", '2'],complex_numbers)
        remove_interval(complex_numbers, ['5',"to", '2'])  # Out of range positions
        print("Test failed: Removed elements in an invalid interval.")
    except ValueError:
        print("Test passed: Tried to remove elements in an invalid interval.")


def test_replace():
    complex_numbers = []


    # Test invalid number format
    try:
        replace(complex_numbers, ['invalid', '5+5i'])  # Replace 'invalid' with '5+5i'
        print("Test failed: Invalid number was accepted.")
    except ValueError as e:
        if str(e) == "The number is not of a+bi form":
            print("Test passed: Correctly rejected invalid number format.")
        else:
            print("Test failed: Invalid error message.")
    except Exception as e:
        print("Test failed with exception:", e)









