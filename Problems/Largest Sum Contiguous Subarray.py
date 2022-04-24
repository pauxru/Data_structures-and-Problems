Array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_sequence(arr):
    """
    Take an array and return the sum of the
    sub-array with most of valued sum
    :param arr: the give array
    :return: sum of the largest sub-array
    """

    max_seq = 0
    if len(arr) > 0:  # Catch empty array
        max_seq = arr[0]
    else:
        return 0
    curr_max = 0

    for num in range(len(arr)):
        curr_max = curr_max + arr[num]
        if curr_max < 0:
            curr_max = 0
        else:
            if curr_max > max_seq:
                max_seq = curr_max
    if max_seq < 0:
        return 0  # catch where all nums are negative
    return max_seq


print(max_sequence(Array))
