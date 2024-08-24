'''You are tasked with creating a Python program that serves as an interactive tool for a friend who
 enjoys exploring numbers. The program should begin by prompting the user to enter their name and 
 then ask them for three of their favorite numbers. After gathering this information, the program
  should greet the user with a personalized message that includes their name. The three numbers
provided by the user should be stored in a list. The program should then check if any of the
 numbers are even or odd, and store this information in a separate list of tuples, where each
 tuple contains the number and a string indicating whether it is "even" or "odd". Following this,
the program should use a for loop to iterate over the list of numbers, and for each number,
it should create a tuple containing the number and its square. These tuples should be printed
 in a creative and engaging format. Additionally, the program should calculate the sum of the three
 numbers and print the result, accompanied by an encouraging message. Finally, the program should
determine if the sum is a prime number and notify the user with an appropriate message. The goal
 is to make the tool both enjoyable and informative, allowing the user to explore their favorite
numbers in a fun and interactive way,
 while also introducing some interesting logical checks.'''

def get_favorite_numbers():
    """
    Prompts the user for their name and three favorite numbers.
    Returns a list containing the three favorite numbers.
    """
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's explore your favorite numbers.")
    favorite_numbers = []
    for i in range(3):
        number = float(input(f"Enter favorite number {i + 1}: "))
        favorite_numbers.append(number)
    return favorite_numbers

def classify_even_odd(numbers):
    """
    Given a list of numbers, classifies each number as "even" or "odd".
    Returns a list of tuples (number, classification).
    """
    classifications = []
    for num in numbers:
        classification = "even" if num % 2 == 0 else "odd"
        classifications.append((num, classification))
    return classifications

def print_number_and_square(numbers):
    """
    Prints each number and its square in an engaging format.
    """
    print("\nExploring your favorite numbers:")
    for num in numbers:
        square = num ** 2
        print(f"{num} squared is {square}")

def calculate_sum(numbers):
    """
    Calculates the sum of the provided numbers.
    Returns the sum.
    """
    total_sum = sum(numbers)
    print(f"\nThe sum of your favorite numbers is {total_sum}. Keep it up!")

    return total_sum

def is_prime(number):
    """
    Checks if a given number is prime.
    Returns True if prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    favorite_numbers = get_favorite_numbers()
    classifications = classify_even_odd(favorite_numbers)
    print_number_and_square(favorite_numbers)
    total_sum = calculate_sum(favorite_numbers)

    if is_prime(total_sum):
        print(f"\nWow, {total_sum} is a prime number! 🌟")
    else:
        print(f"\nKeep exploring! {total_sum} is not a prime number.")

if __name__ == "__main__":
    main()
