import random

a = int(random.randint(1,3))
print (a)

answer = int(input("Guess the number I'm thinking of 1 to 3: " ))

if answer == a:
    print ("nice!")

if answer > a:
    print("Too High!")
        
if answer < a:
    print("Too Low")

while answer != a:
    answer = int(input("Guess the number I'm thinking of 1 to 3: " ))
    if answer != a: 
        if answer > a:
            print("Too High!")
        
        if answer < a:
            print("Too Low")
            
    if answer == a:
        print("way to go! " )  
        

