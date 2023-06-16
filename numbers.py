num = 0
gnum = 0

user_num = float(input("Enter your number: "))
while user_num > 0:
    gnum += user_num
    user_num = float(input("Enter your number: "))
    if user_num < 0:
        continue
    
print(gnum)
