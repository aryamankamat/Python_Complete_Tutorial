# Creating a bubble sort function
def bubble_sort(lst1):
    # Outer loop for traverse the entire list
    for i in range(0, len(lst1) - 1):
        for j in range(len(lst1) - 1):
            if lst1[j] > lst1[j + 1]:
                temp = lst1[j]
                lst1[j] = lst1[j + 1]
                lst1[j + 1] = temp
    return lst1


lst1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", lst1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(lst1))