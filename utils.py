def convert_to_int(s):
    try:
        float_value = float(s)  # Convert the string to a float
        int_value = int(float_value)
        return int_value
    except ValueError:
        print("Error")
        return None
    
def convert_to_time(ticks):
    time = ticks * 81e-12
    return time