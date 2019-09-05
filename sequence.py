n = int(input("Enter the length of the sequence: ")) # Do not change this line
# 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
first_int = 1
second_int = 2
third_int = 3
sum = 0


for all in range(0, n):
    while sum <= n:
        if sum == n:
            break
        print(first_int)
        sum += 1
        if sum == n:
            break        
        first_int = first_int + second_int + third_int
        print(second_int)
        sum += 1
        if sum == n:
            break
        second_int = second_int + third_int + first_int
        print(third_int)
        sum += 1

        third_int = third_int + first_int + second_int
        
    


