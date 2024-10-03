def bubble_sort(list1):
    n = len(list1)  # Corrected assignment
    
    for i in range(n):  # Outer loop to ensure the pass through the entire list
        for j in range(n-i-1):  # Inner loop for comparison
            if list1[j] > list1[j+1]:  # Swap if the element is greater than the next
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapped = True
                # import pdb; pdb.set_trace()
        if not swapped:        
            break  # Return the sorted list
    return list1
# Example usage
list1 = [1, 9, 3, 4, 2]
sorted_list = bubble_sort(list1)
print(sorted_list)
