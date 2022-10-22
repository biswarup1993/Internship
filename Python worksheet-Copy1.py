#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Python worksheet

#Q1- Which of the following operators is used to calculate remainder in a division?
#Ans- C

#Q2- In python 2//3 is equal to
#Ans- 0

#Q3 In python, 6<<2 is equal to?
#Ans-24

#Q4- In python, 6&2 will give which of the following as output?
#Ans- 2

#Q5-In python, 6|2 will give which of the following as output?
#Ans-6

#Q6- What does the finally keyword denotes in python?
#Ans-C


#Q7- What does raise keyword is used for in python?
#Ans- A


#Q8- Which of the following is a common use case of yield keyword in python?
#Ans- C

#Q9- Which of the following are the valid variable names?
#Ans- _abc,abc2

#Q10- Which of the following are the keywords in python?
#Ans- yield, raise


# In[7]:


##Wap factorial of number

Factorial=1
num=10

if num<0:
    print("No factorial")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        Factorial= Factorial*i
        print("The factorial of",num,"is", Factorial)


# In[ ]:


##  Wap to find number is prime or composite number

num=19
count=0

if num>1:
    for i in range(1,num+1):
        if(num%i) == 0:
         count=count+1
    if count == 2:
     print("This is prime")
    else:
     print("This composite")


# In[2]:


#wap check whether a given string is palindrome or not

s=input("Enter word")

revstr=(s[::-1])

if revstr==s:
  print("Palindrome string")
else:
 print("Not palindrome string")


# In[40]:


## WAP program to get the third side of right-angled triangle from two given sides.

def pythagoras(opposite_side, adjacent_side, hypotenuse):
    if opposite_side == str("x"):
        return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
    elif adjacent_side == str("x"):
        return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
    elif hypotenuse == str("x"):
        return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    else:
        return ("You know the answer!")
    
print(pythagoras(3, 4, 'x')) 
print(pythagoras(3, 'x', 5)) 
print(pythagoras('x', 4, 5)) 
print(pythagoras(3, 4, 5))


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


## WAp to print the frequency of each of the characters present in a given string.

string=input ("Enter the string ")
freq=[None]*len(string)
for i in range (0, len(string)):
  freq[i]=1
  for j in range(i+1,len(string)):
    if(string[i]==string[j]):
      freq[i]=freq[i]+1 
      string=string[:j]+'0'+string[j+1:];
print ("Character and their frequency"); 
for i in range(0,len (freq)):
  if(string[i]!=' ' and string[i]!='0'):
    print(string[i]+"="+str(freq[i]))


# In[ ]:




