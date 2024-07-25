import sys
import numpy as np


def merge_array(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

j = len(sys.argv)-1
i = 3
array_1 = np.load(sys.argv[1])
array_2 = np.load(sys.argv[2])
result_array = merge_array(array_1, array_2)
while i<= j:
    array_2 = np.load(sys.argv[i])
    result_array = merge_array(result_array,array_2)
    i += 1
print(result_array)



