count = 0
while count < 5:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(number * 2)
    count += 1
   
    while True:
        print("This loop will never end.")