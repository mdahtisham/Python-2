a1 = int(input("{Enter a number 1 : "))
a2 = int(input("{Enter a number 2 : "))
a3 = int(input("{Enter a number 3 : "))
a4 = int(input("{Enter a number 4 : "))

if (a1 > a4  ):
    win1 = a1
else:
    win1 = a4

if(a2 > a3):
    win2 = a2
else:
    win2 = a3

if (win1 > win2 ):
    print(win1)
else:
    print(win2)



