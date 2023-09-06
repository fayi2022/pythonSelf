#To nunderstand controle statement if elif else
#Program to check weather the entered number is positive, negative or zero
num=int(input("Enter the number:"))
if num>0 :
    print("The enterd number "+str(num)+"is positive")
elif num==0 :
    print("The entered number "+str(num)+"is zero")
elif num<0 :
    print("The entered number " + str(num) + "is negative")
else :
    print("***Wrong entry****")
