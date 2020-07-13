def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    count = {}

    for array in arrays:
        for number in array:
            if number in count:
                count[number] += 1
            
            else:
                count[number] = 1

    result = [item[0] for item in count.items() if item[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))