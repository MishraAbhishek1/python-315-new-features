"""
Python 3.15: Profiling Example

Profiling helps us identify which functions
take more time to execute.
"""

# Function 1: Simulate some work.
def calculate_total():
    total = 0
    
    for number in range(1_000_000):
        
        total += number
    
    return total

# Function 2: Perform another calculation.
def calculate_squares():
    total = 0
    
    for  number in range(500_000):
        total += number * number
    
    return total


# Main Funcitons calls both calculations
def main():
    print("starting calculations....")
    
    result1 = calculate_total()
    result2 = calculate_squares()
    
    print("Total", result1)
    print("Squares total:", result2)

if __name__ == "__main__":
    main()