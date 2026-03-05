
print("---Strings----")
course = "  Python Programming    "
print(course.upper())
print(course.lower())
print(course.title())
print(course.lstrip())
print(course.rstrip()) 
print(course.find("Pro"))
print(course.find("pro"))
print(course.replace("p","j")) # replae p with j
print("Pro" in course) #return True or False
print("Pro" not in course) 

#x = a + bj , imaginary number 


print("---Numbers----")
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) # floating point number
print(10 // 3) # returns it in integer 
print(10 % 3) # Modulus 3, remainder of divison 
print(10 ** 3) # 10 to the power of 3

print("---Assignent Operator ----")
x = 10 
x = x + 3
x += 3 # this is exactly the same as above 

print("---Working with Numbers----")

print (round(2.9)) 
print(abs (-2.9)) # absolute number

print("---Math Moduel libarary----")
# Math Module, Libary for differnt kinds 
import math
print (math.ceil(2.2))

#strings cant be concatincated if they are not the same type
x=input("x: ") 
print (type (x))
y = int(x) + 1 
print (f"x: {x}, y: {y}")
#y = x + 1  issue with this is that you cant combine a string with an int

