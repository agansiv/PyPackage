from sys import path
path.append('..\\extra\\venv')
from Modules import Sub as s ,Add as a

print (s.sub()," ",a.add() ,end = "  !!!! \n")