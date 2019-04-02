# import array

'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1]  should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''


def first_missing_positive(inputArray):
    if not inputArray:
        return 1

    for i, num in enumerate(inputArray):
        while i + 1 != inputArray[i] and 0 < inputArray[0] < len(inputArray):
            v = inputArray[i]
            inputArray[i], inputArray[v - 1] = inputArray[v - 1], inputArray[i]

            if inputArray[i] == inputArray[v - 1]:
                break

    for i, num in enumerate(inputArray, 1):
        if num != i:
            return i

    return len(inputArray) + 1


r1 = first_missing_positive([3, 4, -1, 1])
r2 = first_missing_positive([1, 2, 0])

assert r1, 2
assert r2, 3


input("\n\nPress any key to exit.\n")
