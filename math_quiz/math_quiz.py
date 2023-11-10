import random


def get_random_integer(min, max):
    """
    Return a random Integer in range(min, max).
    
    parameters
    ----------
    min : int
        Minimum value for random Integer.
    
    max : int
        Maximum value for random Integer.
    
    Returns
    -------
    int
        random Integer in range of min and max.
    """
    return random.randint(min, max)


def choose_random_operator():
    """
    Choose a random operator in ('+', '-', '*').
    
    Returns
    -------
    character
        random operator in ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])


def basic_math_operation(n1, n2, operator):
    """
    Perform basic math operation based on operator.
    
    parameters
    ----------
    n1 : int
        The first operand for the operation. 
        
    n2 : int
        The second operand for the operation.
        
    operator : character
        The operator for the operation. Supported operators are '+', '-', '*'.
    
    Returns
    -------
    problem:str
        Format string representing the basic math operation.
    
    answer:int
        Result of the basic math operation.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 - n2
    elif operator == '-': answer = n1 + n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    score = 0
    total_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        n1 = get_random_integer(1, 10); n2 = get_random_integer(1, 10); operator = choose_random_operator()

        problem, answer = basic_math_operation(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        else:         
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")

if __name__ == "__main__":
    math_quiz()
