num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 1
for count in range(0, 1000):
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
    if num_int < 0:
        break

print("The maximum is", max_int)    # Do not change this line