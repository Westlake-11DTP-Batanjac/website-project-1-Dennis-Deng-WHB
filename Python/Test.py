# Performer: Karl Urban, born in Wellington, New Zealand

def Begin():
    Player = input(("Welcome to the quiz. What's your name? "))
    print(f"Alright {Player}, now you will answer the following eight questions about Karl Urban, a New Zealand actor. Wish You Luck.")
    print("------Loading...------")
    Quiz()

def Quiz():
    score = 0
    Question_set_1 = ["Christchurch", "Wellington", "Auckland"]
    Q_Num = 1
    Answers = 1
    print("Question 1: In what city is Karl Urban born?")
    for i in Question_set_1:
        print(f"{Answers}. {i}")
        Answers += 1
    while True:
        try:
            answer = int(input("Enter answer number: "))
            Check(Q_Num, answer, score)
        except:
            print("An error occured, retry")

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 2
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 3
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 4
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 5
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 6
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 7
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

    # Question = ["Christchurch", "Wellington", "Auckland"]
    # Q_Num = 8
    # Answers = 1
    # print("Question 1: In what city is Karl Urban born?")
    # for i in Question:
    #     print(f"{Answers}. {i}")
    #     Answers += 1
    # answer = input("Enter your answer: ").strip().lower()
    # Check(Q_Num, answer)

def Check(Q_Num, answer, score):
    if Q_Num == 1:
        if answer == 2:
            score = score + 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Score: {score}")
    # elif Q_Num == 2:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 3:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 4:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 5:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 6:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 7:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    # elif Q_Num == 8:
    #     if answer == "wellington":
    #         score += 1
    #         print(f"Correct! Score: {score}")
    #     else:
    #         print(f"Wrong! Score: {score}")
    
Begin()