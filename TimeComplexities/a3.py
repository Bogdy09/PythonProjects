import random
import timeit

def generate_random_natural_numbers(n):
    if n < 0 or n>100:
        print("Please enter a number between 0 and 100")
        return

    natural_numbers = random.sample(range(101), n)  # Generate a list of n random natural numbers between 0 and 100

    return natural_numbers

def ascending_cocktailSort(a, step):
   # nr = 0
    #if step==0:
      #  return a
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False  # it means that it is not yet fully sorted

        for i in range(start, end):  # a loop from left to right at the end of which the greatest number will be on its final position
            if (a[i] > a[i + 1]):  # we sort it in an ascending order
                swapped=True
               # nr += 1
                a[i], a[i + 1] = a[i + 1], a[i]
               # if nr == step:
                  #  return a

        if (swapped == False):  # if nothing moved, then array is sorted.
            break

        swapped = False  # if we did not exit the program the list is not sorted yet

        end = end - 1  # since the greatest number is in the right place we move the end point back by one

        for i in range(end - 1, start - 1, -1):  # now we do the same thing, but from right to left
            if (a[i] > a[i + 1]):
                swapped=True
#                nr += 1
                a[i], a[i + 1] = a[i + 1], a[i]
                #if nr == step:
                  #  return a

        start = start + 1  # since the smallest number is in the right place we increase the starting point

    return a  # Return the partially sorted list

def number_of_steps_CocktailSort(a): #same sorting but we use it for simply calculating the number of steps that will take place for the random list
    nr=0
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False  # it means that it is not yet fully sorted

        for i in range(start, end):  # a loop from left to right at the end of which the greatest number will be on its final position
            if (a[i] > a[i + 1]):  # we sort it in an ascending order
                nr+=1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if (swapped == False):  # if nothing moved, then array is sorted.
            break

        swapped = False  # if we did not exit the program the list is not sorted yet

        end = end - 1  # since the greatest number is in the right place we move the end point back by one

        for i in range(end - 1, start - 1, -1):  # now we do the same thing, but from right to left
            if (a[i] > a[i + 1]):
                nr+=1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start = start + 1  # since the smallest number is in the right place we increase the starting point
    return nr

def ascending_gnomeSort(a, n, step1):
    index = 0  # Initialize the index to start sorting
   # k = 0  # Initialize the step counter

    while index < n:  # Continue sorting until the index reaches the end
        if index == 0:  # If at the beginning of the list, move to the next element
            index = index + 1

        if a[index] >= a[index - 1]:  # If two elements are in the correct order
            index = index + 1  # Move to the next element
        else:
          #  k += 1  # Increment the step counter
            a[index], a[index - 1] = a[index - 1], a[index]  # Swap the current and previous elements

          #  if k == step1:  # If the specified step is reached
              #  return a  # Return the partially sorted list

            index = index - 1  # Move back to the previous element

    return a  # Return the fully sorted list


def number_of_steps_GnomeSort(a, n): #same sorting but we use it for simply calculating the number of steps that will take place for the random list
    index = 0
    k = 0
    while index < n:
        if index == 0:
            index = index + 1
        if a[index] >= a[index - 1]:
            index = index + 1
        else:
            k += 1
            a[index], a[index - 1] = a[index - 1], a[index]
            index = index - 1
    return k

def generate_random_list(length):
    return [random.randint(1, 10000) for _ in range(length)]

def generate_sorted_list(length, scenario):
    if scenario == "best":
        return list(range(1, length + 1)) #ascending list
    elif scenario == "average":
        return generate_random_list(length)  #I am using my random list generation function for the average case
    elif scenario == "worst":
        return list(range(length, 0, -1)) #descending list
    else:
       print("Invalid scenario")
       return []




while True: # we create the selection menu
    print("1. Generate a list of n random natural numbers between 0 and 100.")
    print("2. Sort the list using the cocktail sort.")
    print("3. Sort the list using the gnome sort.")
    print("4. Display the best case runtime for CocktailSort and GnomeSort.")
    print("5. Display the average case runtime for CocktailSort and GnomeSort.")
    print("6. Display the worst case runtime for CocktailSort and GnomeSort.")
    print("0. Exit the program")

    option=input("Choose what you want the program to do(a number between 0 and 6)")

    if option=="1": #we use the function for generating random numbers
        n = int(input("Enter the number of random natural numbers to generate(between 0 and 100): "))
        random_natural_numbers = generate_random_natural_numbers(n)
        print("Random Natural Numbers:", random_natural_numbers)
        copy_list = random_natural_numbers.copy()  # we use a copy
        copy_list1 = random_natural_numbers.copy()  # we use a copy

    elif option == "2":
        if 'random_natural_numbers' not in locals(): #if we did not generate the numbers, we must do that first
            print("Please generate a list of random natural numbers first.")
        else:
            number = number_of_steps_CocktailSort(copy_list)
            step = int(input("Enter the number of steps after which you want to see the partially sorted list, between 0 and {} (if you choose a bigger number it means that the list will be fully sorted): ".format( number))) #we choose a number of steps between 0 and the maximum number of steps that the function does
            if step<0:
                print("Please choose a number greater then 0")
                break
            partially_sorted_list = ascending_cocktailSort(list(random_natural_numbers), step)
            print("Partially sorted list after {} steps with CocktailSort: {}".format(step, partially_sorted_list))
            random_natural_numbers=partially_sorted_list.copy()
            copy_list=partially_sorted_list.copy() #we use this to make the partially sorted list the new original list for subsequent iterations.
    elif option=="3":
        if 'random_natural_numbers' not in locals(): #if we did not generate the numbers, we must do that first
            print("Please generate a list of random natural numbers first.")
        else:
            number1=number_of_steps_GnomeSort(copy_list1, n)
            step1 = int(input( "Enter the number of steps after which you want to see the partially sorted list, between 0 and {} (if you choose a bigger number it means that the list will be fully sorted): ".format( number1))) #we choose a number of steps between 0 and the maximum number of steps that the function does
            if step1<0:
                print("Please choose a number greater then 0")
                break
            partially_sorted_list1=ascending_gnomeSort(list(random_natural_numbers), n, step1)
            print("Partially sorted list after {} steps with GnomeSort: {}".format(step1, partially_sorted_list1))
            random_natural_numbers = partially_sorted_list1.copy()
            copy_list1 = partially_sorted_list1.copy() #we use this to make the partially sorted list the new original list for subsequent iterations.

    elif option=="4":
        list_lengths = [500, 1000, 2000, 4000, 8000]
        for length in list_lengths:
            best_case_list = generate_sorted_list(length, "best") #for the best case scenario we are using a list sorted in ascending order

            duration_cocktail = timeit.timeit(lambda: ascending_cocktailSort(best_case_list, len(best_case_list)-1), number=1) # we use timeit to calculate the runtime

            duration_gnome = timeit.timeit(lambda: ascending_gnomeSort(best_case_list, length, step1=0), number=1)

            print(f"Best Case:")
            print(f"Time taken to sort a list with CocktailSort of length {length}: {duration_cocktail:.6f} seconds")
            print(f"Time taken to sort a list with GnomeSort of length {length}: {duration_gnome:.6f} seconds")

    elif option=="5":
        list_lengths = [500, 1000, 2000, 4000, 8000]
        for length in list_lengths:
            random_list = generate_random_list(length)

            # Measuring average-case runtime for CocktailSort
            duration_cocktail_average = timeit.timeit(lambda: ascending_cocktailSort(random_list, len(random_list) - 1), number=1)


            # Measuring average-case runtime for GnomeSort
            duration_gnome_average = timeit.timeit(lambda: ascending_gnomeSort(random_list, length, step1=0), number=1)

            print(f"Average Case:")
            print(f"Time taken to sort a list with CocktailSort of length {length}: {duration_cocktail_average:.6f} seconds")
            print(f"Time taken to sort a list with GnomeSort of length {length}: {duration_gnome_average:.6f} seconds")

    elif option=="6":
        list_lengths = [500, 1000, 2000, 4000, 8000]
        for length in list_lengths:
            worst_case_data = generate_sorted_list(length, "worst")

            # Measuring worst-case runtime for CocktailSort
            duration_cocktail_worst = timeit.timeit(lambda: ascending_cocktailSort(worst_case_data, len(worst_case_data) - 1), number=1)

            worst_case_data = generate_sorted_list(length, "worst")
            # Measuring worst-case runtime for GnomeSort
            duration_gnome_worst = timeit.timeit(lambda: ascending_gnomeSort(worst_case_data, length, step1=0),number=1)

            print(f"Worst Case:")
            print(f"Time taken to sort a list with CocktailSort of length {length}: {duration_cocktail_worst:.6f} seconds")
            print(f"Time taken to sort a list with GnomeSort of length {length}: {duration_gnome_worst:.6f} seconds")

    elif option == "0": #we exit the program
        print("Thanks for your patience!")
        break
    else:
        print("Please enter a valid number(between 0 and 6)") #if the number option does not exist


"""

Theorethical Part:

For CockTail Sort, we have:

Best Case: 

The best case complexity for the CockTail sort is O(n), and it happens when the list is already sorted.
That is, because if the list is already sorted, then the function only goes in the first for loop a single time, taking n steps.

Worst Case: 

The worst case complexity for the CockTail sort is O(n^2), and it happens when the list is sorted in a reverse order.
For example, if you wanted to sort it in an ascending order, and the list was in descending order, that would be the worst case complexity.
That is, because when it is sorted in reverse order it makes the most swaps(n swaps n times)

For Gnome Sort, we have:

Best Case:

The best case complexity for the Gnome sort is O(n), and it happens when the list is already sorted.
That is, because if the list is already sorted, then the function makes n-1 comparisons and 0 swaps.

Worst Case:

The worst case complexity for the Gnome sort is O(n^2), and it happens when the list is sorted in a reverse order.
In this case, the Gnome sort will perform the maximum number of swaps and comparisons(it makes approximately n swaps n times).

"""

