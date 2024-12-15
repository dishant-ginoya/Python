# # ------- Division Calculator with Error Handling -------
# #   Create a simple division calculator that takes two numbers as input from the user and divides the first number by the second.
# #   Implement error handling using try-except to manage possible errors that could occur during the input or division process.
# #
# # Instructions:
# # 1.) Input Handling:
# #       Ask the user to input two numbers.
# #       Ensure the inputs are valid numbers.
# #
# # 2.) Division Logic:
# #       Divide the first number by the second number.
# #
# # 3.) Error Handling:
# #      Use a try-except block to catch and handle the following exceptions:
# #         i.) ValueError: Raised when the input is not a number.
# #         ii.) ZeroDivisionError: Raised when the user tries to divide by zero.
# #      General Exception: Catch any other unexpected errors.
# #
# # 4.) Output:
# #      If the division is successful, print the result.
# #      If an error occurs, print an appropriate error message.
# #
# #  -------------------
# # TEST CASE :-
# #     Enter the first number: 10
# #     Enter the second number: 2
# #     The result of 10 / 2 is 5.0
# # -------------------
# #     Enter the first number: 10
# #     Enter the second number: 0
# #     Error: Division by zero is not allowed.
# # -------------------
# #     Enter the first number: ten
# #     Enter the second number: 2
# #     Error: Please enter valid numbers.

# # ========================================================================================================== # #


def division_calculator(num1, num2):
    try:
        result = float(num1) / float(num2)
        print(f'\n  The result of {int(num1)} / {int(num2)} is {result}')

    except ValueError:
        print('\n Error: Please enter valid numbers.')

    except ZeroDivisionError:
        print('\n Error: Division by zero is not allowed.')

    except Exception as e:
        print(f'\n An unexpected error occurred: {e}')



number_1 = input('Enter the first number:- ')
number_2 = input('Enter the second number:- ')

division_calculator(number_1,number_2)
