# This excersice is about to do a loop to find the text string FIZZBUZ in remainder of 3 and 5 upto 100

# Solution #4

for i in range(1, 101):
    print("Fizz"*(i % 3 < 1)+(i % 5 < 1)*"Buzz" or i)
