import random

print("you want to play y or n")
select=input()

while(select=='y'):
    score=0
    word = ['father', 'brake', 'country', 'green','aeroplane']

    def checkword(x):
        checkrandom=[]

        for same in checkrandom:
            if same==x:
                newword = random.choice(word)
                checkword(newword)

        checkrandom.append(x)

    for i in range(5):
        i=random.choice(word)
        checkword(i)

        x=list(i)

        random.shuffle(x)
        shuffleword="".join(x)

        print("Guess the word:", shuffleword)
        userinput=input("Input:")

        print("")

        if i==userinput:
            print("Correct")
            score+=1
        else:
            print("Wrong")
            score-=1
    print("")
    print("Net Score",score)
    print("Game Over")
    print("you want to play again y or n")
    select=input()
