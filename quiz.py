import time


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
    ">> Q1. Delhi is Capital of India": "true",
    ">> Q2. Steve Jobs is the founder of Microsoft": "false",
    ">> Q3. Jack Dorsey is the founder of Twitter": "true",
    ">> Q4. Rust is a programming language": "true",
    ">> Q5. Go is a statically typed, compiled programming language designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson.": "true",
}


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
