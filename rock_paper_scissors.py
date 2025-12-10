import random

print("=====================")
print("Rock Paper Scissors")
print("=====================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

user_choice = int(input("Pick a number (1-3): "))
com_choice = random.randint(1, 3)

if user_choice == 1:
    print("You picked ✊")
elif user_choice == 2:
    print("You picked ✋")
elif user_choice == 3:
    print("You picked ✌️")
else:
    print("Invalid choice! Please pick a number between 1 and 3.")
    exit()

if com_choice == 1:
    print("Computer picked ✊")
elif com_choice == 2:
    print("Computer picked ✋")
elif com_choice == 3:
    print("Computer picked ✌️")

if user_choice == com_choice:
    print("It's a tie!")
elif (user_choice == 1 and com_choice == 3) or \
     (user_choice == 2 and com_choice == 1) or \
     (user_choice == 3 and com_choice == 2):        
    print("You win!")
else:
    print("Computer wins!") 
      

