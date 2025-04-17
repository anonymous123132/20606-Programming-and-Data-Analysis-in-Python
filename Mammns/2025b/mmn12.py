
"""
@Project: Maman12_Q2

@Description :The code contains several functions from Maman 12.

@ID : 325819951
@Author: Nataniel Shulkin
@semester : 2024b
"""



def is_prime(n):
    '''
    Determines if a given natural number is a prime number.

    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    This function checks whether the input number has any divisors other than 1 and itself
    by testing divisibility from 2 to n-1.

    Parameters:
    n (int): The natural number to be checked. Must be greater than 1.
    Returns:
    bool: True if the number is prime, False otherwise.
    '''
    for DivisionNumber in range(2, n):  # Iterate over all numbers from 2 to n-1
        if n % DivisionNumber == 0:  # Check if n is divisible by DivisionNumber without a remainder
            return False  # Return False if a divisor is found
    return True  # Return True if no divisors are found


def max_prime():
    '''
    Finds the largest prime number entered by the user.

    This function repeatedly accepts natural numbers from the user and checks
    if each number is a prime. If the number is prime and greater than the
    previously recorded largest prime, it updates the largest prime value.
    The process continues until the user enters a number less than or equal to 1.

    Args:
        None

    Returns:
        LargestNumber (int): The largest prime number entered by the user.
             Returns 1 if no prime numbers are entered.

    '''
    LargestNumber, CurrentNumber = 1, 1  # Initialize LargestNumber to 1 (as required) and CurrentNumber to 1

    while CurrentNumber > 1:
        CurrentNumber = int(input("Enter Number: "))  # Prompt user for input
        if is_prime(CurrentNumber) and CurrentNumber > LargestNumber:
            LargestNumber = CurrentNumber  # Update LargestNumber if CurrentNumber is a prime and greater than LargestNumber

    return LargestNumber  # Return the largest prime number found




def compression(WordToCheck):
    '''
    Compresses a string by replacing consecutive repeating characters with the character
    followed by the number of repetitions. Single characters are left unchanged.

    Args:
        WordToCheck (str): The input string to be compressed.

    Returns:
        FinalStr (str): The compressed string where consecutive characters are represented
             by the character followed by its count. Characters appearing only once are left unchanged.

    '''
    CountLetters = 1  # Counter for consecutive letters
    FinalStr = ''  # To store the final compressed string

    for i in range(1, len(WordToCheck)):  # Loop through the string starting from the second character
        if WordToCheck[i] == WordToCheck[i - 1]:  # Check if current character is the same as the previous one
            CountLetters += 1  # Increment count if characters are the same
        elif CountLetters == 1:  # If no repetition, add the character directly
            FinalStr += WordToCheck[i - 1]
            CountLetters = 1
        else:  # If repetition is found, add the character followed by the count
            FinalStr += WordToCheck[i - 1] + str(CountLetters)
            CountLetters = 1

    # Handle the last character(s) after the loop
    if WordToCheck[-1] == WordToCheck[-2]:
        FinalStr += WordToCheck[-1] + str(CountLetters)
    else:
        FinalStr += WordToCheck[-1]

    return FinalStr

def sum_square(num):
    """
    Calculates the sum of the squares of the digits in a given natural number.
    Parameters:
    num (int): A natural number (positive integer).
    Returns:
    int: The sum of the squares of the digits of `num`.
    """
    FinalNum = 0
    for digit in str(num):  # Convert number to string to iterate over digits
        FinalNum += int(digit) ** 2  # Convert digit to int and square it
    return FinalNum

def is_happy(num):
    """
    Checks if a number is a happy number. A happy number is a number that
    eventually reaches 1 when replaced repeatedly by the sum of the squares
    of its digits. The process is limited to 10 iterations.

    Parameters:
    num (int): A natural number to check if it's happy.

    Returns:
    bool: True if the number is happy, False otherwise.

    The function will return `True` if the number reaches 1 in 10 iterations,
    and `False` if the process takes more than 10 iterations without reaching 1.
"""
    if type(num) == type(1):  # Ensure that the input is a valid integer
        for i in range(1, 10):  # Limit to 10 iterations
            num = sum_square(num)  # Apply the sum_square function to the number
            if num == 1:  # If the number reaches 1, return True
                return True
        return False  # If the number doesn't reach 1 within 10 steps, return False

def count_happy_numbers():
    """
    Counts the number of happy numbers in the range from 1 to 100.

    A happy number is a number that eventually reaches 1 when replaced repeatedly by the sum of the squares of its digits.
    This function uses the `is_happy` function to check for happy numbers in the specified range.

    Returns:
    int: The number of happy numbers in the range from 1 to 100.
"""
    SumApprovedNumbers = 0  # Initialize the count of happy numbers
    for i in range(1, 101):  # Loop through the numbers from 1 to 100
        if is_happy(i):  # Check if the number is happy using the `is_happy` function
            SumApprovedNumbers += 1  # Increment the count if the number is happy
    return SumApprovedNumbers  # Return the total count of happy numbers





def main():
        """
        Tester for all functions in the assignment.
        Calls each function with multiple test cases and prints the results.
        """
        print("Question 1: Prime Number Functions")
        print("Testing is_prime:")
        print("is_prime(7):", is_prime(7))  # Expected: True
        print("is_prime(10):", is_prime(10))  # Expected: False

        print("\nTesting max_prime:")
        # Since max_prime requires user input, it should be tested manually
        print("Please test max_prime function manually due to input requirements.")

        print("\nQuestion 2: Compression Function")
        print("Testing compression:")
        print("compression('aabccceeeeedab'):", compression("aabccceeeeedab"))  # Expected: a2bc3e5dab
        print("compression('abcde'):", compression("abcde"))  # Expected: abcde
        print("compression('xxxyyyzzz'):", compression("x3y3z3"))  # Expected: x3y3z3

        print("\nQuestion 3: Happy Numbers")
        print("Testing sum_square:")
        print("sum_square(123):", sum_square(123))  # Expected: 14
        print("sum_square(98):", sum_square(98))  # Expected: 145

        print("\nTesting is_happy:")
        print("is_happy(19):", is_happy(19))  # Expected: True
        print("is_happy(2):", is_happy(2))  # Expected: False

        print("\nTesting count_happy_numbers:")
        print("count_happy_numbers():", count_happy_numbers())  # Expected: 20


if __name__ == "__main__":
    main()


