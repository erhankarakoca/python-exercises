"""
    that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not
    suitable for large data sets as its average and worst-case time complexity is quite high.
    The complexity is O(n^2)
"""


def buble_sort(array):

    swapped = False

    for i in range(len(array)-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place

        for j in range(0, len(array)-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return array

    return array


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

    print(buble_sort(input_array))


if __name__ == "__main__" :
    main()