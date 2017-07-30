def bubble_sort(a_list):
    """Bubble sorting"""
    size = len(a_list)
    for i in range(size-1):
        for j in range(size-i-1):
            if a_list[j+1] < a_list[j]:
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
    print('After sorting: ', a_list)
    print(bubble_sort.__doc__)

test_list = [100000000, 0.1, -0.100001, 23, 1.2, -3, 0, -100]

bubble_sort(test_list)
