def merge_sort(array):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(array) <= 1:
        return
    
    # Divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively apply merge_sort to the left and right halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Merge the sorted left and right halves back into the original array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Compare elements from left and right halves and merge them in sorted order
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # If there are remaining elements in the left or right half, add them to the sorted array
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    # Example usage
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Display the unsorted array
    print('Unsorted array: ')
    print(numbers)
    
    # Perform merge sort on the array
    merge_sort(numbers)
    
    # Display the sorted array
    print('Sorted array: ' + str(numbers))
  
