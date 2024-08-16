#Day16 Python programming
#August 16, 2024

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

                

# Example usage
array = [1, 3, 83, 6, 2, 17]
bubble_sort(array)
print("Sorted array is:", array)

array1=[100, 56, 34, 3]
bubble_sort(array1)
print("Sorted array is:", array1)

array2=[1, 56, 204, 399]
bubble_sort(array2)
print(f"Sorted array is: {array2}")



array3=[500, 5, 20, 3, 0.3, 173, 30]
bubble_sort(array3)
print(f"Sorted array is: {array3}")

