# Performer: Karl Urban, born in Wellington, New Zealand

def Begin():
    Player = input(("Welcome to the quiz. What's your name? "))
    print(f"Alright {Player}, now you will answer the following eight questions about Karl Urban, a New Zealand actor. Wish You Luck.")
    print("------Loading...------")
    Quiz()

def Question1(score):
    Answer_set_1 = ["Christchurch", "Wellington", "Auckland"]
    Q_Num = 1
    Answers = 1
    print(f"Question {Q_Num}: In what city is Karl Urban born?")
    for i in Answer_set_1:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question2(score):
    Question = ["1970", "1971", "1972"]
    Q_Num = 2
    Answers = 1
    print(f"Question {Q_Num}: What year is Karl Urban born?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question3(score):
    Question = ["Ghost Ship", "Lord of the Rings", "Star Trek"]
    Q_Num = 3
    Answers = 1
    print(f"Question {Q_Num}: What's Karl Urban's first Hollywood film name?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question4(score):
    Question = ["Thor: Ragnarok", "Iron Man 3", "Spiderman: Brand New Day"]
    Q_Num = 4
    Answers = 1
    print(f"Question {Q_Num}: In what MARVEL movie did Karl Urban participate?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question5(score):
    Question = ["Butcher", "Homelander", "A-Train"]
    Q_Num = 5
    Answers = 1
    print(f"Question {Q_Num}: In The BOYS, who did Karl Urban act as?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question6(score):
    Question = ["Mortal Kombat I", "Mortal Kombat II", "Mortal Combat II"]
    Q_Num = 6
    Answers = 1
    print(f"Question {Q_Num}: Which of the following movie is Karl in?")
    for i in Question:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question7(score):
    Q_Num = 7
    print(f"Question {Q_Num}: True or False: Karl Urban voiced the character, Bob, in Ark: The Animated Series")
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Question8(score):
    Q_Num = 8
    print(f"Question {Q_Num}: True or False: Karl Urban played as Eomer in The Lord of the Rings: Return of the King")
    while True:
        try:
            answer = input("Enter your answer: ").lower().strip()
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

def Check(Q_Num, answer, score):
    if Q_Num == 1:
        if answer == "wellington":
            score = score + 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 2:
        if answer == "1972":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 3:
        if answer == "ghostship":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 4:
        if answer == "thor:ragnarok":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 5:
        if answer == "butcher":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 6:
        if answer == "mortalkombatii":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 7:
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    elif Q_Num == 8:
        if answer == "true":
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")

def End(score):
    print("------Test Over------")
    if score >= 5:
        print(f"Final Mark: {score}, Test Passed")
    elif score <= 4:
        print(f"Final Mark: {score}, Test Failed")
    print("GoodBye")
    
Begin()