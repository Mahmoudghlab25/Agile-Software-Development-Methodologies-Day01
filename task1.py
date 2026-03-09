def get_sum_from_string(operation_str):
    """
    This function takes a raw addition formula, tries to split them 
    by '+' operator, convert both sides into integers 
    and return their summation.
    
    params:
    1) @operation_str: the raw string that represents the summation operation
    return:
    1) @summation: the sum of both sides in the operation_str.
    """
    summation = 0  # Initialize to provide a default return value
    try:
        # Split the string and strip whitespace
        lhs, rhs = operation_str.split('+')
        lhs = lhs.strip()
        rhs = rhs.strip()
        
        # Convert to integers and calculate sum
        summation = int(lhs) + int(rhs)
        
    except ValueError:
        print("Error: Ensure the string contains exactly one '+' and two valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return summation