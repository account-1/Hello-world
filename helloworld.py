'''
x=10
print("x=%d"%x)


x=20245
print("%10d"%x)


x="3"

#print("{1}, {0}".format(type(float(x)),x))
y=float(x)
print(y)

x=4.4
y=10
y=y+x
print(y ,  type(y))


nyDict = {1:2,3:4}
userDict = nyDict
print(userDict)

myTuple = (1,3,2,4,5,6,7,8,9)
userTuple=myTuple[-1:-5:-1]
print(userTuple)


char ='6'
print(float(char))
if 5 > 0 and 5<10 and 5>10:
        print(10)
else:
        print(20)


f = open("E:\\myTest.txt","r")
text = f.readline()
while text != '':
        print(text,end='')
        text = f.readline()
print("\n the contents pf the file has been completely printed")
f.close()




print("Hello World")


try:
        a = 10/0
except Exception as e:
        print("Error")

print("done")


s = r"Jalape\N{LATIN SMALL LETTER N WITH TILDE}o"
print(s)

a = b'Jalape\xc3\xb1o'
print(a)
 

a = [1,2,3,4]
b = ['w','e','r']
if a is b:
        print("a is b")
if a==b:
        print("a equal too b")
if type(a) is type(b):
        print("type same")



def my_function():
    param=[]
    param.append("thing")
    print(id(param))
    return (param)
#1st call
myList = []
print(id(myList))
myList = my_function() # returns ["thing"]
print(myList)
print(id(myList))

#2nd call

print(my_function())# returns ["thing", "thing"]

if 5 and None:
        print('yea')
else:
        print("No"


# Python code to demonstrate copy operations 
  
# importing "copy" for copy operations 
import copy 
  
# initializing list 1 
li1 = [1, 2, [3,5], 4] 
  
# using copy to shallow copy  
li2 = copy.copy(li1) 
  
# original elements of list 
print ("The original elements before shallow copying") 
for i in range(0,len(li1)): 
    print (li1[i],end=" ") 
  
print("\r") 
  
# adding and element to new list 
li2[3] = 7
  
# checking if change is reflected 
print ("The original elements after shallow copying") 
for i in range(0,len( li1)): 
    print (li1[i],end=" ")
print("\r") 

print ("The new elements after shallow copying") 
for i in range(0,len( li2)): 
    print (li2[i],end=" ") 


'''







