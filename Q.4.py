age=int(input("Please enter your age"))
if age>18:
    print("You are already voting")
elif age<18:
    print("You are still small you will start voting in",18-age,"years.")
elif age==18:
    print("This year you will start voting")
else:
    print("Invalid entry try again")