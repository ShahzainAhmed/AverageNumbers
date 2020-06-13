# Taking input from the user for the list and numbers.
n=int(input("Enter the number of elements to be inserted: "))
a=[]

# Using for loop and range.
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))
