for i in range(5):
    print(i)
    
for j in range(15):
    print(j*2)
        
for num in range(8):
    print("hello"*num)
            
for i in range(2,10):
    print(i)

x = 6
while x < 15:
    print(x)
    x+=1

x = 4

while x >= 0:
    print ("Hello"*x)
    x-=1


num = 5
while num >= 1:
    print("*"*num)
    num-=2
    
x = 5
while x < 15:
    if x % 2 == 0:
        print("EVEN",x)
        break
print(x)
x+=1

x=5
while x < 15:
    if x % 2 == 0:
        print("Even nmber found")
        break
    print(x)
    x += 2
else:
    print("All numbers were odd")
    
for i in range(3):
    for j in range(2):
        print(i,j)
        
x = 5
if x > 9:
    print("Hello, World!")

x = 10
if x > 9:
    print("Hello, World!")

x = 5
if x > 9:
    print("Hello!")
print("End")

x = 15

if x > 9:
    print("Hello!")
else:
    print("Bye!")
    
x = 5

if x > 9:
    print("Hello!")
elif x <15:
    print("It's great to see you")
else:
    print ("bye")
print("END")

my_list = [1,2,3,4,5]
for elem in my_list:
    if elem % 2 == 0:
        print("Even", elem)
        print("Break")
        break
else:
    print("Odd:", elem)

my_list = [5,6,7,8]
for i, elem in enumerate(my_list):
    print(i,elem)