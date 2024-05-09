def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    fnd = arr[-1]
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        y = arr[mid]

        if fnd > y >= x:
            fnd = y

        if y < x:
            low = mid + 1

        elif y > x:
            high = mid - 1

        else:
            return iterations, fnd

    return iterations, fnd


ls = [i / 10 for i in range(0, 100, 3)]

print(ls)
# [0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7, 6.0, 6.3, 6.6, 6.9, 7.2, 7.5, 7.8, 8.1, 8.4, 8.7, 9.0, 9.3, 9.6, 9.9]


print(binary_search(ls, 0.0))
# (5, 0.0)

print(binary_search(ls, 4.2))
# (5, 4.2)

print(binary_search(ls, 5))
# (5, 5.1)

print(binary_search(ls, 9.7))
# (6, 9.9)

print(binary_search(ls, 9.9))
# (6, 9.9)

print(binary_search(ls, -10))
# (5, 0.0)

print(binary_search(ls, 10))
# (6, 9.9)
