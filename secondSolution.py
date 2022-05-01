# This excersice is about to do a loop to find the text string FIZZBUZ in remainder of 3 and 5 upto 100

# Solution #2

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
