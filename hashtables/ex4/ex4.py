def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums = {}
    result = []

    for number in a:
        nums[number] = 1

        # if the opposite value is not in the list
        if number != 0 and -number in nums: 
            result.append(abs(number))

    return result



 


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))