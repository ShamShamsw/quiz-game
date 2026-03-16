# Beginner Project 02: Quiz Game

**Time:** 45–75 minutes  
**Difficulty:** Beginner  
**Focus:** Planning data structures, organizing code into functions, writing self-documenting comments, lists and dictionaries

---

## Why This Project?

A quiz game is one of the best beginner projects because it forces you to think about **how to store and organize data** before you write logic. In interviews, choosing the right data structure is half the battle. This project practices that decision-making process.

---

## The Importance of Comments

In this project, you will write **three types of comments**:

### 1. Planning comments (before you code)
Write your data structure choices and reasoning at the top of the file. Example:
```python
# I chose a list of dictionaries to store questions because:
# - Each question has multiple pieces of data (text, choices, answer)
# - A list lets me easily loop through all questions
# - A dictionary lets me access each piece by name instead of index
# Alternative considered: a list of tuples — rejected because accessing
# fields by index (question[0], question[2]) is harder to read than
# question["text"], question["answer"]
```

### 2. Docstrings (what a function does)
Every function gets a docstring. No exceptions.

### 3. Decision comments (why you did something a specific way)
Whenever you choose between two approaches, leave a comment explaining your choice. This is exactly what interviewers want to hear when you think out loud.

---

## Requirements

Build a command-line quiz game that:

1. Presents multiple-choice questions one at a time
2. Accepts the user's answer (A, B, C, or D)
3. Tells the user immediately if they're right or wrong
4. Shows the correct answer when they're wrong
5. Tracks the score throughout the quiz
6. Shows a final summary with their score and a message based on how they did

### Example session:

```
=== Python Quiz Game ===
5 questions | Type A, B, C, or D to answer

Question 1 of 5:
What keyword creates a function in Python?

  A) method
  B) def
  C) function
  D) create

Your answer: B
✅ Correct!

Question 2 of 5:
What does `len([1, 2, 3])` return?

  A) 2
  B) [1, 2, 3]
  C) 3
  D) Error

Your answer: A
❌ Incorrect. The correct answer is C) 3

... (3 more questions) ...

=== Quiz Complete! ===
Your score: 4 / 5 (80%)
Great job! You really know your Python basics!
```

---

## STOP — Plan Before You Code

Before writing any Python, answer these questions in a comment block at the top of your file. **Spend at least 10–15 minutes on this step.**

### Planning Questions

1. **How will you store the quiz questions?**
   - What data does each question need? (question text, choices, correct answer, maybe an explanation)
   - What data structure will hold a single question? (dictionary, named tuple, dataclass, class?)
   - What data structure will hold ALL the questions? (list, dictionary keyed by number?)
   - **Write out your decision and WHY you chose it over the alternatives**

2. **What functions do you need?**
   For each function, plan:
   - Name (descriptive verb-noun: `display_question`, `check_answer`, `show_results`)
   - Parameters (what information does it need?)
   - Return value (what information does it send back?)
   - Side effects (does it print anything? modify any data?)

   Suggested functions to consider:
   - A function to display one question and its choices
   - A function to get and validate the user's answer
   - A function to check if the answer is correct
   - A function to show the final results
   - A main function that runs the quiz loop

3. **How will you calculate and display the final score?**
   - What variable(s) do you need to track?
   - What are the message thresholds? (100% = "Perfect!", 80%+ = "Great!", etc.)

4. **What could go wrong?**
   - User types lowercase "a" instead of "A"
   - User types "1" instead of "A"
   - User types a full word like "def" instead of "B"
   - User presses Enter with nothing

5. **What order will you build and test?**
   Number your build steps. What can you test first, even before the full program works?

---

## Step-by-Step Instructions

### Step 1: Create your file and write the plan (10–15 minutes)

Create `quiz.py`. Write your complete planning block as a multi-line comment at the top. This should be **at least 20 lines**. Include your data structure decision and the reasoning behind it.

### Step 2: Define your question data (5 minutes)

Create at least 5 quiz questions. Store them using the data structure you planned.

```python
# Each question is stored as a dictionary with four keys:
# - "question": the question text (string)
# - "choices": the four answer options (dict mapping A/B/C/D to text)
# - "answer": the correct letter (string, uppercase)
# - "explanation": why the answer is correct (string, shown on wrong answers)
#
# I chose a dictionary over a tuple because:
# [your reasoning here — write this yourself]

questions = [
    {
        "question": "What keyword creates a function in Python?",
        "choices": {
            "A": "method",
            "B": "def",
            "C": "function",
            "D": "create"
        },
        "answer": "B",
        "explanation": "The 'def' keyword (short for 'define') declares a function in Python."
    },
    # Add 4 more questions...
]
```

**Important:** Add a comment above the data explaining the structure. Someone reading your code for the first time (like an interviewer) should understand the data layout without having to read every entry.

### Step 3: Write `display_question` (5 minutes)

This function takes a question dictionary and the question number, then prints it formatted nicely.

```python
def display_question(question, number, total):
    """
    Display a single quiz question with its answer choices.

    Parameters:
        question (dict): A question dictionary with keys "question" and "choices".
        number (int): The current question number (1-based, for display).
        total (int): The total number of questions in the quiz.

    Returns:
        None — this function only prints to the console.

    Why this is a separate function:
        Separating display logic from game logic makes the code easier to
        modify later (e.g., if we wanted to add a GUI, we'd only change
        this function, not the quiz logic).
    """
    # TODO: implement this
    pass
```

Notice the docstring explains not just WHAT but WHY it's a separate function. Do this for every function.

### Step 4: Write `get_answer` (5 minutes)

This function prompts the user and validates their input. It keeps asking until the user gives a valid response (A, B, C, or D).

Add a comment explaining:
- Why you convert to uppercase (or lowercase)  
- Why you validate in a loop instead of just accepting whatever they type

### Step 5: Write `check_answer` (5 minutes)

This function compares the user's answer to the correct answer and prints feedback.

```python
def check_answer(user_answer, question):
    """
    Check if the user's answer is correct and display feedback.

    Parameters:
        user_answer (str): The user's chosen letter (e.g., "B").
        question (dict): The full question dictionary.

    Returns:
        bool: True if the answer is correct, False otherwise.

    Design note:
        This function returns a boolean AND prints feedback. In a more
        complex app, you'd want to separate these (return the result, let
        the caller decide what to print). For this small project, combining
        them keeps the main loop simple.
    """
    # TODO: implement this
    pass
```

### Step 6: Write `show_results` (5 minutes)

This function takes the score and total, calculates the percentage, and shows a message.

Plan your message thresholds in a comment:
```python
# Score messages:
# 100%      → "Perfect score! ..."
# 80-99%    → "Great job! ..."
# 60-79%    → "Good effort! ..."
# Below 60% → "Keep practicing! ..."
#
# I'm using if/elif instead of a dictionary here because the conditions
# are ranges, not exact matches. A dictionary would work if I mapped
# each possible score to a message, but that's less maintainable.
```

### Step 7: Write the main function and quiz loop (5 minutes)

Tie everything together:

```python
def main():
    """
    Run the quiz game from start to finish.

    Flow:
        1. Print welcome message
        2. Loop through each question
        3. For each: display, get answer, check, update score
        4. After all questions: show results
    """
    # Step 1: Initialize the score counter
    # (Why a simple int and not something fancier? Because we only
    # need to count correct answers — no need for a complex data structure)
    score = 0

    # TODO: implement the rest
```

### Step 8: Test thoroughly (5 minutes)

Run through the quiz testing:
- All correct answers
- All wrong answers  
- Mixed correct/wrong
- Invalid inputs (lowercase, numbers, empty)
- Edge case: what if there's only 1 question?

---

## Comment Checklist

Before you consider this done:

- [ ] Planning block at the top (20+ lines) with data structure reasoning
- [ ] Every function has a complete docstring (description, parameters, returns)
- [ ] The data structure choice has a comment explaining WHY
- [ ] At least 2 functions have a "design note" explaining a design decision
- [ ] Input validation has comments explaining what you're protecting against
- [ ] Score thresholds are documented in a comment before the if/elif chain
- [ ] The `if __name__ == "__main__"` guard is present with a comment

---

## Reflect on What You Learned

After finishing, write 2–3 sentences for EACH audience below. Translating technical work into different registers is a core communication skill.

### To a friend (casual, no jargon)

> _"I built a thing that..."_
>
> Example: "I made a quiz game that asks you questions about Python and tells you your score at the end. I had to figure out how to store the questions and answers together so the program could check if you were right."

### To an employer (focus on skills and process)

> _"In this project I practiced..."_
>
> Example: "I practiced choosing appropriate data structures — I used a list of dictionaries to pair questions with answers and metadata. I wrote complete docstrings for every function and planned the data model before writing any logic."

### To a professor (technical, precise)

> _"This project demonstrates..."_
>
> Example: "This project demonstrates the use of list and dictionary data structures for structured data, function decomposition with documented interfaces, iteration with index tracking, and conditional scoring logic. I evaluated trade-offs between lists of dicts vs. parallel lists and documented the reasoning."

**Write yours in a comment block at the bottom of your Python file:**
```python
# ============================================================
# WHAT I LEARNED
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
```

---

## Stretch Goals

1. Shuffle the question order each time using `random.shuffle()` (comment on why random improves replayability)
2. Load questions from a JSON file instead of hardcoding them (comment on why external data is better)
3. Add a timer that shows how long the user took per question and overall
4. Add a "review" mode at the end that shows all questions the user got wrong
