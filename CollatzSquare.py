"""
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.
Let the user type in an integer and that keeps calling collatz() on that number 
until the function returns the value 1. (Amazingly enough, this sequence actually 
works for any integer—sooner or later, using this sequence, you’ll arrive at 1! 
"""
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
