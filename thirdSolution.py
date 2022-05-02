# This excersice is about to do a loop to find the text string FIZZBUZ in remainder of 3 and 5 upto 100

# Solution #3
for i in range(1, 101):
    findOut = ""
    if i % 3 == 0:
        findOut = "Fizz"
    if i % 5 == 0:
        findOut += "Buzz"
    print(findOut or i)
