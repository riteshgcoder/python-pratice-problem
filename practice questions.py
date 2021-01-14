 Q1. Python program to check a no. is even or odd.

"""

logic:-

x%2==0 true(even)

      false(odd)"""

x=int(input("Enter a no."))

if x%2==0:

    print(x,'Even')

else:


    print(x,'Odd')

💨Output

-----------------------------------------------------


Q2. Python program to add two no.

x=int(input("Enter first no."))
y=int(input("Enter second no."))
s=x+y
print(s)

💨Output

Enter first no.6
Enter second no.7
13
>>>

----------------------------------------------------------------


 Q3. Python program to check a leap year or not.
"""
leap year=366 days
non leap year=365 days

(logic):-
x%400==0      T(L.Y)
              F(x%4==0 and x%100!=0)    T(LY)
                                        F(Non LY)"""
x=int(input("Enter a year"))
if x%400==0:
    print('year is leap')
elif x%4==0 and x%100!=0:
    print('year is leap')
else:
    print('Non leap year')


💨Output
Enter a year2016
year is leap
>>> 
= RESTART: C:/Users/ritesh gupta/AppData/Local/Programs/Python/Python38/prac_prog.py
Enter a year2017
Non leap year
>>> 

------------------------------------------------------------------------------------------------------
    
        
 Q5. Python program to print first 10 natural no.
i=1
while i<=10:  #condition
    print(i)
    i+=1

💨Output
1
2
3
4
5
6
7
8
9
10
>>> 

# OR in one line
i=1
while i<=10:
    print(i, end="  ")
    i+=1

💨Output
1  2  3  4  5  6  7  8  9  10  
>>> 

# for loop se
for i in range(1,11):
    print(i, end=" ")


💨Output
1  2  3  4  5  6  7  8  9  10  
>>> 

# in one line
print([i for i in range (1,11)])

💨Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 

--------------------------------------------------------------------


 Q6. Python program to print first 10 natural no. in reverse order.
# while loop se
i=10

while i>=1:

    print(i, end=" ")

    i-=1

💨Output
10 9 8 7 6 5 4 3 2 1 
>>> 

# for loop se
for i in range(10,0,-1):
     print(i, end=" ")

💨Output
10 9 8 7 6 5 4 3 2 1 
>>> 

--------------------------------------------------------------------------

 Q7. Python program to reverse a tuple.

""" list:- reverse function hota hai
but tuple:- reverse function nhi hota hai"""

t=eval(input("Enter"))
print("entered tuple is",t)
l=list(t)
l.reverse()
t=tuple(l)
print('reverse of tuple is',t)

💨Output
Enter1,2,3,4
entered tuple is (1, 2, 3, 4)
reverse of tuple is (4, 3, 2, 1)
>>> 

-----------------------------------------------------------------------------------------------------------------------

 Q8. Python program to print indices of all the occurence of a given element in a given list.


l=[eval(x) for x in input("enter list element").split(',')]

element=eval(input("Enter element value"))

index=0

while index<len(1):

    if l[index]==element:

        print(index,end=' ')

        index+=1

-----------------------------------------------------------------------------------------------------

 Q9. Python program to return next prime no.
def next_prime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n

-----------------------------------------------------------------------------------------------------

                
            
 Q10. Python program to create list of first N prime no.
"""

-prime producer(N)

-Next prine(num)

-use generator to produce list of n prime no."""



def next_prime(num):

    while True:

        num+=1

        for i in range(2,num):

            if num%i==0:

                break

        else:

            return num

def prime_producer(N):

    num, count=1,1

    while count<=N:

        num=nextprime(num)

        yield num

        count+=1

N=int(input("How many prime no. you want to generate?"))

---------------------------------------------------------------------------------------------------------


 Q11. Python program to calculate factorial in single line.
f= lambda n:n*f(n-1) if n>0 else 1
print(f(5))

O/P:-120

--------------------------------------------------------------------------------------------------------

 Q12. Python program to remove duplicate character from a string.
'''
s=aabbccbcbc
s=abc'''

s=input("Enter a string")
i=o
s1=" "
for x in s:
    if s.index(x)==i:
        s1+=x
    i+=1
print(s1)


💨Output
= RESTART: C:/Users/ritesh gupta/AppData/Local/Programs/Python/Python38/jdj.py =
Enter a stringaabbcc
 abc
>>> 

----------------------------------------------------------------------------------------------------

 Q13. Python program to calculate area of circle.
a=int(input("Enter radius of circle"))
x=3.14*a*a
print('Area of circle is',x)

💨Output
Enter radius of circle4
Area of circle is 50.24
>>> 

# Reduce code
x=3.14*int(input("Enter radius of circle"))**2
print('Area of circle is',x)
💨Output
Enter radius of circle4
Area of circle is 50.24
>>> 

# in one line

print('Area of circle is',3.14*int(input("Enter radius of circle"))**2)

💨Output
Enter radius of circle4
Area of circle is 50.24
>>>

------------------------------------------------------------------------------------------------------


 Q14. Python recursive function to calculate sum of square of first N natural no.
'''

n=5

=1+4+9+16+25=55'''



def sum(n):

    if n==1:

        return 1

    return n**2 +sum(n-1)

# in one line
sum=lambda n:1 if n==1 else n**2+sum(n-1)

---------------------------------------------------------------------------------------------------------

Q15. Python program to reverse a string.


s=input("Enter a string")

print(s[::-1])

💨Output
Enter a string Ritesh
hsetiR
>>> 

-----------------------------------------------------------------------------------------

 Q16. Python program to print table of 5.
for i in range(1,11):

    print(5,"x",i,"=",i*5)

💨Output
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
>>> 

# formated string se
for i in range(1,11):
    print("5*%d=%d"%(i,i*5))
💨Output
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45
5*10=50
>>> 

------------------------------------------------------------------------------------------------

 Q17. Python program to print table according to user choice.
n=int(input("Enter a no."))
for i in range(1,11):
    print(n,"*",i,"=", n*i)
    
💨Output
Enter a no.2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
>>> 

# formatted string se
n= int(input("Enter a no."))
for i in range(1,11):
    print("%d* %d=%d"%(n,i,n*i))
💨Output
Enter a no.7
7* 1=7
7* 2=14
7* 3=21
7* 4=28
7* 5=35
7* 6=42
7* 7=49
7* 8=56
7* 9=63
7* 10=70
>>> 

-------------------------------------------------------------------------------


 Q18. Python progam to calculate simple interest.
'''
SI=PRT/100'''


p=float(input("Enter principle amount"))
r=float(input("Enter rate of interest"))
t=float(input("Enter time:"))
si=p*r*t/100
print(si)

💨Output
Enter principle amount100
Enter rate of interest4.5
Enter time:3
13.5

--------------------------------------------------------------------------------

 Q19. Python program to check divisibility of a no. by 5
x=int(input("Enter a no."))

if x%5==0:

     print(x,"is divisible by 5")

else:

     print(x,"is not divisible by 5")


💨Output
Enter a no.31
31 is not divisible by 5
>>> 

--------------------------------------------------------------------------------------------

 Q20. Python program to check no. positive, negative and zero.
x=int(input("Enter a no."))

if x>0:

    print("+ve")

elif x<0:

    print("-ve")

else:

    print("Zero")

💨Output
Enter a no.-4
-ve
>>> 

--------------------------------------------------------------------------------

 Q21. Python program to print first 10 odd natural no.
for i in range(1,20,2):
    print(i,end=" ")

OR
for i in range(1,20):
    print(i,end=" ") if i%2 else print(end=" ")

OR
i=1
while i<=19:
    print(i,end=" ")
    i+=2
💨Output
1 3 5 7 9 11 13 15 17 19 
>>> 

-------------------------------------------------------------------------------------------------

 Q22. Python program to print first 10 even natural no.
for i in range(2,21,2):
    print(i,end=" ")

OR
for i in range(2,22):
    print(i,end=" ") if i%2==0 else print(end=" ")

OR
i=2
while i<=20:
    print(i, end=" ")
    i+=2

OR
i=1
while i<=10:
    print(2*i,end=" ")
    i+=1

💨Output
2 4 6 8 10 12 14 16 18 20 
>>> 

-------------------------------------------------------------------------------------

 Q23. Python program to print first n natural no.
n=int(input("Enter a no."))
i=1
while i<=n:
    print(i,end=" ")
    i+=1

#OR for loop se
n= int(input("Enter a no."))
for i in range(i,n+1):
    print(i,end=" ")
    

💜💨Output
Enter a no.20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
>>> 

------------------------------------------------------------------------------------------
 
 Q24. Python program to check prime no.
n=int(input("Enter a no."))
if n<2:
    print("Not a prime no.")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime no.")
            break
    else:
        print("prime no.")
          
💨Output
Enter a no.7
prime no.

-------------------------------------------------------------------------------------------

 Q25. Python program to calculate volume of cuboid.

print("Enter length, breath and height of cuboid")
l,b,h=float(input()),float(input()),float(input())
v=l*b*h
print(v, "volume")

💛💨Output
Enter length, breath and height of cuboid
12
2
4
96.0 volume
>>> 

--------------------------------------------------------------------------------------------------------

 Q26. Python program to print first N natural no. in reverse order.
n=int(input("Enter a natural no."))

while n:

     print(n,end=" ")

     n-=1

OR
n=int(input("Enter a natural no."))
i=1
while i<=n:
    print(n-i+1,end=" ")
    i+=1

OR
n= int(input("Enter a natural no."))
for i in range(n,0,-1):
    print(i,end=" ")

💙💨💦Output
Enter a natural no.15
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
>>> 

---------------------------------------------------------------------------------------------------

 Q27. Python program to arrange three words in dictionary order.(by using min max func.)
print("Enter three city names")
a,b,c=input(),input(),input()
print(min(a,b,c))
x=a,b,c
if x==a:
    print(min(b,c),max(b,c))
elif x==b:
    print(min(a,c),max(a,c))
elif x==c:
    print(min(a,b),max(a,b))

OR in one line
[for x in sorted(input("Enter comma seperated three cities names").split(',')) if print(x,end=" ")]


🗽Output
Enter three city names
mumbai
chennai
pune
chennai
>>> 

--------------------------------------------------------------------------------------------------------------

Q28. Python program to print first N odd natural no. in reverse order. 
n=int(input("Enter a natural no."))
for i in range(1,n+1):
    print(2*n-2*i+1,end=" ")

OR
n=int(input("Enter a natural. no"))
for i in range(2*n-1,0,-2):
    print(i,end=" ")

💣Output
Enter a natural. no10
19 17 15 13 11 9 7 5 3 1 
>>>

-------------------------------------------------------------------------------------------------------

 Q29. Python program to print first N even natural no. in reverse order.
n=int(input("Enter a natural no."))
for i in range(1,n+1):
    print(2*n+2-2*i,end=" ")

💞OR
n=int(input("Enter a natural no."))
for i in range(2*n,1,-2):
    print(i,end=" ")

💤Output
Enter a natural no.5
10 8 6 4 2 
>>> 

--------------------------------------------------------------------------------------------

 Q30. Python program to short a list of a no.
l=[int(e) for e in input("Enter no. seprated by commas.").split(',')]
print(l)
l.sort()
print(l)

👻Output
Enter no. seprated by commas.10,2,3,7,9,1
[10, 2, 3, 7, 9, 1]
[1, 2, 3, 7, 9, 10]
>>> 

---------------------------------------------------------------------------------------------------------


 Q31. Write a recursive function to calculate sum of first N natural no. in python.
    def sumN(n):
    if n==1:
        return 1
    return sumN(n-1)+n

💪Output
>>> x=sumN(5)
>>> x
15
>>> 

----------------------------------------------------------------------------------------------------------

 Q32. Write a recursive python function to print first N even natural no.
def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n, end=" ")

👮Output
>>> printNeven(5)
2 4 6 8 10 
>>> 

-----------------------------------------------------------------------------------------------------------------

Q33. Python program to count frequency of elements of a tuple.
t=(1,2,3,1,1,2,3)
i=0
for e in t:
    if t.index(e)==i:
        print(e,"--",t.count(e))
        i+=1
👳Output
1 -- 3
2 -- 2
3 -- 2
>>> 

--------------------------------------------------------------------------------------------------------------------

 Q34. Recursive function to print first N even natural no. in reverse order in python.
def printevenreverse(n):
    if n>0:
        print(2*n,end=' ')
        printevenreverse(n-1)
👦Output
>>> printevenreverse(10)
20 18 16 14 12 10 8 6 4 2 
>>> 

--------------------------------------------------------------------------------------------------------------

 Q35. Return multiple value from pyhton function.
def fun():
    return 1,2,3,4,5
💞Output
>>> x=fun()
>>> x
(1, 2, 3, 4, 5)
>>> 

# Agar simply dekhe
>>> a=1,2,3
>>> a
(1, 2, 3)
>>> type(a)
<class 'tuple'>
>>> 

-----------------------------------------------------------------------------------------------------------------

 Q36. Pyhton function always return something.
def f1():
    print("Hello")

👨Output
>>> x=f1()
Hello
>>> 

# Agar simply dekhe..
>>> x=f1()
Hello
>>> x
>>> print(x)
None # kuch nahi ko bhi return krega..
>>> type(x)
<class 'NoneType'>
>>> 

-----------------------------------------------------------------------------------------------------------------


 Q37. Python start pattern.
for i in range(1,5):
    for j in range(1,5):
        if j>=1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

🙇Output
* * * *
  *  * *
     * *
       *

---------------------------------------------------------------------------------------------------------------------


 Q39. Python program to calculate factorial of a bigger no.
def f(n):
    f=1
    while n:
        f=f*n
        n-=1
    return f

👽Output
>>> f(5)
120
>>> 
============================================ RESTART: C:/Users/ritesh gupta/AppData/Local/Programs/Python/Python38/hehd.py ============================================
>>> f(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Q40. Python program to print marksheet of students.
print("Enter marks of 5 subject")

a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())

if a>=33 and b>=33 and c>=33 and d>=33 and e>=33:

    print("result:pass")

    per=(a+b+c+d+e)/5

    print("percentage:",per)

    if per>=60:

        print("First")

    elif per>=50:

        print("second")

    else:

        print("thrid")

else:

    print("fail")

💃Output
Enter marks of 5 subject
3
33
33
33
33
fail
>>> 
= RESTART: C:/Users/ritesh gupta/AppData/Local/Programs/Python/Python38/hehd.py
Enter marks of 5 subject
72
73
89
37
86
result:pass
percentage: 71.4
First
>>> 

----------------------------------------------------------------------------------------------------------------------------

 Q41. Python program to merge two tuples.
t1=(10,20,30,40)
t2=(5,9,12,18,22,25)
t3=[]
i,j,k=0,0,0
while i<len(t1) and j<len(t2):
    if t1[1]<t2[j]:
        t3.append(t1[i])
        i+=1
        k+=1
    else:
        t3.append(t2[j])
        j+=1
        k+=1
if i==len(t1):
    while j<len(t2):
        t3.append(t2[j])
        j+=1
        k+=1
elif j==len(t2):
    while i<len(t1):
        t3.append(t1[i])
        i+=1
        k+=1
t3=tuple(t3)
print(t3)
👮Output
(5, 9, 12, 18, 10, 20, 30, 40, 22, 25)
>>>

---------------------------------------------------------------------------------------------------------------

 Q42. python pattern program.
n=int(input("Enter the size"))
for i in range(n):
    string="*"*(i+1)
    string+=''*(2*(n-i-1))
    string+='*'*(i+1)
    print(string)
for i in range(n-1):
    string='*'*(n-i-1)
    string+=''*(2*(i+1))
    string+='*'*(n-i-1)
    print(string)   

💥Output
Enter the size10
**
****
******
********
**********
************
**************
****************
******************
********************
******************
****************
**************
************
**********
********
******
****
**




