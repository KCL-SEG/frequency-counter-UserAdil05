def frequencies(items):
    # Initialize an empty dictionary to store frequencies
    frequency_dict = {}

    # Iterate over each item in the list
    for item in items:
        # Convert the item to a string (if it's not already a string)
        item_str = str(item)

        # If the item is already in the dictionary, increment its count
        if item_str in frequency_dict:
            frequency_dict[item_str] += 1
        else:
            # Otherwise, add the item to the dictionary with a count of 1
            frequency_dict[item_str] = 1

    return frequency_dict

# Test the function with the provided examples
test1 = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
test2 = frequencies([100, 'Hello', '100', '100', 100])

