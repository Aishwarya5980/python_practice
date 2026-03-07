# start
# single line comment
# this is multi line comment
# This is my 1st python code
print()
print("Hi, This is my 1st python code")
print("hello python")


# functions are of the types : Built in functions, user defined functions, lThird party / library functions
# this is built in function
print("\n========================")
print("     Trust Python       ")
print("========================\n")
print('single qotes is accepted in python')

#Escape sequence
# \" - double quote
# \' - single quote
# \\ - backslash
# \n - new line
# \t - tab
# \r - carriage return
# \b - backspace
# \f - form feed
#print("double quote "something" ") #shows error
print("double quote \"something\" \n")
print('double quote "something" ') #this will work without escape sequence because we are using single quote to define string
print("""\nPath:C:\\User\\aish
Path:D:\\Data\n""") #this will work without escape sequence because we are using triple double quote to define string

#exercise
print("Your Learning Path:\n\t- Python Basics \n\t- Data Enginerring \n\t- AI\n")

#variable is a container that holds data. It is a way to store and manipulate data in a program. In Python, you can create a variable by assigning a value to it using the equal sign (=). For example:
name="Aishwarya"
print("my name is", name)
print(name, "is learning python to become expert in it")
language="python"
print("my name is", name, "and I am learning",language,"to become expert in it\n")   
name="Baraa"
#python os executed line by line so the value of name will be updated to "baraa" and the output will be "baraa is learning python to become expert in it"
print(name, "is already a expert in it\n")

#exercise
channel_name="datawithbaraa"
print("info@"+channel_name+".com")
print("support@"+channel_name+".com")
print("www"+channel_name+".com")
print()

#input in python
#Dynamic input from user
name=input('eetr your name:');
#hard coded input
country='USA'
print("my name is", name, "is from", country)

print()
print("I have so far learnt print, input, comment and variables")