n=0
while n<3:
     answer=input("do you want to continue? (yes/no): ")
     if answer=="yes":
        print("glad to hear that you want to continue")
        break
     else:
         n+=1
else:
     print("3 strikes, you are out!")
     