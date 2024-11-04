#problem 6, 12

#NUI
import math
def create_complex(real, imag):
    return {'real': real, 'imag': imag}

def get_real(complex_num):
    return complex_num['real']

def get_imag(complex_num):
    return complex_num['imag']

"""def create_complex(real, imag):
    return [real, imag]
def get_real(complex_num):
    return complex_num[0]
def get_imag(complex_num):
    return complex_num[1]"""

def to_str(complex_num):
    return f"{get_real(complex_num)} + {get_imag(complex_num)}i"

import math

def modulus(complex_num):
    real_part = get_real(complex_num)
    imag_part = get_imag(complex_num)
    return math.sqrt(real_part**2 + imag_part**2)


def modulus_difference(num1, num2):
    return abs(modulus(num1) - modulus(num2))

def is_prime(n):
    if not isinstance(n, (int, float)) or n < 2 or n % 1 != 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_difference_subarray(complex_numbers):
    max_length = 0
    current_length = 1
    start_index = 0
    subarray = []
    max_subarray = []

    for i in range(1, len(complex_numbers)):
        diff_modulus = modulus_difference(complex_numbers[i-1], complex_numbers[i])

        if is_prime(diff_modulus):
            current_length += 1
            if complex_numbers[i - 1] not in subarray:
                subarray.append(complex_numbers[i - 1])
            if complex_numbers[i] not in subarray:
                subarray.append(complex_numbers[i])

            if current_length > max_length:
                max_length = current_length
                max_subarray = subarray
        else:
            current_length = 1
            subarray = []
            start_index = i
    return max_length, max_subarray

def Max(a, b):
    if a > b:
        return a
    else:
        return b


def alternating_subsequence(numbers):
    n = len(numbers)
    DP = [[0 for i in range(2)] for j in range(n)]

    for i in range(n):
        DP[i][0], DP[i][1] = 1, 1

    res = 1

    for i in range(1, n):
        for j in range(0, i):
            # Extract real part from complex numbers
            if get_real(numbers[j]) < get_real(numbers[i]) and DP[i][0] < DP[j][1] + 1:#if the last element is greater than the previous one
                DP[i][0] = DP[j][1] + 1

            if get_real(numbers[j]) > get_real(numbers[i]) and DP[i][1] < DP[j][0] + 1:#if the last element is smaller than the previous one
                DP[i][1] = DP[j][0] + 1

        if res < max(DP[i][0], DP[i][1]):
            res = max(DP[i][0], DP[i][1])

    # Print the DP array
    print("DP array:")
    for row in DP:
        print(row)
    # Find the actual subsequence elements
    subsequence = []
    for i in range(n - 1, -1, -1):
        if DP[i][0] == res:
            subsequence.append(numbers[i])
            res -= 1
        elif DP[i][1] == res:
            subsequence.append(numbers[i])
            res -= 1

    return subsequence[::-1] #return reversed list


#UI
"""def read_complex_from_console(complex_numbers):#   WITTHOUT RETURN
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    complex_numbers.append(create_complex(real, imag))"""
def read_complex_from_console():
    input_str = input("Enter complex numbers: ")
    complex_str_list = input_str.split()

    complex_numbers = []
    for complex_str in complex_str_list:
        parts = complex_str.replace(' ', '').split('+')
        real_part = int(parts[0])
        imag_part = int(parts[1].replace('i', ''))

        complex_numbers.append(create_complex(real_part, imag_part))

    return complex_numbers


def display_complex_list(complex_list):
    for num in complex_list:
        print(to_str(num))

def display_property_result(property_func, numbers):
    result = property_func(numbers)
    print(f"Result: {result}")

def main():
    # Initialize 10 complex numbers
    complex_numbers = [
        create_complex(1, 2),
        create_complex(3, 5),
        create_complex(1, 4),
        create_complex(7, 8),
        create_complex(9, 10),
        create_complex(3, 4),
        create_complex(36, 48),
        create_complex(39, 80),
        create_complex(17, 18),
        create_complex(19, 20),
    ]

    while True:
        print("\nMenu:")
        print("1. Read a list of complex numbers (in z = a + bi form) from the console.")
        print("2. Display the entire list of numbers on the console.")
        print("3. Display the length and elements of a longest subarray of numbers where the difference between the modulus of consecutive numbers is a prime number.(naive)")
        print("4. Display the length and elements of a longest alternating subsequence, when considering each number's real part")
        print("0. Exit the application")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Read complex numbers and extend the list
            complex_numbers.extend(read_complex_from_console())
        elif choice == '2':
            display_complex_list(complex_numbers)
        elif choice == '3':
            display_property_result(prime_difference_subarray, complex_numbers)
        elif choice == '4':
            display_property_result(alternating_subsequence, complex_numbers)

        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
