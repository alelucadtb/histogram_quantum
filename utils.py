def find_min_diff(vector, a):
    # Check if the vector is empty
    if not vector:
        return None, None
    
    # Initialize variables for the minimum difference and nearest element
    min_diff = 10**18
    closest_element = None
    index_min = -1

    # Iterate through the vector
    for index, b in enumerate(vector):
        diff = abs(a - b)
        if diff < min_diff:
            min_diff = diff
            closest_element = b
            index_min = index
    
    return min_diff, index_min


def convert_to_int(s):
    try:
        float_value = float(s)  # Convert the string to a float
        int_value = int(float_value)
        return int_value
    except ValueError:
        print("Error")
        return None