#! usr/bin/env python3


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such
    that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list.sort(reverse=True)
    x = 0
    for i in range(0, len(input_list), 2):
        x = x * 10 + input_list[i]
    y = 0
    for i in range(1, len(input_list), 2):
        y = y * 10 + input_list[i]
    return [x, y]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def main():

    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test_function(test_case)


if __name__ == "__main__":
    main()
