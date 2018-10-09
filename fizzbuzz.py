for num in range(1,21):
    string = ""
    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string += str(num)
    print (string)

for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)