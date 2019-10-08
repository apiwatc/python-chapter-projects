import time
from decimal import Decimal


# check if a number is a prime number
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        else:  # 2 and 3 are prime number
            return True
    else:
        # num % 2 to n-1, if == 0 then not prime number
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# print list of prime numbers
def prime_eratosthenes(num):
    # list of number from 2 to num
    prime = [i for i in range(2, num+1)]
    for i in range(2, num+1):
        # 2 -> 4,6,8...num
        # 3 -> 6,9,12...num
        # so on
        for j in range(i+i, num+1, i):
            try:
                prime.remove(j)
            except ValueError:
                # if number is already removed, it will raise error
                continue
    return prime


if __name__ == "__main__":
    s2 = time.time()
    print(is_prime(100))
    e2 = time.time()
    print(Decimal(e2)-Decimal(s2))

    s1 = time.time()
    print(prime_eratosthenes(100))
    e1 = time.time()
    print(Decimal(e1)-Decimal(s1))
