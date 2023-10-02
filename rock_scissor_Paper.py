import random
def winner_msg():
    print("Hurrah! You Won......")

def loser_msg():
    print("OOPS! You lose......")
    
def print_choices(str,str2):
    print(f"Computer's Choice: '{str.capitalize()}'  ||  User's Choice: '{str2.capitalize()}'")

def print_winner(string1,string2):
    print(f"{string1.capitalize()} beats the {string2.capitalize()}\n")
    
list_choice = ["Rock", "Scissor","Paper"]
RULES = """\n-->Rock wins against Scissors;
-->Paper wins against Rock; 
-->Scissors wins against Paper\n"""
computer_choice = random.choice(list_choice).lower()
print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To 'Rock','Scissor','Paper' GAME ☆*: .｡. o(≧▽≦)o .｡.:*☆\n ")
user_choice = input("Enter Your Choice ('Rock','Scissor','Paper')\n-->Press 'q' to exit\n-->type 'rules' for GAME RULES:\n--> ").lower()
while(True):
    if computer_choice == user_choice:
        print_choices(computer_choice,user_choice)
        print("Game Tie!!")
    elif user_choice =='q':
        print("Thanks for Playing!\nexiting.......")
        exit()
    elif user_choice == "rules":
        print(RULES)
    elif computer_choice =="rock":
        if user_choice =="paper":
            print_choices(computer_choice,user_choice)
            winner_msg()
            print_winner(user_choice,computer_choice)
        elif user_choice =="scissor":
            print_choices(computer_choice,user_choice)
            loser_msg()
            print_winner(computer_choice,user_choice)
        else:
            print("Invalid Choice!")
    elif computer_choice == "scissor":
        if user_choice =="rock":
            print_choices(computer_choice,user_choice)
            winner_msg()
            print_winner(user_choice,computer_choice)
        elif user_choice =="paper":
            print_choices(computer_choice,user_choice)
            loser_msg()
            print_winner(computer_choice,user_choice)
        else:
            print("Invalid Choice!")
    elif computer_choice=="paper":
        if user_choice == "rock":
            print_choices(computer_choice,user_choice)
            loser_msg()
            print_winner(computer_choice,user_choice)
        elif user_choice == "scissor":
            print_choices(computer_choice,user_choice)
            winner_msg()
            print_winner(user_choice,computer_choice)
        else:
            print("Invalid Choice")
    else:
        print("Invalid Input!!!..choose any ['rock','scissor','paper']")
    user_choice = input("Enter Your Choice ('Rock','Scissor','Paper')\n-->Press 'q' to exit\n-->type 'rules' for GAME RULES:\n--> ").lower()
            
