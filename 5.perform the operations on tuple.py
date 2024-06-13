def main():
    
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (6, 7, 8, 9, 10)
    concatenated_tuple = tuple1 + tuple2   
    element_to_find = 3
    element_to_count = 3
    try:
        index_of_element = concatenated_tuple.index(element_to_find)
    except ValueError:
        index_of_element = None
    count_of_element = concatenated_tuple.count(element_to_count)
    print("Concatenated Tuple:", concatenated_tuple)
    if index_of_element is not None:
        print(f"Index of element {element_to_find}:", index_of_element)
    else:
        print(f"Element {element_to_find} is not in the tuple")
    print(f"Count of element {element_to_count}:", count_of_element)
if __name__ == "__main__":
    main()
