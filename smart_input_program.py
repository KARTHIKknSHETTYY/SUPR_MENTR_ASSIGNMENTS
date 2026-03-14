# taking user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# categorizing age using conditionals
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

# personalized message
print("\nHello", name + "!")
print("You are", age, "years old and you are", category + ".")
print("It's great that you enjoy", hobby + "!")