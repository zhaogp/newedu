def bubble_sort(a_list):
    size = len(a_list)
    for i in range(size-1):
        for j in range(size-i-1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

print(bubble_sort([23, 0.1, 2, -1, 9]))
