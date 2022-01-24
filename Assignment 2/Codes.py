Q1 : 


input_string=input("Enter the string: ")

print("Length of string :",len(input_string))

print("Reverse of string is : ","'"+input_string[-1: :-1]+"'")

slicestr=input_string[slice(9,26)]
print(slicestr)

newstring=input_string.replace("a case sensitive","object oriented")
print(newstring)

print("Index of substring 'a' is",input_string.index('a') )

print(input_string.replace(" ",""))

Q2 :

name=input("Please enter your name: ")
sid=input("Enter SID: ")
department=input("Enter department name: ")
cgpa=float(input("Enter CGPA: "))
print("");
print('''Hey, %s Here!
My SID is %s
I am from %s department and my CGPA is %s'''%(name,sid,department,cgpa))
   

Q3 :

a=56
b=10
print("a&b: ",a&b)
print(" ")
print("a|b: ",a|b)
print(" ")
print("a^b: ",a^b)
print(" ")
print("a<<2:",a<<2,"and", "b<<2: ",  b<<2)
print(" ")
print("a>>2:",a>>2, "and b>>4",b>>4)

Q4 :
    
num1=input("Enter the first number : ");
num2=input("Enter the Second number : ");
num3=input("Enter the Third number : ");
if(num1 > num2 and num1 > num3):
    print("The greatest number is : ",num1)
elif(num2 > num1 and num2 > num3):
    print("The greatest number is : ",num2)
else :
    print("The greatest number is : ",num3)

Q5 :
inp_string=input("Enter the string: ")
if 'name' in inp_string:
    print("yes")

else:
    print("no") 

Q6:

side1=input("Enter the first side : ");
side2=input("Enter the Second side : ");
side3=input("Enter the Third side : ");
if(side1 > side2+side3 or side2 > side1+side3 or side3 > side1+side2):
    print("No")
else:
    print("Yes")
