print("="*18)
print("KBC (Kaun Banega Crorepati)")
print("="*18)

player_prize=[]
questions=["Who is Prime Minster of India","Name the programming language loved by hackers"]
answers=["Narendra Modi","Python"]

for i in questions:
    if i==questions[0]:
        print(questions[0])
        print("1. Narendra Modi        2. Vladimir Putin        3. Dronald Trump      4. Xi Xingpi")
        usr_ans=input("Write answer: ")
        if usr_ans==answers[0]:
            print("Sahi jawab")
            print("Won $500")
            player_prize.append(500)
        else:
             print("Wrong")

    elif i==questions[1]:
        print(questions[1])
        print("1. C++       2.Python     3. C       4. Java")
        usr_ans=input("Write answer: ")
        if usr_ans==answers[1]:
            print("Sahi jawab")
            print("Won $1000")
            player_prize.append(1000)
        else:
            print("Wrong")

print(f"Total Prize you won {player_prize[0]+player_prize[1]}")
            
        

            
   

 


