# Performer: Karl Urban, born in Wellington, New Zealand

# Make a loading screen
import time

# Starting the quiz function
def Begin():
    # Enter player name
    Player = input(("Welcome to the quiz. What's your name? "))
    while True:
        start = input("Do you want to do a quiz?(y or n): ")
        if start == "y":
            print(f"Alright {Player}, now you will answer the following eight questions about Karl Urban. Wish You Luck.")
            time.sleep(2)
            print("\nLoading Questions")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".\n")
            time.sleep(1)
            score = 0
            # Start of question 1
            Question1(score)
            break
        elif start == "n":
            print("Alright then, GoodBye")
            break
        else:
            print("Not an option, just enter y or n WILL YOU!")

def Question1(score):
    # Possible answers of Q1
    Question = ["Christchurch", "Wellington", "Auckland"]
    Answer_Num = 1
    # Question of Q1
    print("Question 1: In what city is Karl Urban born?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    # Answer check
    while True:
        try:
            # Correct answer
            answer = int(input("Enter your answer (In number): "))
            if answer == 2:
                score = score + 1
                print(f"Correct! Score: {score}")
                # give player time to check scores
                time.sleep(1)
                print("\n")
                Question2(score)
                break
            # If input isn't an option
            elif answer > 3:
                print(f"That's not an option, retry")
            # Wrong answer
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question2(score)
                break
        # When the input type isn't int
        except:
            print("Should be a number, retry")

# Q2 to Q6 are same as Q1
def Question2(score):
    Question = ["1970", "1971", "1972"]
    Answer_Num = 1
    print("Question 2: What year is Karl Urban born?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 3:
                score += 1
                print(f"Correct! Score: {score}")
                time.sleep(1)
                print("\n")
                Question3(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question3(score)
                break
        except:
            print("Should be a number, retry")

def Question3(score):
    Question = ["Ghost Ship", "Lord of the Rings", "Star Trek"]
    Answer_Num = 1
    print("Question 3: What's Karl Urban's first Hollywood film name?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 1:
                score += 1
                print(f"Correct! Score: {score}")
                time.sleep(1)
                print("\n")
                Question4(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question4(score)
                break
        except:
            print("Should be a number, retry")

def Question4(score):
    Question = ["Thor: Ragnarok", "Iron Man 3", "Spiderman: Brand New Day"]
    Answer_Num = 1
    print("Question 4: In what MARVEL movie did Karl Urban participate?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 1:
                score += 1
                print(f"Correct! Score: {score}")
                time.sleep(1)
                print("\n")
                Question5(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question5(score)
                break
        except:
            print("Should be a number, retry")

def Question5(score):
    Question = ["A-Train", "Homelander", "Butcher"]
    Answer_Num = 1
    print("Question 5: In The BOYS, who did Karl Urban act as?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 3:
                score += 1
                print(f"Correct! Score: {score}")
                time.sleep(1)
                print("\n")
                Question6(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question6(score)
                break
        except:
            print("Should be a number, retry")

def Question6(score):
    Question = ["Mortal Kombat I", "Mortal Kombat II", "Mortal Combat II"]
    Answer_Num = 1
    print("Question 6: Which of the following movie is Karl in?")
    for i in Question:
        print(f"{Answer_Num}. {i}")
        Answer_Num += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 2:
                score += 1
                print(f"Correct! Score: {score}")
                time.sleep(1)
                print("\n")
                Question7(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                time.sleep(1)
                print("\n")
                Question7(score)
                break
        except:
            print("Should be a number, retry")

# True or False Questions
def Question7(score):
    print("Question 7: True or False: Karl Urban voiced the character, Bob, in Ark: The Animated Series")
    while True:
        answer = input("Enter your answer (In correct spacing): ").lower()
        # Correct inputs
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
            time.sleep(1)
            print("\n")
            Question8(score)
            break
        elif answer == "false":
            print(f"Wrong! Score: {score}")
            time.sleep(1)
            print("\n")
            Question8(score)
            break
        # Wrong inputs
        else:
            print("That's not an option, retry")
        
# Similar to Q7
def Question8(score):
    print("Question 8: True or False: Karl Urban played as Eomer in The Lord of the Rings: Return of the King")
    while True:
        answer = input("Enter your answer (In correct spacing): ").lower()
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
            time.sleep(1)
            print("\n")
            End(score)
            break
        elif answer == "false":
            print(f"Wrong! Score: {score}")
            time.sleep(1)
            print("\n")
            End(score)
            break
        else:
            print("That's not an option, retry")

# Finishing Quiz
def End(score):
    print("------Test Over------")
    print("Calculating Marks...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    # Pass line
    if score >= 5:
        print(f"\nFinal Mark: {score}, Test Passed\n")
    # Quiz failed
    elif score <= 4:
        print(f"\nFinal Mark: {score}, Test Failed\n")
    print("GOODBYE")
    
# Start the entire quiz
Begin()