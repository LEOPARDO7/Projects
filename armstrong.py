
num = int(input("enter the number:"))
temp = num
sum = 0
while(num>0):
    a = num % 10
    num = num // 10
    sum = sum + (a*a*a)
print(sum)

if(sum == temp):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
