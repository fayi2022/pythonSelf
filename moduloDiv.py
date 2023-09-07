x=int(input("Enter the first num:"))
y=int(input("Enter the second number:"))

if(y!=0) :
    z=x%y
    print("The remainder is:"+str(z))
    if(y<0) :
        print("The divider is negative")
else :
    print("Division is not defined")

