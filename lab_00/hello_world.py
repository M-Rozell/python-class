# print("Hello World!")
# def my_function():
#   print("Hello from a function")
# my_function()

def add_together(num_1, num_2):
    "docstrings happening"
    result = num_1 + num_2 # addition in python
    return result # return the result
print(add_together(3,4))    



def multiply(num_1, num_2):
    "multiplying numbers"
    # return None
    result = num_1 * num_2
    return result
print(multiply(10,12))

def power(num, power_raise):
    "Power Raise Activated!!"
    result = num ** power_raise
    return result
print(power(3,2))

def subtract(num_1, num_2):
    "Subtraction"
    result = num_1 - num_2
    return result
print(subtract(10,5))

def printinfo(name, age):
    "Printing Name and Age info"
    print ("Name: ", name)
    print ("Age: ", age)
    return
printinfo(age=41, name="Maggie")
        


