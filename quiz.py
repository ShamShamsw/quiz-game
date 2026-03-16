"""
Quiz Game — Starter Code
=========================

YOUR TASK: Fill in every function marked with TODO.
Read the README.md in this folder FIRST for the full instructions.

TIME ESTIMATE: 45–75 minutes

IMPORTANT — If You Get Stuck:
    1. Re-read the README section for the step you're on.
    2. Try writing what you want the code to do in plain English first.
    3. Test one function at a time — don't build everything then hope it works.
    4. Use an AI assistant (like Copilot Chat) to ASK QUESTIONS about
       concepts you don't understand — for example:
         "How do I loop through a list of dictionaries in Python?"
         "What's the difference between a list and a dictionary?"
       DO NOT ask AI to write the solution for you. The learning happens
       when YOUR brain figures out how to connect the pieces. AI is a
       tutor, not a shortcut. If AI writes your code, you skip the
       struggle that actually builds understanding.
    5. Check the Python docs: https://docs.python.org/3/

PLANNING — Answer these BEFORE writing any code (fill in below):

    Data structure for a single question:
        - I will use a dictionary with keys: "question", "choices", "answer", "explanation"
        - Why a dict? Because each question has named fields — accessing
          question["answer"] is clearer than question[2]
        - Alternative considered: a tuple — rejected because index-based
          access (question[0], question[2]) is harder to read

    Data structure for ALL questions:
        - A list of dictionaries — easy to loop through with a for loop
        - The list order IS the quiz order

    Functions I'll create:
        - display_question(question, number, total) — show one question nicely
        - get_answer() — get a valid A/B/C/D from the user
        - check_answer(user_answer, question) — compare and give feedback
        - show_results(score, total) — final summary with a message
        - main() — run the quiz loop

    Score tracking:
        - A simple integer counter, incremented for each correct answer
        - Message thresholds: 100% perfect, 80%+ great, 60%+ good, below 60% keep practicing

    Edge cases:
        - User types lowercase "a" instead of "A"
        - User types a number or full word
        - User just presses Enter
"""

# ============================================================
# STEP 1: QUIZ DATA
# ============================================================
# Each question is a dictionary with four keys:
#   "question"    — the question text (string)
#   "choices"     — the four options (dict mapping A/B/C/D to text)
#   "answer"      — the correct letter, uppercase (string)
#   "explanation" — why the answer is correct (shown on wrong answers)
#
# I chose a list of dictionaries because:
#   - Each question has multiple named fields → dict is clearer than tuple
#   - A list preserves order and is easy to iterate with enumerate()
#   - This structure maps naturally to JSON if we ever load from a file
# ============================================================

QUESTIONS = [
    {
        "question": "What keyword creates a function in Python?",
        "choices": {"A": "method", "B": "def", "C": "function", "D": "create"},
        "answer": "B",
        "explanation": "The 'def' keyword (short for 'define') declares a function in Python.",
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "choices": {"A": "2", "B": "[1, 2, 3]", "C": "3", "D": "Error"},
        "answer": "C",
        "explanation": "len() returns the number of items in a list. [1, 2, 3] has 3 items.",
    },
    # TODO: Add at least 3 more questions of your own!
    # Think about topics you've been learning recently.
    # Each question needs all four keys: question, choices, answer, explanation.
]


# ============================================================
# STEP 2: DISPLAY A QUESTION
# ============================================================
# Separating display from logic means if you wanted to change
# how questions look (colors, formatting), you only change this
# function — the quiz logic stays untouched.
# ============================================================


def display_question(question, number, total):
    """
    Display a single quiz question with its answer choices.

    Parameters:
        question (dict): A question dictionary with keys "question" and "choices".
        number (int): The current question number (1-based, for display).
        total (int): The total number of questions in the quiz.

    Returns:
        None — this function only prints to the console.

    Example output:
        Question 2 of 5:
        What does len([1, 2, 3]) return?

          A) 2
          B) [1, 2, 3]
          C) 3
          D) Error
    """
    # TODO: Implement this function
    # Hints:
    #   - Print the question number and total first
    #   - Print the question text
    #   - Loop through the choices dict and print each one formatted as "  A) text"
    #   - You can loop through a dict with: for letter, text in question["choices"].items()
    pass


# ============================================================
# STEP 3: GET AND VALIDATE THE USER'S ANSWER
# ============================================================
# Keep asking until the user types A, B, C, or D.
# Convert to uppercase so "a" and "A" both work.
# ============================================================


def get_answer():
    """
    Prompt the user for their answer and validate it.

    Returns:
        str: The user's answer as an uppercase letter (A, B, C, or D).

    Why validate in a loop instead of accepting anything:
        If we accepted "banana" as an answer, check_answer would always
        say it's wrong — but the user didn't mean to answer, they made
        a typo. Validating prevents false negatives and teaches the user
        what inputs are expected.
    """
    # TODO: Implement this function
    # Hints:
    #   - Use a while True loop
    #   - Use input("Your answer: ").strip().upper() to clean the input
    #   - Check if the answer is in ["A", "B", "C", "D"]
    #   - If valid, return it. If not, print a helpful message and loop again.
    pass


# ============================================================
# STEP 4: CHECK THE ANSWER
# ============================================================
# Compare the user's choice to the correct answer.
# Show immediate feedback — right or wrong.
# ============================================================


def check_answer(user_answer, question):
    """
    Check if the user's answer is correct and display feedback.

    Parameters:
        user_answer (str): The user's chosen letter (e.g., "B").
        question (dict): The full question dictionary (has "answer" and "explanation").

    Returns:
        bool: True if correct, False if incorrect.

    Design note:
        This function returns a boolean AND prints feedback. In a bigger app,
        you'd separate these (return the result, let the caller print).
        For this small project, combining them keeps the main loop simple.
    """
    # TODO: Implement this function
    # Hints:
    #   - Compare user_answer to question["answer"]
    #   - If correct: print a success message, return True
    #   - If wrong: print the correct answer AND the explanation, return False
    pass


# ============================================================
# STEP 5: SHOW FINAL RESULTS
# ============================================================
# Score messages (document your thresholds!):
#   100%      → "Perfect score! ..."
#   80–99%    → "Great job! ..."
#   60–79%    → "Good effort! ..."
#   Below 60% → "Keep practicing! ..."
#
# Using if/elif because the conditions are ranges, not exact values.
# A dictionary wouldn't work well for ranges.
# ============================================================


def show_results(score, total):
    """
    Display the final quiz score with a message based on performance.

    Parameters:
        score (int): Number of correct answers.
        total (int): Total number of questions.

    Returns:
        None — prints to console.
    """
    # TODO: Implement this function
    # Hints:
    #   - Calculate the percentage: score / total * 100
    #   - Use if/elif to pick the right message
    #   - Print the score, percentage, and message
    pass


# ============================================================
# STEP 6: MAIN QUIZ LOOP
# ============================================================
# This function ties everything together.
# ============================================================


def main():
    """
    Run the quiz game from start to finish.

    Flow:
        1. Print a welcome message with the question count
        2. Loop through each question using enumerate()
        3. For each: display → get answer → check → update score
        4. After all questions: show results
    """
    # Initialize the score counter
    # (A simple int is enough — we only need to count correct answers)
    score = 0
    total = len(QUESTIONS)

    # TODO: Implement the rest of this function
    # Hints:
    #   - Print a welcome banner
    #   - Use: for i, question in enumerate(QUESTIONS):
    #     This gives you both the index (i) and the question dict
    #   - Call display_question with number=i+1 (because enumerate starts at 0)
    #   - Call get_answer() to get the user's choice
    #   - Call check_answer() and if it returns True, add 1 to score
    #   - After the loop, call show_results(score, total)
    pass


# Main guard — only runs the quiz when you execute this file directly
if __name__ == "__main__":
    main()


# ============================================================
# WHAT I LEARNED (fill this in AFTER you finish)
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
