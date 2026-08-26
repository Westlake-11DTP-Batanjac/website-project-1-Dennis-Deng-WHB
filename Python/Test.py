# Performer: Karl Urban, born in Wellington, New Zealand

def Begin():
    Player = input(("Welcome to the quiz. What's your name? "))
    print(f"Alright {Player}, now you will answer the following eight questions about Karl Urban, a New Zealand actor. Wish You Luck.")
    print("------Loading...------")
    score = 0
    Question1(score)

def Question1(score):
    Question = ["Christchurch", "Wellington", "Auckland"]
    Answers = 1
    print("Question 1: In what city is Karl Urban born?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "wellington":
                score = score + 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question2(score)
            break
        else:
            print("An error occured, retry")

def Question2(score):
    Question = ["1970", "1971", "1972"]
    Answers = 1
    print("Question 2: What year is Karl Urban born?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "1972":
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question3(score)
            break
        else:
            print("An error occured, retry")

def Question3(score):
    Question = ["Ghost Ship", "Lord of the Rings", "Star Trek"]
    Answers = 1
    print("Question 3: What's Karl Urban's first Hollywood film name?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "ghost ship":
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question4(score)
            break
        else:
            print("An error occured, retry")

def Question4(score):
    Question = ["Thor: Ragnarok", "Iron Man 3", "Spiderman: Brand New Day"]
    Answers = 1
    print("Question 4: In what MARVEL movie did Karl Urban participate?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "thor: ragnarok":
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question5(score)
            break
        else:
            print("An error occured, retry")

def Question5(score):
    Question = ["Butcher", "Homelander", "A-Train"]
    Answers = 1
    print("Question 5: In The BOYS, who did Karl Urban act as?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "butcher":
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question6(score)
            break
        else:
            print("An error occured, retry")

def Question6(score):
    Question = ["Mortal Kombat I", "Mortal Kombat II", "Mortal Combat II"]
    Answers = 1
    print("Question 6: Which of the following movie is Karl in?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer in Question:
            if answer == "mortal kombat ii":
                score += 1
                print(f"Correct! Score: {score}")
            else:
                print(f"Wrong! Score: {score}")
            Question7(score)
            break
        else:
            print("An error occured, retry")

def Question7(score):
    print("Question 7: True or False: Karl Urban voiced the character, Bob, in Ark: The Animated Series")
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
        elif answer == "false":
            print(f"Wrong! Score: {score}")
        else:
            print("An error occured, retry")
        Question8(score)
        break

def Question8(score):
    print("Question 8: True or False: Karl Urban played as Eomer in The Lord of the Rings: Return of the King")
    while True:
        answer = input("Enter your answer (In correct uppercase & spacing): ").lower()
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
        elif answer == "false":
            print(f"Wrong! Score: {score}")
        else:
            print("An error occured, retry")
        End(score)
        break

def End(score):
    print("------Test Over------")
    if score >= 5:
        print(f"Final Mark: {score}, Test Passed")
    elif score <= 4:
        print(f"Final Mark: {score}, Test Failed")
    print("GoodBye")
    
    
Begin()