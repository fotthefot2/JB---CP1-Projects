#Judah Beagley, period 1, multiplication table
#you are evil for this
import time
print("here is the multiplication table")
#the i and y in range work together to be multiplied then laid out in a table
for i in range(1,16):
    for y in range(1,16):
        print(f"{i*y:4}",end="")#cool math stuff
        time.sleep(.01)#makes it look cooler
    print()#for new lines
