#function operations for user defined math operations
def add(x,y):      #Addition function definition
    z=x+y    
    return z
def sub(x,y):      #Subtraction function definiton 
    z=x-y           
    return z
def mul(x,y):      #Multiplication function definition
    z=x*y
    return z
def div(x,y):      #Division function definition
    z=x/y
    return z
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("addition of ",a,b,add(a,b), "subtraction ",a,b,sub(a,b), "Multiplication",a,b,mul(a,b),"Division ",a,b,mul(a,b),)

