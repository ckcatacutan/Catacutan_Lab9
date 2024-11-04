rows = int(input("Enter the number of rows: "))
number = 1
for i in range(1, rows + 1):
    for j in range(i):
        if number > 15:
            break
        print(number, end=" ")
        number += 1
    print()  
    if number > 15:
        break