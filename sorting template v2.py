# sorting algorithm template v2

import random
import time

def bubble_sort(unsorted_list):
    # write your code here
    return sorted_list

def selection_sort(unsorted_list):
    # write your code here
    return sorted_list

def insertion_sort(unsorted_list):
    # write your code here
    return sorted_list

def merge_sort(unsorted_list):
    # write your code here
    # there is also a helper function below if necessary
    return merge(left_half, right_half)

def merge(left, right):
    # write your code here
    return sorted_list

def quick_sort(unsorted_list):
    # write your code here
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