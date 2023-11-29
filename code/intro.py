# List definition
my_list_A = [1, 2, 3, 4, 5, 6]
my_list_B = [1, 2, 5, 4, 8, 6]

# Compare lists
print("Comparing lists")
print("Pairs of unequal elements are: ")
for i in range(len(my_list_A)):
    if my_list_A[i] != my_list_B[i]:
        print(my_list_A[i], my_list_B[i])
print("Done")