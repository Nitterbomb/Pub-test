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
    print("Bubble Sort")
    start_time = time.time()
    print(bubble_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Selection Sort")
    start_time = time.time()
    print(selection_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Insertion Sort")
    start_time = time.time()
    print(insertion_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Merge Sort")
    start_time = time.time()
    print(merge_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")

    print("Quick Sort")
    start_time = time.time()
    print(quick_sort(to_be_sorted))
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.6f} seconds\n")
    
if __name__ == "__main__":
    main()
