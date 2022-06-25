# Program 2

a = input("Enter your Name \n")
b = input("Enter a Date \n")


Letter = '''Dear <|name|> 
You are Selected 
Date: <|date|> '''

Letter = Letter.replace("<|name|>", a)
Letter = Letter.replace("<|date|>", b)

print(Letter)