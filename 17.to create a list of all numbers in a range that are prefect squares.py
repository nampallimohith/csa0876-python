def perfect_squares_in_range(start, end):

    start = max(start, 0)
    
 
    perfect_squares = [x*x for x in range(int(start ** 0.5) + 1, int(end ** 0.5) + 1)]

    return perfect_squares

# Example usage:
start_range = 1
end_range = 25
perfect_squares_list = perfect_squares_in_range(start_range, end_range)
print("Perfect squares within the range", start_range, "to", end_range, "are:", perfect_squares_list)
