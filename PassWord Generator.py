import random
import string
alphabets = string.ascii_letters
numbers = string.digits
less_ch = '#$%'
characters = '!~@#$%^&*(_+|?><|)'
total = ""
def generate_password(level, length):
    if level == "simple":
        total = alphabets + numbers
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
    elif level == "medium":
        total = alphabets + numbers + less_ch
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
        
    elif level == "tough":
        total = alphabets + numbers + characters
        password =  ''.join(random.choice(total) for _ in range(length))
        return password
        
    else:
        return "Invalid Choice"
        
print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To RANDOM PASSWORD GENERATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆ \n")
try:        
    length = int(input("Enter desired length of Password(min=4 , max=16): "))
    while(length not in range(4,21)):
        print("Length not Suitable,\n ")
        length = int(input("Enter Length Again: "))
except:
    print("Invalid Input.\nexiting.......")
    exit()
list2 = ['simple', 'medium','tough']
level = input("Enter Complexity level ('simple', 'Medium','tough'): ").lower()
while(level not in list2):
    print("Invalid Input")
    level = input("Enter Complexity level ('simple', 'Medium','tough'): ").lower()
        

password = generate_password(level,length)
print(f"Password Generated is: {password}")
print("Thanks for Using!!\n exiting...")
    