# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:37:02 2019

@author: Kankan Joyti
"""

l1=[9,8,7,6,5,4,3]

for i in range(len(l1)):
    position=l1.index(l1[i])+1
    value=l1[i]
    print(position,value)
    
#2
def string(x):
    for i in range(len(x)):
        if(x[i]==" "):
            print(x[i+1:len(x)]+" "+x[0:i])
            break
string("this is given string")        

#3
def prime(n):
    if n==2:
        print("prime")
    else:    
        for i in range (2,n):
           if(n%i==0):
              print("not prime")
              break
        else:
            print("prime")
prime(10)

#4
def fabonaci(n):
    a=0
    b=1
    
    if n==1:
        print(0)
    if n==2:
        print(1)
    else:
        for i in range(3,n+1):
            c=a+b
            a,b=b,c
        print(c)    
fabonaci(5)       

#5
def palindrom(x):
    for i in range(len(x)//2):
        if x[i]!=x[len(x)-(i+1)]:
            print("not")
            break
        else:
            print("yes")
            break
palindrom("geek")            

#6
def area(r):
    a=3.142*r**2
    print(a)
area(5)   

#7
def sum_square(n):
    a=0
    for i in range(n+1):
        a=a+i**2
    print(a)
sum_square(5)   

#8
def prime(a,b):
    if 2>=a and 2<=b:
        print(2)
        a=3
    for i in range(a,b+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
                
        
prime(1,15)                
                
                 
#        
def prime(a,b):
    lower=min(a,b)
    upper=max(a,b)
    for num in range(lower,upper + 1):  
       if num > 1:  
           for i in range(2,num):  
               if (num % i) == 0:  
                   break  
           else:  
               print(num)          
    
prime(1,15)        
        
#9
def swap(l1,a,b):
    c=l1.index(a)
    d=l1.index(b)
    l1[c]=b
    l1[d]=a
    print(l1)
swap([1,2,3,4,5],1,4)    

#10
def rev(l1):
    l2=[]
    for i in range(len(l1)):
        l2.append(l1[len(l1)-(i+1)])
        
    print(l2)
rev([1,2,3,4,5]) 

#11
def rev(x):
    l2=[]
    for i in range(len(x)):
        l2.append(x[i])
        
    
    print(''.join(l2[0:len(l2)]))
rev("kankanjyoti")

#12
def rev(x):
    a=0
    for i in range (len(x)):
        if i==(len(x)-1):
            print(x[a:i+1])
        else:
        
            if(x[i]==" "):
                print(x[a:i])
                a=i
rev( "Indian Statistical Institute - Tezpur sample python code") 

           
            
    


        
        
        
        
        
        
        
    
    
    
        
    