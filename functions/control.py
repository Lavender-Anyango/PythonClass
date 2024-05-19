def print_numbers(n):
    numbers = range(n)

    for number in numbers:
        print(number)

def print_even_numbers(n):
    numbers = range(n)

    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print(f"{number} is odd")


def check_divisibility(n):
    numbers = range(n)

    for number in numbers:
        if number % 2 == 0:
            print(f'{number} is divisible by 2')
        elif number % 3 == 0:
            print(f'{number} is divisible by 3')
        elif number % 5 == 0:
            print(f'{number} is divisible by 5')
        elif number % 7 == 0:
            print(f'{number} is divisible by 7')
        else:
            print(f'{number} is not divisible by 2, 3, 5, and  7')


def countdown(n):
    while n > 0:
        print(n)
        n -=1

def countdown_five(n):
    while n > 0:
        print(n)
        if n == 5:
            break
        n -= 1

def divisible_by_seven(n):
    x = 1
    while x <= n:
        x+= 1

        if x % 7 != 0:
            continue
        print(x)


# Q1:
def fizzbuzz(n):
    numbers = range(n)

    for number in numbers:
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print("FizzBuzz")

# Q2:
def even_numbers():
    num = 0
    while num <= 50:
        num +=1
        if num % 2!= 0:
            continue
        print(num)


counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)