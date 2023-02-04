def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid] #Guessed value
        if guess == target:
            return mid
        
        elif guess > target:
            end = mid -1
        
        else:
            start = mid + 1
        
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

