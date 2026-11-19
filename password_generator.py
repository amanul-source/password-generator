while True:
 import random
 import string
 user_input=input("Do you want to generate password (yes/NO):")

 if user_input == 'yes':
    print("**********WELCOME TO PASSWPORD GENERATER**********")

    password=int(input("Enter number of digit you want in password:-"))
    characters=string.ascii_letters+string.digits+string.punctuation

    generated_password=""

    for i in range (password):
     generated_password+=random.choice(characters)
    print("Your passowrd is: ",generated_password)

 else:
  break   
 
