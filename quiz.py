# quiz.py

def ask_question(question, options, correct_option):
    """
    Asks a question and validates the user's answer.
    """
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter the number of your choice: "))
            if 1 <= answer <= len(options):
                return answer == correct_option
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# List of questions
questions = [
    {
        "question": "Why do you want to learn programming?",
        "options": [
            "To solve problems and automate tasks.",
            "To become a software developer.",
            "Because it sounds cool.",
            "I don't know yet."
        ],
        "correct_option": 1
    },
    {
        "question": "What do you think programming requires?",
        "options": [
            "Creativity and logic.",
            "Patience and persistence.",
            "Teamwork and collaboration.",
            "All of the above."
        ],
        "correct_option": 4
    },
    {
        "question": "How much time are you willing to dedicate weekly?",
        "options": [
            "1-2 hours.",
            "5-10 hours.",
            "10+ hours.",
            "None of the above."
        ],
        "correct_option": 3
    },
    {
        "question": "What’s your biggest motivation?",
        "options": [
            "Building useful tools.",
            "Making money.",
            "Learning something new.",
            "I’m not sure yet."
        ],
        "correct_option": 1
    },
]

# Ask the questions
score = 0
for q in questions:
    if ask_question(q["question"], q["options"], q["correct_option"]):
        print("Correct!")
        score += 1
    else:
        print("That's not correct.")

# Evaluate the result
print(f"\nYou scored {score} out of {len(questions)}.")
if score >= 3:
    print("Great! You seem motivated to start programming!")
else:
    print("Keep exploring and find your reasons to learn programming!")
