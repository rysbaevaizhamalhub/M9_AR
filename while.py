# Aizhamal Rysbaeva
# Nov 19, 2024

# Problem
# Write an infinite loop that prints “Infinite”.
# An infinite loop never ends.
# The condition is always true.
# After you prove to yourself that this works, comment out the code that produces the infinite loop.
# To break a loop in progress you should be able to do ctrl-C or command-C (depending on your platform).

# i = 1
# while "space":
#     print("Infinite")

print(1 == True)


# Problem 2
#  Create a list called L that starts with the numbers 57 and 83 in it.
# Then build a while loop, starting with a counter assigned to the value 0.
#  On each iteration, the loop should append the current value of a counter variable to the list
# and then increase the counter by 1.
# The while loop should stop once the counter variable is greater than 10.
#  Finish by printing a statement that tells us a) how many elements are in the list,
# and b) what the third element in the list is.

L = [57, 83]
i = 0
while i <= 10:
    L.append(i)
    i += 1

print(f"the list has {len(L)} elements")
print(f"the third element of the list is {L[2]}")

# Problem 3
# Using a while loop,
# ask the user to enter a number.
# Append each entered number to a list and add them together.
# Continue asking for a num until the sum of list of numbers is greater than 100.

numbers = []
sum = 0

while sum <= 100:
    number = int(input("enter a number: "))
    numbers.append(number)
    sum += number

print("total sum is now gteater than 100")
print("numbers entered:", numbers)
print("final sum:", sum)
