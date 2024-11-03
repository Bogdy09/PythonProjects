# find the greatest number formed by a number's digit
def greatest_number(x):
    digit_list = []

    def merge_sort(arr):
        if len(arr)<=1:
            return arr

        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        left_sorted=merge_sort(left)
        right_sorted=merge_sort(right)

        return merge_sort_helper(left_sorted, right_sorted)

    def merge_sort_helper(left, right):
        i=j=0
        sorted_list=[]
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                sorted_list.append(left[i])
                i+=1
            else:
                sorted_list.append(right[j])
                j+=1
        while i<len(left):
            sorted_list.append(left[i])
            i+=1

        while j<len(right):
              sorted_list.append(right[j])
              j+=1

        return sorted_list

    while x > 0: #we add to the list the digits of the number and sort them in a descending order with the previous function
        digit_list.append(x % 10)
        x = x//10
        final_list=merge_sort(digit_list)
    y = 0
    for i in range(0, len(final_list)): #we create a new number with the digits in descending order(thus creating the greatest number formed by your number's digits
        y = y * 10 + final_list[i]
    return y
def main():
    x = int(input("Write a natural number:"))
    result=greatest_number(x)
    print("The greatest number formed by your number's digits is:", result)
if __name__ == "__main__":
    main()
