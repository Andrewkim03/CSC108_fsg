from time import time 

def insertion_sort(arr) -> None:

    return None


def selection_sort(arr) -> None:

    return None


lst = [i for i in range(100)]


# Measure time for Insertion Sort
insertion_list = list.copy()
start_time = time()
insertion_sort(insertion_list)
insertion_sort_time = time() - start_time

# Measure time for Selection Sort
selection_list = list.copy()
start_time = time()
selection_sort(selection_list)
selection_sort_time = time() - start_time

# Results
print(f"Insertion Sort Time: {insertion_sort_time:.6f} seconds")
print(f"Selection Sort Time: {selection_sort_time:.6f} seconds")