# Initialize array
arr = [5, 2, 8, 7, 1]

# Display elements of the original array
print("Elements of original array: ")
for i in arr:
    print(i, end=" ")

# Sort the array in ascending order
ascending_array = sorted(arr)

# Display elements of the array after sorting in ascending order
print("\n\nElements of array sorted in ascending order: ")
for i in ascending_array:
    print(i, end=" ")

# Sort the array in descending order
descending_array = sorted(arr, reverse=True)

# Display elements of the array after sorting in descending order
print("\n\nElements of array sorted in descending order: ")
for i in descending_array:
    print(i, end=" ")
