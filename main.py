def main():
    print("Hello, World!")
    
    # Do whatever - a simple example
    for i in range(5):
        print(f"Counting: {i}")
    
    # Perform some basic operations
    result = calculate_sum(10, 20)
    print(f"The sum is: {result}")
    
    # Create and manipulate a list
    my_list = create_list(5)
    print(f"Created list: {my_list}")
    print(f"Reversed list: {reverse_list(my_list)}")

def calculate_sum(a, b):
    return a + b

def create_list(size):
    return [i * 2 for i in range(size)]

def reverse_list(lst):
    return lst[::-1]

if __name__ == "__main__":
    main()