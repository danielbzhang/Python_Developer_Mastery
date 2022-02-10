import random

answer = random.randint(1, 10)

    while True:
        try:
            # print(answer)
            guess = int(input("Guess a number: "))
            if 0 < guess < 11:
                if answer == guess:
                    print("You are a genius!")
                    break
                else:
                    print("You are close! Please try again!")
                    continue
            else:
                print("The number needs to be btw 1 and 10")
                continue
        except ValueError:
            print('please enter a number')
            continue
