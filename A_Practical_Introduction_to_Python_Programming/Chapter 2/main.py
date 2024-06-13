for i in range(100):
    print("Iron Man")

for i in range(100):
    print("CapitanAmerica",end=' ')

print()
for i in range(1,101):
     print(i,"Black Panther")

for i in range(1,21):
    print(i,'---',i**i)

for i in range(5,90,3):
    print(i+3,end=',')

print()
for i in range(10):
    print("A",end='')
for i in range(7):
    print("B",end='')
for i in range(4):
    print("CD",end='')
for i in range(5):
    print("F",end='')
print('G')
print()

name = input("Enter your name: ")
times = int(input("how many times to print name: "))
for i in range(times):
    print(name)


print()
wide = int(input(" how wide the box should be: "))
high = int(input(" how high the box should be: "))
for i in range(high):
    print('*'*wide)
print()

hieght = int(input("How high shoudl be the trianglr: "))
for i in range(1,hieght):
    print(i*'*')

hieght = int(input("How high shoudl be the trianglr: "))
for i in range(hieght,1,-1):
    print(i*'*')

wide1 = int(input(" how wide the box should be: "))
high1 = int(input(" how high the box should be: "))
s=" "
print('*'*wide1)
for i in range(high1-2):
    print('*',s*(wide1-2-2),'*')
print('*' * wide1)
