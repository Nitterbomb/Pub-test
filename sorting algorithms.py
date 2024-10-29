# Sorting template
import random
import time

def bubble_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    sort_count = 1
    while sort_count != 0:
        sort_count = 0
        for index in range(0, len(sorted_list)-1):
            if sorted_list[index] > sorted_list[index+1]:
                temp_storage = sorted_list[index]
                sorted_list[index] = sorted_list[index+1]
                sorted_list[index+1] = temp_storage
                sort_count += 1
    return sorted_list

def selection_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for index in range(len(sorted_list)):
        min_index = index
        for index_2 in range(index, (len(sorted_list))):
            if sorted_list[min_index] > sorted_list[index_2]:
                min_index = index_2
        temp_storage = sorted_list[index]
        sorted_list[index] = sorted_list[min_index]
        sorted_list[min_index] = temp_storage
    return sorted_list

def insertion_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    for index in range(1,len(sorted_list)):
        for index_2 in range(0,index):
            if sorted_list[index] < sorted_list[index_2]:
                temp_storage = sorted_list[index_2]
                sorted_list[index_2] = sorted_list[index]
                sorted_list[index] = temp_storage
    return sorted_list

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = merge_sort(unsorted_list[:mid])
        right = merge_sort(unsorted_list[mid:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_list[k] = right[j]
            j += 1
            k += 1
    return unsorted_list

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list[len(unsorted_list) // 2] 
        left = []
        middle = []
        right = []

        for x in unsorted_list:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return quick_sort(left) + middle + quick_sort(right)

def main():
    to_be_sorted = [random.randint(1,100) for i in range(100)]
    sorted_small_to_big = [i for i in range(100)]
    sorted_big_to_small = [i for i in range(100,0,-1)]
    merge_sort_to_be_sorted = to_be_sorted
    merge_sort_small_to_big = sorted_small_to_big
    merge_sort_big_to_small = sorted_big_to_small
    quick_sort_to_be_sorted = to_be_sorted
    quick_sort_small_to_big = sorted_small_to_big
    quick_sort_big_to_small = sorted_big_to_small
    print("Bubble Sort - Random Data Set")
    start_time = time.time()
    print(bubble_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Bubble Sort - Small to Big Sorted Data Set")
    start_time = time.time()
    print(bubble_sort(sorted_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Bubble Sort - Big to Small Sorted Data Set")
    start_time = time.time()
    print(bubble_sort(sorted_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Selection Sort - Random Data Set")
    start_time = time.time()
    print(selection_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Selection Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(selection_sort(sorted_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Selection Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(selection_sort(sorted_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Insertion Sort - Random Data Set")
    start_time = time.time()
    print(insertion_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Insertion Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(insertion_sort(sorted_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Insertion Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(insertion_sort(sorted_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Merge Sort - Random Data Set")
    start_time = time.time()
    print(merge_sort(merge_sort_to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Merge Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(merge_sort(merge_sort_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Merge Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(merge_sort(merge_sort_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Quick Sort - Random Data Set")
    start_time = time.time()
    print(quick_sort(quick_sort_to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Quick Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(quick_sort(quick_sort_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Quick Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(quick_sort(quick_sort_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    
if __name__ == "__main__":
    main()