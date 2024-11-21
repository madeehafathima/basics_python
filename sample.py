name=input(" ")
age = int(input())
if(age>=18):
    print(f"{name} is eligible to vote")
else:
    print(f"comeback after {18-age} years")