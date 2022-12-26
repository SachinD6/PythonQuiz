# CONSTANTS
TOTAL_QUESTION = 5
SCORE = 0

QUESTIONS = {
    "In school, Albert Einstein failed most of the subjects, except for physics and math.": "y",
    "The first song ever sung in the space was Happy Birthday.": "y",
    " A male canary tends to have a better singing voice than a female canary.": "y",
    "Tea contains more caffeine than coffee and soda": "n",
    "Dogs have an appendix.": "n",
    "Bill Gates is the founder of Amazon.": "n",
    "Mice have more bones than humans.": "y",
    "The first product with a bar code was chewing gum": "y",
    "The Beatles is a famous rock band from Manchester, the United Kingdom": "n",
    "The star is the most common symbol used in all national flags around the world.": "y",
}

# IMPORTS
import random, time, sys


def welcome_and_greets():
    """
    Returns welcome message and greets user
    """
    print("Welcome to Quiz game")
    print(
        """
    
░██████╗░██╗░░░██╗██╗███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔═══██╗██║░░░██║██║╚════██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝
██║██╗██║██║░░░██║██║░░███╔═╝  ██║░░██╗░███████║██╔████╔██║█████╗░░
╚██████╔╝██║░░░██║██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
░╚═██╔═╝░╚██████╔╝██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝


█ █▄░█ █▀ ▀█▀ █▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
█ █░▀█ ▄█ ░█░ █▀▄ █▄█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█

    1. Qᴜɪᴢ ɢᴀᴍᴇ ʜᴀs 5 ᴏ̨ᴜᴇsᴛɪᴏɴs.
    2. Each questions is of 2 points.
    3. ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴄʜᴏᴏsᴇ ᴇɪᴛʜᴇʀ (y/n)
    4. PRESS E/e ᴛᴏ ᴇxɪᴛ
    """
    )


welcome_and_greets()

# Ascii art generated from => https://fsymbols.com/generators/carty/


randomQuestions = random.sample(
    QUESTIONS.items(), TOTAL_QUESTION
)  # Get 5 random questions

correctAnswerMessages = [
    "Congrats! You got it right ✅",
    "Congatulations, It is correct 🎉",
    "Thats right, great 😉",
]  # Add more if you want

incorrectAnswerMessages = ["Not correct ❌", "Oops, Wrong answer 😔", "Not right 😕"]

run = "y"

while run[0].lower() == "y":

    for question, answer in randomQuestions:
        print(f">> {question} (Y/N)")
        userAnswer = input("Enter answer: ")

        if userAnswer == "E" or userAnswer == "e":
            print("Exiting...")
            time.sleep(0.5)
            print(f"Your score is {SCORE} out of {TOTAL_QUESTION * 2}")
            sys.exit(0)  # exit the program if user enters E or e

        if answer == userAnswer.lower():
            print(
                random.choice(correctAnswerMessages) + "\n"
            )  # show random message from list
            SCORE += 2
        else:
            print(random.choice(incorrectAnswerMessages) + "\n")

    print(
        f"""    -------------------------------------------------------------------------
        Your score is {SCORE} out of {TOTAL_QUESTION * 2} and you got {int(SCORE / 2)} answers correct
        ----------------------------------------------------------------------------------"""
    )
    print("\n")

    run = input("Do you want to play again? (y/n): ")
    print("\n")

print("THANKS FOR PLAYING!!!")
