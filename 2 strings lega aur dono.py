# Question 7
# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length 
# jyaada hogi use print karega aur agar dono strings ki length equal hui to dono ko line by 
# line print karega . Hint :- use len() builtin function..
# Input:-
# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)
# Output :-
# welcome
# sonu
# monu


def definekaro(x,y):
    if len(x)==len(y):
        print("both are eyual ")
    else:
        print(x,"and",y)    
a=str(input("Enter the name: "))
b=str(input("Enter the name: "))
definekaro(a,b)

