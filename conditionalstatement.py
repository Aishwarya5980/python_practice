password="8694q Qwertttttt"
password=password.strip()
if password =="":
    print("password cannot be empty")
elif len(password)<9:
    print("password must be at least 8 characters long")
elif not any (c.isupper() for c in password):
    print("password must contain at least one lowercase letter")
elif not any (c.islower() for c in password):
    print("password must contain at least one uppercase letter")
elif " " in password:
    print("password cannot contain spaces")
else:
    print("password is valid")
score=58
print("A") if score >= 90 else print("B") if score >= 80 else print("C") if score >= 70 else print("D") if score >= 60 else print("F")

#match case statement
country="India"
match country:
    case "United States":
        print("Capital: Washington, D.C.")
    case "India":
        print("Capital: New Delhi")
    case "United Kingdom":
        print("Capital: London")
    case "Australia":
        print("Capital: Canberra")
    case _:
        print("Country not found")