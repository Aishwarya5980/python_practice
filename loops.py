for i in (1,2,3):
    print(i)

for i in range(0,10):
    print(f"round : {i} ")

item=[1,23,56,567]
for i in item:
    print(i)

for i in range(0,10,2):
    if i==6:
        break
    else:
        print(i)

for i in range(0,10,2):
    if i==2:
        break
    else:
        print(i)
else:
        print("kas kas")

names=["aishwarya","baraa","maria"]
for name in names:
    if name==None:
        print("Found missing name")
        break
else:
        print("""All names are present""")

file_list=["file1.txt","file2.txt","file3.txt","file3.txt"]
for file in file_list:
     if file_list.count(file)>1:
          print(f"{file} is duplicate")
          break
     
for x in range(2):
     for y in range(3):
            print(f"x={x}, y={y}")  
     
colors=["red","green","blue"]
size=["S","M","L"]
for color in colors:
     for s in size:
            print(f"color={color}, size={s}")

years=[2020,2021,2022]
month=["Jan","Feb","Mar"]
days=range(1,29)
for year in years:
     for mon in month:
          for day in days:
               print(f"report_{year}_{mon}_{day}.csv")


answer=""
while answer != "yes":
     answer=input("do you want to continue? (yes/no): ")
print("thankyou") 

