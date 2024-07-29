def find_closest_element(vector, a):
    # Check if the vector is empty
    if not vector:
        return None
    
    # Initialize variables for the minimum difference and nearest element
    min_diff = float('inf') 
    closest_element = None
    
    # Itera through the vector
    for b in vector:
        diff = abs(a - b)
        if diff < min_diff:
            min_diff = diff
            closest_element = b
    
    return min_diff


def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        print(f"Errore: '{s}' non è un numero valido.")
        return None