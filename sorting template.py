# Sorting template
import random

def bubble_sort(unsorted_list):
    # Your code goes here

def selection_sort(unsorted_list):
    # Your code goes here

def insertion_sort(unsorted_list):
    # Your code goes here

def merge_sort(unsorted_list):
    # Your code goes here

def quick_sort(unsorted_list):
    # Your code goes here

def main():
    to_be_sorted = [random.randint(1,100) for i in range(100)]
    print("Bubble Sort")
    print(bubble_sort(to_be_sorted))
    print("Selection Sort")
    print(selection_sort(to_be_sorted))
    print("Insertion Sort")
    print(insertion_sort(to_be_sorted))
    print("Merge Sort")
    print(merge_sort(to_be_sorted))
    print("Quick Sort")
    print(quick_sort(to_be_sorted))

if __name__ == "__main__":
    main()