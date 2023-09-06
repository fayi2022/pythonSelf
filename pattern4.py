height=int(input("Enter the height of the pattern:"))
print("The pattern is :")
j=height
i=1
while ((i<=height)and(j>=1)) :
    print("\n")
    k=1
    while k<j :
        print(" ",end="")
        k=k+1
    l=1
    while l<=i :
        print("* ",end="")
        l=l+1
    i=i+1
    j=j-1
else :
    print("\nLoop finished")