# Python program of above implementation
import random


def get_min_max(low, high, ints):
    arr_max = ints[low]
    arr_min = ints[low]

    # If there is only one element
    if low == high:
        arr_max = ints[low]
        arr_min = ints[low]
        return (arr_max, arr_min)
    # If there is only two element
    elif high == low + 1:
        if ints[low] > ints[high]:
            arr_max = ints[low]
            arr_min = ints[high]
        else:
            arr_max = ints[high]
            arr_min = ints[low]
        return (arr_max, arr_min)
    else:
        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = get_min_max(low, mid, ints)
        arr_max2, arr_min2 = get_min_max(mid + 1, high, ints)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))


def main():

    # Example Test Case of Ten Integers

    ints = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(ints)
    high = len(ints) - 1
    low = 0
    ints_max, ints_min = get_min_max(low, high, ints)
    print("Pass" if ((0, 9) == ints_max, ints_min) else "Fail")


if __name__ == "__main__":
    main()

# # Driver code
# arr = [1000, 11, 445, 1, 330, 3000]

# print('Minimum element is ', arr_min)
# print('nMaximum element is ', arr_max)

# # This code is contributed by DeepakChhitarka
