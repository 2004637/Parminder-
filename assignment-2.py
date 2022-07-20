'''num=int(input("enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(tem==rev):
        print("the number is palindrome!")
    else: 
        print("is not a palindrome!")'''
  

'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    n=int(input("input a number to compute the factorial:"))
    print(factorial(n))'''
 
'''nterms=int(input("how many terms"))
n1,n2=0,1
cout=0
if nterms <=0:
    print("please enter a positive integer")
elif nterms==1:    
        print("fibonacci sequenceupto",nterms,";")
        print(n1)
else:        
          print("fibonacci sequence:")
          while cout<nterms:
              print (n1)
              nth=n1+n2
              n1=n2
              n2=nth
              cout+=1'''

              
'''def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("selet operation.")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
while True:

    choice=input("enter choice(1/2/3/4): ")
    if choice in('1','2','3','4'):
        num1=float(input("enter first number: "))
        num2=float(input("enter second number: "))
        if choice == '1':
                   print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
                   print(num1,"-",num2,"=",substract(num1,num2))
        elif choice == '3':
                   print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == '4':
                   print(num1,"/",num2,"=",divide(num1,num2))
        next_calculation = input("let's do next calculation?(yes/no): ")
        if next_calculatiom == "no":
            break
else:
    print("invalid input")'''


'''rows=int(input("enter a number of rows:"))
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("* ",end="")
        k +=1
    k=0
    print()'''


'''year=2000
if(year%400 == 0) and (year%100 == 0):
    print("{0} is a leap year".format( year))
elif(year%4 == 0) and (year%100 != 0):
                       
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))'''

    






                       


























              



    
          



                  
                         
                         
   

                         
           
           

