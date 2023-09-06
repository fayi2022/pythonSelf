import math
def hey(value) :
    print("Hello I am a function"+value)
hey("Fayisa Yahiya")

def hoi(*names) :
    print("Hoi function is called")
    print(names)
hoi("Shahdan","Ehaan","Yahiya")

def hoo(num1,num2) :
    return num1+num2
sum=hoo(10,30)
print("Sum is:"+str(sum))
square=math.sqrt(sum)
print("Square="+str(square))