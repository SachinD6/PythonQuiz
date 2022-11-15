import time
import random


def show_instructions(instructions: list):
    for instruction in instructions:
        time.sleep(2)
        print(instruction)


show_instructions(
    [
        " \n -------------------------\n Welcome to quiz !! \n -------------------------",
        "You will be asked 5 questions.",
        "You will be given 2 choices either True/False",
        "You will be given 20 points for each correct answer.",
        "GOOD LUCK!",
        "\n",
    ]
)

questions = {
    ">> Delhi is Capital of India": "true",
    ">> Steve Jobs is the founder of Microsoft": "false",
    ">> Jack Dorsey is the founder of Twitter": "true",
    ">> Rust is a programming language": "true",
    ">> Go is a statically typed, compiled programming language designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson.": "true",
}

# randomQuestions = random.sample(list(questions), 5)


def start_quiz():
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question} (True/False): ").lower()
        if user_answer == str(answer):
            print("Correct!")
            score += 20
        else:
            print("Incorrect!")
    print(
        f" \n -------------------------\n Your score is {score} \n -------------------------"
    )


if __name__ == "__main__":
    start_quiz()

""""
Improvements:
1. Add more questions
2. Store gretting messages in any container like list and show them randomly when user answer the question.
3. Add numbering to questions automatically. Example: Q1. Delhi is Capital of India
4. Show random questions from questions dictionary.


"""
