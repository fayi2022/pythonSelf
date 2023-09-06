#Program to understand list operations in Python
values=["Shahdan","Yousuf","Cuber"]
values=values+["10Q","GAES"]  #To add extra two items
print("The entered list is: ")
print(values)
values[2]="Yahiya" #To change the third value
print(values[1])  #To print the item in indevalue 1
print(values[-1])  #To print the last item
print(values[2:]) #To print the item from index value 2 to index value at the end
print(values[-3:-1])  #To print the item frm index value -3 to the item just before last item
values.append("Petname is Shanthanu") #To append extra item at the end
print(values) #Print the entire list