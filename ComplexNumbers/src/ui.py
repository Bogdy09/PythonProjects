#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

from functions import *

def read_number():
    real_number=input("Please enter complex numbers(a+bi form): ")
    return real_number

complex_numbers=[]
def get_user_input():
    return input("Enter the command: ")

def display_error(message):
    print(f"Error: {message}")


def parse_command(command):
    if not command:
        raise ValueError("Please enter the command")
    elements = command.split()
    action = elements[0].lower()
    args = elements[1:]
    return action, args

def to_str(nr):
        return str(nr[0])+'+'+str(nr[1])+'i'

def display(complex_numbers):
    for nr in complex_numbers:
        print(to_str(nr))
