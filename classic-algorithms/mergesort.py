"""
    Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray,
    and then merging the sorted subarrays back together to form the final sorted array. In simple terms, we can say that
    the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves
    back together. This process is repeated until the entire array is sorted.
    The complexity of the function is O(n*logn) --> starts with the merge step in while it visits n items and
    log n comes from the binary tree we create which is on the order of log n.
"""
import random


def merge(sub_array0, sub_array1):
    """
    Merges two array with sorting
    :return: merged array
    """

    merged_array = []

    while sub_array1 and sub_array0:
        if sub_array0[0] <= sub_array1[0]:
            merged_array.append(sub_array0.pop(0))
        else:
            merged_array.append(sub_array1.pop(0))

    merged_array.extend(sub_array0)
    merged_array.extend(sub_array1)

    return merged_array

def merge_sort(array):
    """
    This is recursive function that divides array and sends to the merge
    :return: marge (arrayOne, arrayTwo)
    """
    if len(array) <= 1:
        return array

    # random selection to prevent dead loop for special sequences (???)
    rand_item = array[random.randint(0, len(array) - 1)]
    left, mid, right = [], [], []

    for item in array:
        if item < rand_item:
            left.append(item)
        elif item == rand_item:
            mid.append(item)
        else:
            right.append(item)

    left = merge_sort(left)
    left.extend(mid)
    right = merge_sort(right)
    return merge(left, right)


def main():
    """
    Take the user input
    """

    input_array = []
    try:
        while True:
            input_array.append(int(input("Please enter a element.(strings finishes the process)")))
    # if the input is not-integer, just print the list
    except:
        print(input_array)

    # Another method
    # lst1 = [int(item) for item in input("Enter the list items : ").split()]
    # print(lst1)

    print(merge_sort(input_array))


if __name__ == "__main__":
    main()
