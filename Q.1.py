#1) Write a program to accept a number from user and display its table in the 
# given format:
num=int(input("Please enter a number"))
print("The table of number",num,"is")

for x in range(1,11):
    print(num,"X",x,"=",num*x)