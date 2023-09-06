#Printing number 1 to 10
print("Printing number 1 to 10")
for i in range(1,11) :
    print(i)
#For printing 1 to 10 with difference 3
print("printing 1 to 10 with difference 3")
for x in range(1,11,3) :
    print(x)

#For printing 1 to 11. But the loop should continue without printing the number 7
print("For printing 1 to 11. But the loop should continue without printing the number 7")
for y in range(1,12):
    if y==7 :
        continue
    print(y)