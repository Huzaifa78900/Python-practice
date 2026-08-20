import random

def game():
    score=random.randint(1,100)
    with open("highscore.txt") as f:
        highscore=f.read()
        if highscore!="":
            highscore=int(highscore)
        else:
            highscore=0

    if score>highscore:
        with open("highscore.txt","w") as f:
            f.write(str(score))
        print("New high score:",score)

    return score


game()

