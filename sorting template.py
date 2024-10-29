# Sorting template
import random
import time

def bubble_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Your code goes here
    return sorted_list

def selection_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Your code goes here
    return sorted_list

def insertion_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Your code goes here
    return sorted_list

def merge_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Your code goes here
    return sorted_list

def quick_sort(unsorted_list):
    sorted_list = unsorted_list[:]
    # Your code goes here
    return sorted_list

def main():
    to_be_sorted = [random.randint(1,100) for i in range(100)]
    sorted_small_to_big = [i for i in range(100)]
    sorted_big_to_small = [i for i in range(100,0,-1)]
    
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
    print(merge_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Merge Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(merge_sort(sorted_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Merge Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(merge_sort(sorted_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Quick Sort - Random Data Set")
    start_time = time.time()
    print(quick_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Quick Sort - Sorted Small to Big Data Set")
    start_time = time.time()
    print(quick_sort(sorted_small_to_big))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    print("Quick Sort - Sorted Big to Small Data Set")
    start_time = time.time()
    print(quick_sort(sorted_big_to_small))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    
if __name__ == "__main__":
    main()
