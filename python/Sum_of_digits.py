number = input("Enter Number: ") #string is a list of char 
sum = 10

# range(0,3) = [0,1,2]
for digit in number:
    sum = sum + int(digit)
print(sum)

# using int
number = int(input("Enter Number: "))
sum = 0
while(number>0):
    sum = sum + (number % 10) #taking last digit
    number = number // 10 #removing laswt digit
# for digit in number:
#     sum = sum + digit
print(sum)