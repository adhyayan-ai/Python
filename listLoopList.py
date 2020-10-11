list_of_lists = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4 , 5],
    [4, 5, 6],
    [5, 6, 7]
]

for x in list_of_lists:
    for y in x:
        print(y, end="")
    print()