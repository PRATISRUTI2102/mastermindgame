import random
num = random.randrange(1000,9999)
n = int(input("GUESS THE 4 DIGIT NUMBER"))
if (n==num): 
    print("GREAT! YOU GUESSED THE NUMBER IN JUST 1 TRY. YOU ARE A MASTERMND!")
else:
    ctr = 0
    while(n != num):
        ctr += 1
        count = 0
        n = str(num)
        num = str(num)
        correct = ['X']*4
        for i in range(0, 4):
            if(n[i] == num[i]):
                count += 1
                correct[i] = n[i]
            else:
                continue
            print("NOT QUITE THE NUMBER. BUT YOU DID GET",count,"digit(s) correct!")
            print('\n')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))
            elif (count == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))
 
   
    if n == num:
        ctr+=1
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")