def get_user_numbers():
    """
    Prompts the user to enter numbers until a blank input is provided.
    Returns a list of all entered numbers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)  
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    return user_numbers


def count_nums(num_lst):
    """
    Takes a list of numbers and returns a dictionary with the counts of each number.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  
    return num_dict


def print_counts(num_dict):
    """
    Prints the frequency of each number from the dictionary.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    """
    Main function to run the program:
    - Gets a list of user-entered numbers
    - Counts the frequency of each number
    - Prints the results
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
