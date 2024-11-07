import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within a specified range.
    
    Parameters:
        min_value (int): The minimum value in the range.
        max_value (int): The maximum value in the range.
        
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Randomly selects a mathematical operator for the quiz.
    
    Returns:
        str: A random operator from the list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def create_problem(num1, num2, operator):
    """
    Creates a math problem as a string and calculates its answer based on the operator.
    
    Parameters:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator to use ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Main function to conduct the math quiz game. Presents math problems to the user and 
    keeps track of the score.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and an operator
        num1 = generate_random_integer(1, 10)
        
        # Fix: num2 should also be an integer, so using 1 as the minimum and 5 as the maximum
        num2 = generate_random_integer(1, 5)
        
        operator = choose_operator()

        # Create the math problem and calculate the correct answer
        problem, correct_answer = create_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a numeric answer.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
