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

                 grades.append(grade)
                 #if the user types anything else other than numbers
                 break
            except ValueError:
                  print("*only numbers*")

average = sum(grades) / len(grades)

print (f"your grade average is {average:.2f}")