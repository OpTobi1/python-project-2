#Assignment: HW2 Author: Liav Lugasi, ID: 213007271

#Question 1


def count_even_and_4(num):
    count = 0
    num = abs(num)

    while num > 0:
        digit = num % 10
        if digit % 2 == 0 and digit > 4:
            count += 1
        num //= 10

    return count


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))


count1 = count_even_and_4(num1)
count2 = count_even_and_4(num2)


if count1 == count2:
    print("YES")
else:
    print("NO")



#Question 2


a = int (input("enter the first number: "))
b = int (input("enter the second number: "))
c = int (input("enter a number between 0 to 9: "))

while c < 0 or c > 9:
    print ("wrong number")
    c = int(input("enter a number between 0 to 9: "))

c = str(abs(c))

for num in range(a, b + 1):
        if c not in str(num):
            print(num)


#Question 3

def string_length(list, x):
    for str in list:
        if len(str) == x:
            return 1
    return 0






