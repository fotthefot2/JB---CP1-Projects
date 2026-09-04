# Judah Beagley, period 1, average grade assignment

#time to see if the while true will work like how i hope it will
print("enter in your grades. only use numbers.")
#this will be used for an append 
grades = []
#the range makes it so i can use just a single f string not a bunch of stuff
for i in range(7):
        while True:
            try:
                 #the f string makes it way shorter while still getting the job done
                 grade = float(input(f"period {i+1}: "))
                 #the append lets me be lazy and has it show all of it neatly.
                 grades.append(grade)
                 break
            except ValueError:
                  print("*only numbers*")

print("here are your grades" ())