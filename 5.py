print( 'add : 1')
print( 'subtraction : 2')
print( 'multiplication : 3')
print( 'divide : 4')

n = input('enter no : ' )
n1 = input('enter no : ')


ch=float(input("enter operation : "))

if ch==1:
    c = float(n) + float(n1)
    print(c)
elif ch==2:
        c = float(n) - float(n1)
        print(c)
elif ch==3:
    c = float(n) * float(n1)
    print(c)
elif ch==4:
    c = float(n) / float(n1)
    print(c)
    
else:

 print ('invaled')




