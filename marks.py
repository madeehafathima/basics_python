name=input("enter name:")
m=int(input())
if(m>=90):
    grade="Grade A+"
elif(80<=m<=89):
    grade="Grade B"
elif(70<=m<=79):
    grade="Grade C"
elif(60<=m<=69):
    grade="Grade D"
else:
    grade="fail"
print(grade)
