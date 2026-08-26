# Performer: Karl Urban, born in Wellington, New Zealand

# Starting the quiz function
def Begin():
    # Enter player name
    Player = input(("Welcome to the quiz. What's your name? "))
    print(f"Alright {Player}, now you will answer the following eight questions about Karl Urban, a New Zealand actor. Wish You Luck.")
    print("------Loading...------")
    score = 0
    # Start of question 1
    Question1(score)

def Question1(score):
    # Possible answers of Q1
    Question = ["Christchurch", "Wellington", "Auckland"]
    Answers = 1
    # Question of Q1
    print("Question 1: In what city is Karl Urban born?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    # Answer check
    while True:
        try:
            # Correct answer
            answer = int(input("Enter your answer (In number): "))
            if answer == 2:
                score = score + 1
                print(f"Correct! Score: {score}")
                Question2(score)
                break
            # If input isn't an option
            elif answer > 3:
                print(f"That's not an option, retry")
            # Wrong answer
            else:
                print(f"Wrong! Score: {score}")
                Question2(score)
                break
        # When the input type isn't int
        except:
            print("An error occured, retry")

# Q2 to Q6 are same as Q1
def Question2(score):
    Question = ["1970", "1971", "1972"]
    Answers = 1
    print("Question 2: What year is Karl Urban born?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 3:
                score += 1
                print(f"Correct! Score: {score}")
                Question3(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                Question3(score)
                break
        except:
            print("An error occured, retry")

def Question3(score):
    Question = ["Ghost Ship", "Lord of the Rings", "Star Trek"]
    Answers = 1
    print("Question 3: What's Karl Urban's first Hollywood film name?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 1:
                score += 1
                print(f"Correct! Score: {score}")
                Question4(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                Question4(score)
                break
        except:
            print("An error occured, retry")

def Question4(score):
    Question = ["Thor: Ragnarok", "Iron Man 3", "Spiderman: Brand New Day"]
    Answers = 1
    print("Question 4: In what MARVEL movie did Karl Urban participate?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 1:
                score += 1
                print(f"Correct! Score: {score}")
                Question5(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                Question5(score)
                break
        except:
            print("An error occured, retry")

def Question5(score):
    Question = ["A-Train", "Homelander", "Butcher"]
    Answers = 1
    print("Question 5: In The BOYS, who did Karl Urban act as?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 3:
                score += 1
                print(f"Correct! Score: {score}")
                Question6(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                Question6(score)
                break
        except:
            print("An error occured, retry")

def Question6(score):
    Question = ["Mortal Kombat I", "Mortal Kombat II", "Mortal Combat II"]
    Answers = 1
    print("Question 6: Which of the following movie is Karl in?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter your answer (In number): "))
            if answer == 2:
                score += 1
                print(f"Correct! Score: {score}")
                Question7(score)
                break
            elif answer > 3:
                print(f"That's not an option, retry")
            else:
                print(f"Wrong! Score: {score}")
                Question7(score)
                break
        except:
            print("An error occured, retry")

# True or False Questions
def Question7(score):
    print("Question 7: True or False: Karl Urban voiced the character, Bob, in Ark: The Animated Series")
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        # Correct inputs
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
            Question8(score)
            break
        elif answer == "false":
            print(f"Wrong! Score: {score}")
            Question8(score)
            break
        # Wrong inputs
        elif answer >= 0 or answer <= 0:
            print("An error occured, retry")
        else:
            print("That's not an option, retry")
        
# Similar to Q7
def Question8(score):
    print("Question 8: True or False: Karl Urban played as Eomer in The Lord of the Rings: Return of the King")
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
            End(score)
            break
        elif answer == "false":
            print(f"Wrong! Score: {score}")
            End(score)
            break
        elif answer >= 0 or answer <= 0:
            print("An error occured, retry")
        else:
            print("That's not an option, retry")

# Finishing Quiz
def End(score):
    print("------Test Over------")
    # Pass line
    if score >= 5:
        print(f"Final Mark: {score}, Test Passed")
    # Quiz failed
    elif score <= 4:
        print(f"Final Mark: {score}, Test Failed")
    print("GoodBye")
    
# Start the entire quiz
Begin()