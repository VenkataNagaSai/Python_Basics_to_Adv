###############################################
#
# Practical Loop Examples
#
# Using loops for complex logic like Prime Number Generation, Pascal Triangle, and Bubble Sort.
#
############################################### 

###############################################
#
# Example 1: Prime Number Generation
#
############################################### 

num = 10
count = 0

for val in range(2, num, 1):
    prime_f = 1
    for div in range(2, int(val/2) + 1):
        if val % div == 0:
            prime_f = 0
            break
    if prime_f == 1:
        print("Prime number is", val)
        count += 1
print("Total prime numbers:", count)

###############################################
#
# Example 2: Pascal Triangle Printing
#
############################################### 

rows = 5
for i in range(rows):
    gap = rows - 1 - i
    for y in range(gap):
        print(" ", end="")
    for z in range(2 * i + 1):
        print("*", end="")
    print()

###############################################
#
# Example 3: Bubble Sort
#
############################################### 

numlist = [25, 10, 5, 30, 15]
count = len(numlist)
swap_f = 1
total_swaps = 0

while (swap_f == 1):
    swap_f = 0
    for i in range(count - 1):
        if numlist[i] > numlist[i + 1]:
            total_swaps += 1
            swap_f = 1
            # Swapping values
            temp = numlist[i]
            numlist[i] = numlist[i + 1]
            numlist[i + 1] = temp

print("Sorted list after", total_swaps, "swaps:", numlist)
