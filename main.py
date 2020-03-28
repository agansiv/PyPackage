from Modules import Sub as s,Add as a,squareroot as sq

print("Sum is : ",a.add() ,end = "\n")
print("Subraction is : ",s.sub(),end =" *\n")
try:
    print ("Squareroot is : " ,sq.sqroot())
except:
    print("Negatigve value has been entered ",sq.val)
    raise

