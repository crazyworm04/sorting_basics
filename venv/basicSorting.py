import timeit
import functools
import random


def bubble_sort(sort_list):  # Bubble sort function
    for i in range(0, len(sort_list) - 1):
        for j in range(0, len(sort_list) - 1):
            if sort_list[j] > sort_list[j + 1]:
                temp = sort_list[j]
                sort_list[j] = sort_list[j + 1]
                sort_list[j + 1] = temp
    return sort_list


def insertion_sort(sort_list):  # Insertion sort function
    for i in range(len(sort_list)):
        list_key = sort_list[i]
        j = i - 1
        while j >= 0 and sort_list[j] > list_key:
            sort_list[j + 1] = sort_list[j]
            j = j - 1
        sort_list[j + 1] = list_key
    return sort_list


def selection_sort(sort_list):  # Selection sort function
    for i in range(len(sort_list) - 1):
        lowest_value = i
        for j in range(i + 1, len(sort_list)):
            if sort_list[lowest_value] > sort_list[j]:
                lowest_value = j
        temp = sort_list[lowest_value]
        sort_list[lowest_value] = sort_list[i]
        sort_list[i] = temp
    return sort_list


def random_data(size):      # Generate random list of integers between 1 and 100 of size specified
    try:
        return random.sample(range(1, 101), size)
    except ValueError:
        print("Amount of list values exceeds the possible boundary")


print(selection_sort(random_data(10)))
for j in range(10, 101, 10):
    bubble_time = timeit.Timer(functools.partial(bubble_sort, random_data(j)))
    insertion_time = timeit.Timer(functools.partial(insertion_sort, random_data(j)))
    selection_time = timeit.Timer(functools.partial(selection_sort, random_data(j)))
    print("The bubble sort took: {0} seconds to process list of size: {1}".format(bubble_time.timeit(1), j))
    print("The insertion sort took: {0} seconds to process list of size: {1}".format(insertion_time.timeit(1), j))
    print("The selection sort took: {0} seconds to process list of size: {1}".format(selection_time.timeit(1), j))
    print("=" * 40)
    print()
