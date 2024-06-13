
def sum_of_numbers():
    n = int(input("Enter the number of integers you want to sum: "))
    total_sum = 0
    for i in range(n):
        number = int(input(f"Enter number {i+1}: "))
        total_sum += number
    print(f"The sum of the {n} numbers is: {total_sum}")
sum_of_numbers()
