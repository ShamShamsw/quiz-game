"""
quiz.py — Command-line Python Quiz Game
========================================

PLANNING BLOCK
==============

1. HOW WILL I STORE THE QUIZ QUESTIONS?
----------------------------------------
Each question needs four pieces of data:
  - The question text (a string)
  - The four answer choices (A, B, C, D mapped to text)
  - The correct answer letter (a single uppercase string)
  - An explanation shown when the user answers incorrectly

Data structure for a SINGLE question: a dictionary.
  - A dictionary lets me access each piece by a readable key
    (question["text"], question["answer"]) rather than by a fragile
    numeric index (question[0], question[2]).
  - Alternative considered: a named tuple — rejected because dictionaries
    are easier to read and modify without needing a class definition.
  - Alternative considered: a dataclass — overkill for a small project
    with no need for methods or type enforcement at this stage.

Data structure for ALL questions: a list of dictionaries.
  - A list lets me loop through every question in order with a for-loop
    or by index (for the "Question X of Y" display).
  - Alternative considered: a dictionary keyed by question number — this
    adds no benefit over a list and complicates iteration.

2. WHAT FUNCTIONS DO I NEED?
------------------------------
  display_question(question, number, total)
    - Prints the formatted question and its A/B/C/D choices.
    - Parameters: question dict, current question number, total count.
    - Returns: None (side-effect only).

  get_answer()
    - Prompts the user and validates their input in a loop.
    - Returns: a validated uppercase letter (str) — one of A, B, C, D.

  check_answer(user_answer, question)
    - Compares the user's answer to the correct answer and prints feedback.
    - Returns: bool (True = correct, False = incorrect).

  show_results(score, total)
    - Calculates percentage and displays a final summary with a message.
    - Returns: None (side-effect only).

  main()
    - Orchestrates the full quiz: welcome, loop, results.

3. SCORE TRACKING
------------------
  A single integer 'score' incremented by 1 for each correct answer.
  Percentage = (score / total) * 100 rounded to the nearest integer.
  Thresholds:
    100%      → "Perfect score! You aced it!"
    80–99%    → "Great job! You really know your Python basics!"
    60–79%    → "Good effort! A little more practice and you'll have it."
    Below 60% → "Keep practicing! Review the topics you missed."

4. WHAT COULD GO WRONG?
-------------------------
  - User types lowercase "b" → convert to uppercase before comparing.
  - User types "1" or "yes" → reject and re-prompt in a loop.
  - User presses Enter with nothing → strip() returns empty string; reject.

5. BUILD ORDER
---------------
  1. Define the questions list.
  2. Implement display_question and test it alone.
  3. Implement get_answer and test with manual input.
  4. Implement check_answer and test correct/incorrect paths.
  5. Implement show_results and verify each threshold branch.
  6. Wire everything in main() and run a full end-to-end test.
"""

# ============================================================
# QUESTION DATA
# ============================================================
# Each entry is a dictionary with four keys:
#   "question"    : the question text displayed to the user
#   "choices"     : dict mapping letter → choice text (A, B, C, D)
#   "answer"      : the correct letter (uppercase string)
#   "explanation" : shown when the user answers incorrectly so
#                   they can learn from the mistake
#
# I chose a list of dicts over parallel lists (one for questions,
# one for answers, etc.) because keeping all data for one question
# together makes the code easier to read and avoids index-sync bugs.

questions = [
    {
        "question": "What keyword creates a function in Python?",
        "choices": {
            "A": "method",
            "B": "def",
            "C": "function",
            "D": "create",
        },
        "answer": "B",
        "explanation": "'def' (short for 'define') is the keyword used to declare "
                       "a function in Python.",
    },
    {
        "question": "What does `len([1, 2, 3])` return?",
        "choices": {
            "A": "2",
            "B": "[1, 2, 3]",
            "C": "3",
            "D": "Error",
        },
        "answer": "C",
        "explanation": "len() returns the number of items in a sequence. "
                       "The list [1, 2, 3] has 3 items.",
    },
    {
        "question": "Which data type is used to store True or False values?",
        "choices": {
            "A": "int",
            "B": "str",
            "C": "float",
            "D": "bool",
        },
        "answer": "D",
        "explanation": "'bool' is the Boolean data type in Python, with only "
                       "two possible values: True and False.",
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "choices": {
            "A": "//",
            "B": "/*",
            "C": "#",
            "D": "--",
        },
        "answer": "C",
        "explanation": "Python uses '#' to begin a single-line comment. "
                       "Everything after '#' on that line is ignored by the interpreter.",
    },
    {
        "question": "Which built-in function prints output to the console?",
        "choices": {
            "A": "echo()",
            "B": "console()",
            "C": "write()",
            "D": "print()",
        },
        "answer": "D",
        "explanation": "print() is Python's built-in function for displaying "
                       "output to the standard output (usually the terminal).",
    },
]


# ============================================================
# FUNCTIONS
# ============================================================


def display_question(question, number, total):
    """
    Display a single quiz question with its answer choices.

    Parameters:
        question (dict): A question dictionary with keys 'question' and 'choices'.
        number (int): The current question number (1-based, for display).
        total (int): The total number of questions in the quiz.

    Returns:
        None — this function only prints to the console.

    Design note:
        Separating display logic from game logic keeps the code easier to
        modify later. If we wanted to add a GUI, we would only change this
        function and not touch the quiz logic at all.
    """
    print(f"\nQuestion {number} of {total}:")
    print(question["question"])
    print()
    # Print each choice on its own line with a two-space indent for readability.
    for letter, text in question["choices"].items():
        print(f"  {letter}) {text}")
    print()


def get_answer():
    """
    Prompt the user to enter an answer and validate their input.

    The function keeps looping until the user enters a valid choice.
    Valid choices are A, B, C, or D (case-insensitive).

    Returns:
        str: A validated uppercase letter — one of 'A', 'B', 'C', or 'D'.

    Design note:
        Input is converted to uppercase so the user can type 'a' or 'A'
        interchangeably. Validation is done in a while-loop rather than a
        single check because we want to keep asking until we get valid input
        — accepting invalid input silently would lead to silent wrong answers.
        We also strip() to guard against accidental whitespace or an empty
        Enter press.
    """
    valid_choices = {"A", "B", "C", "D"}
    while True:
        # strip() removes leading/trailing whitespace including newlines;
        # upper() normalises lowercase input so 'a' == 'A'.
        raw = input("Your answer: ").strip().upper()
        if raw in valid_choices:
            return raw
        # Tell the user exactly what went wrong so they are not confused.
        print("  Please enter A, B, C, or D.")


def check_answer(user_answer, question):
    """
    Check if the user's answer is correct and display feedback.

    Parameters:
        user_answer (str): The user's chosen letter (e.g., 'B').
        question (dict): The full question dictionary (must contain 'answer'
                         and 'explanation' keys).

    Returns:
        bool: True if the answer is correct, False otherwise.

    Design note:
        This function both prints feedback AND returns a boolean. In a larger
        application you would typically separate these concerns (return only
        the result; let the caller decide what to display). For this small
        project, combining them keeps the main loop simple and readable.
    """
    correct_letter = question["answer"]
    correct_text = question["choices"][correct_letter]

    if user_answer == correct_letter:
        print("✅ Correct!")
        return True
    else:
        print(
            f"❌ Incorrect. The correct answer is {correct_letter}) {correct_text}"
        )
        # Show the explanation so the user learns, not just loses a point.
        print(f"   💡 {question['explanation']}")
        return False


def show_results(score, total):
    """
    Display the final quiz results including score, percentage, and a message.

    Parameters:
        score (int): The number of questions answered correctly.
        total (int): The total number of questions in the quiz.

    Returns:
        None — this function only prints to the console.

    Design note:
        The percentage is calculated here rather than passed in so the caller
        does not need to know about the display logic (single responsibility).
        Guard against division-by-zero: if total is 0 we show 0%.
    """
    # Score messages:
    # 100%      → "Perfect score! ..."
    # 80–99%    → "Great job! ..."
    # 60–79%    → "Good effort! ..."
    # Below 60% → "Keep practicing! ..."
    #
    # I'm using if/elif here because the conditions are numeric ranges,
    # not exact matches. A dictionary of exact scores would work for a
    # 5-question quiz but would not scale to quizzes of arbitrary length.
    percentage = int((score / total) * 100) if total > 0 else 0

    print("\n=== Quiz Complete! ===")
    print(f"Your score: {score} / {total} ({percentage}%)")

    if percentage == 100:
        print("Perfect score! You aced it! 🏆")
    elif percentage >= 80:
        print("Great job! You really know your Python basics! 🎉")
    elif percentage >= 60:
        print("Good effort! A little more practice and you'll have it. 👍")
    else:
        print("Keep practicing! Review the topics you missed. 📚")


def main():
    """
    Run the quiz game from start to finish.

    Flow:
        1. Print a welcome banner with the question count.
        2. Loop through each question in order.
        3. For each question: display it, get a validated answer,
           check correctness, and update the score.
        4. After all questions: display the final results.

    Returns:
        None
    """
    total = len(questions)

    # Welcome banner — give the user key info before the first question.
    print("=== Python Quiz Game ===")
    print(f"{total} questions | Type A, B, C, or D to answer")

    # Step 1: Initialize the score counter.
    # A simple int is all we need — we only track the count of correct answers.
    score = 0

    # Step 2: Loop through questions using enumerate so we have a 1-based index
    # for the "Question X of Y" display without a separate counter variable.
    for index, question in enumerate(questions, start=1):
        display_question(question, index, total)
        user_answer = get_answer()
        # check_answer returns True/False; adding True to an int adds 1.
        if check_answer(user_answer, question):
            score += 1

    # Step 3: Show the final tally once all questions are done.
    show_results(score, total)


# ============================================================
# ENTRY POINT
# ============================================================
# The 'if __name__ == "__main__"' guard ensures that main() is only
# called when this file is run directly (e.g., `python quiz.py`).
# If another module imports this file, main() will NOT be called
# automatically — this prevents unexpected side-effects during imports
# or during automated testing.
if __name__ == "__main__":
    main()


# ============================================================
# WHAT I LEARNED
# ============================================================
# Friend:
#   I built a command-line quiz game that asks Python questions one at a
#   time and tells you right away if you got them right. At the end it
#   shows your score and a message based on how well you did. The
#   trickiest part was making sure it kept asking when you typed something
#   wrong instead of just crashing.
#
# Employer:
#   In this project I practiced choosing appropriate data structures —
#   I used a list of dictionaries to pair each question with its choices,
#   correct answer, and an explanation. I wrote complete docstrings and
#   design-note comments for every function, planned the data model before
#   writing any logic, and implemented input validation that gracefully
#   handles invalid or empty input without crashing.
#
# Professor:
#   This project demonstrates the use of list and dictionary data
#   structures for structured, heterogeneous data, function decomposition
#   with documented interfaces (parameters, return values, side-effects),
#   iteration with index tracking via enumerate(), defensive input
#   validation in a while-loop, and conditional scoring logic using
#   if/elif chains. I evaluated trade-offs between lists of dicts,
#   parallel lists, and named tuples, and documented the reasoning for
#   choosing lists of dicts.
# ============================================================
