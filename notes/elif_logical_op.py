# JB, Elif and logical operators notes

age = 15
licence = True
if age >= 18:
    print("you are an adult and can vote")
elif age >= 15 and licence:
    print("you can drive legally. good for you! You are a minor")
elif age >= 15 and not licence:
    print("you could drive but uhh you gotta get a license. you are a minor")
else:
    print("you are a minor. go to school")
