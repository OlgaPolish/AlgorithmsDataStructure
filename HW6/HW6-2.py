def quick_sort_rec(arr):
    stack = []

    def part_sort(left, right):
        if right-left <= 1:
            return
        mid = (left + right) // 2
        sep = arr[mid]
        i = left
        j = right
        while True:
            while arr[i] < sep:
                i += 1
            while arr[j] > sep:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            if i > j:
                stack.append((left, j))
                stack.append((i, right))
                return
    stack.append((0, len(arr) - 1))
    print(stack)
    while True:
        if len(stack) == 0:
            return arr
        (l, r) = stack.pop()
        part_sort(l, r)


arrya = [3, 5, 4, 1, 8, 3, 9, 0, 2, 7, 6]
print(quick_sort_rec(arrya))
