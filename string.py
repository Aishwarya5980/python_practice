# math
text="""Python is easy.
Python is powerful.
I love python ."""
print(len(text))
print(text.count("python"))
age = 25
print("My age is " + str(age))
print("My age is " + repr(age))

# print("My age is " + (age)) # TypeError: can only concatenate str (not "int") to str

#Transformation
price= "1234,567"
print(price.replace(",","."))

phone="+91-1234567890"
print(phone.replace("-","").replace("+91",""))

#Exercise:

Ph="+49 (176) 123-4567"
print(Ph.replace("+","").replace(" ","").replace("(","").replace(")","").replace("-",""))

FirstName= "Aishwarya"
Lastname= "Palani"
print(FirstName+ " " +Lastname)

name= "Aishwarya"
age = 25
is_student= True
print(f"My name is {name}, I am {age} years old,and student status is {is_student} ")
print(f"2+3={2+3}")

CSVdata= "John,Doe,30,Engineer"
print(CSVdata.split(","))

print("ha"*3)
print("="*25)

hello= "hello"
print(hello[3])
print(hello[0:4])
print(hello[1::2])

#cleaning
data= "   Hello, World!    "
print(data.strip())
print(data.lstrip())
print(data.rstrip())
print(len(data))
print(len(data.strip()))
print(len(data.lstrip()))
print(len(data.rstrip()))
dat = "****fghjk***"
print(dat.strip("*"))
print(data.strip().lower())

me= "968-Maria, (D@t@ Engineer);; 27y  "
cleaned_me= me.strip().replace("968-","").replace(";;",",").replace("(","").replace(")","").replace("@","a")
cleaned_1=cleaned_me.replace(","," | ")
print(cleaned_1)

#search
text= "Python is a great programming language. I love Python because it is easy to learn and powerful."
print(text.startswith("Python"))
print(text.endswith("powerful."))
print(text.find("Python"))
print("@" in text)

#validation
country = "USA"
print(country.isalpha())
num=45685855
print(str(num).isnumeric())