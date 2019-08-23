def collatez(number):
    while number > 1:
        print(number)
        if number % 2 == 0:
            number = (number // 2)
        else:
            number = (3 * number + 1)
    print(number)


while True:
    try:
        num = int(input("Enter number: "))
        collatez(num)
        break
    except ValueError:
        print("Please Enter a Number")
