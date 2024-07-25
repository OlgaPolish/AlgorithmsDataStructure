def kth(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]

    if len(arr2) == 0:
        return arr1[k]

    mid1 = len(arr1) // 2
    mid2 = len(arr2) // 2

    if mid1 + mid2 < k:
        if arr1[mid1] > arr2[mid2]:
            return kth(arr1, arr2[mid2 + 1:], k - mid2 - 1)
        else:
            return kth(arr1[mid1 + 1:], arr2, k - mid1 - 1)
    else:
        if arr1[mid1] > arr2[mid2]:
            return kth(arr1[:mid1], arr2, k)
        else:
            return kth(arr1, arr2[:mid2], k)


def kthElement(arr1, arr2, k):
    return kth(arr1, arr2, k - 1)

arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]

print(kthElement(arr1, arr2, 7))