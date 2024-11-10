# sorting algorithm version 2

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
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_half = merge_sort(unsorted_list[:middle])
    right_half = merge_sort(unsorted_list[middle:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    pivot = unsorted_list[len(unsorted_list) // 2] 
    left = [x for x in unsorted_list if x < pivot]
    middle = [x for x in unsorted_list if x == pivot]
    right = [x for x in unsorted_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# a function to track the time each iteration of the algorithm
def time_tracker(algorithm, data):
    start_time = time.perf_counter()
    algorithm(data)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time

def print_results(times_dict):
    for algorithm, times in times_dict.items():
        print(f"\n{algorithm} - Random Data Set:")
        print([f"{time:.6f}" for time in times[0::3]])  # Print every third item starting from index 0
        
        print(f"{algorithm} - Sorted Small to Big Data Set:")
        print([f"{time:.6f}" for time in times[1::3]])  # Print every third item starting from index 1
        
        print(f"{algorithm} - Sorted Big to Small Data Set:")
        print([f"{time:.6f}" for time in times[2::3]])  # Print every third item starting from index 2

              
def main():
    # associate name to algorithm
    sorting_algorithms = {"Bubble Sort": bubble_sort, 
                          "Selection Sort": selection_sort,
                          "Insertion Sort": insertion_sort,
                          "Merge Sort": merge_sort,
                          "Quick Sort": quick_sort
                          }
    
    # create a dictionary for each algorithm name
    times_dict = {name: [] for name in sorting_algorithms.keys()}

    # loops through to change the size of the dataset
    for size in range(1,11):
        random_data = [random.randint(1,10000) for i in range(1000*size)]
        sorted_small_to_big = [i for i in range(1000*size)]
        sorted_big_to_small = [i for i in range(1000*size,0,-1)]
        print(f"\nTesting on dataset size: {1000*size}")

        # iterates through each algorithm on 3 different datasets
        for name, algorithm in sorting_algorithms.items():
            print(f"{name} - Random Data Set")
            total_time = time_tracker(algorithm, random_data)
            print(f"Total Time: {total_time:.6f} seconds")
            times_dict[name].append(total_time)
            
            print(f"{name} - Sorted Small to Big Data Set")
            total_time = time_tracker(algorithm, sorted_small_to_big)
            print(f"Total Time: {total_time:.6f} seconds")
            times_dict[name].append(total_time)
            
            print(f"{name} - Sorted Big to Small Data Set")
            total_time = time_tracker(algorithm, sorted_big_to_small)
            print(f"Total Time: {total_time:.6f} seconds")
            times_dict[name].append(total_time)
        
    print_results(times_dict)
if __name__ == "__main__":
    main()