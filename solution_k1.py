def sum_negative_between_extremes(arr):
    if not arr:
        return 0

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    start = min(max_index, min_index)
    end = max(max_index, min_index)

    return sum(x for x in arr[start + 1:end] if x < 0)

# Пример массива:
A = [3, -4, 6, -2, -1, 8, -5]
result = sum_negative_between_extremes(A)
print("Сумма отрицательных между max и min:", result)
