import time
import random


def show_instructions(instructions: list):
    for instruction in instructions:
        time.sleep(2)
        print(instruction)


def timer():
    """
    Show time left for quiz => Default: 60sec
    """
    time_in_secs = 10
    while time_in_secs != 0:
        # mins, secs = divmod(time_in_secs, 60)
        # timer = "{:02d}:{:02d}".format(mins, secs)
        timer = time_in_secs
        print(f"Time left: {timer}", end="\r")
        time_in_secs -= 1
        time.sleep(1)
    print("Time is up!")


timer()

# show_instructions(
#     [
#         " \n -------------------------\n Welcome to quiz !! \n -------------------------",
#         "You will be asked 5 questions.",
#         "You will be given 2 choices either True/False",
#         "You will be given 20 points for each correct answer.",
#         "GOOD LUCK!",
#         "\n",
#     ]
# )

questions = {
    ">> Delhi is Capital of India": "true",
    ">> Steve Jobs is the founder of Microsoft": "false",
    ">> Jack Dorsey is the founder of Twitter": "true",
    ">> Rust is a programming language": "true",
    ">> Go is a statically typed, compiled programming language designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson.": "true",
    ">> JavaScript is most used programming language for web": "true",
    ">> Python is most used programming language for AI and Machine Learnign": "true",
}


def start_quiz():
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question} (True/False): ").lower()
        #
        if user_answer == str(answer) or str(
            answer[0]
        ):  # show correct even if user enter first letter of answer (t/f)
            print("Correct!")
            score += 20
        else:
            print("Incorrect!")
    print(
        f" \n -------------------------\n Your score is {score} \n -------------------------"
    )


if __name__ == "__main__":
    start_quiz()


# TODO: Make use of threading to run timer function in background with start_quiz()
