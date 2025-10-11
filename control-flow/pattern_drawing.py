size = 0
while size <= 0:
   size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    for j in range(1, size + 1):
        print("*", end= "")
    i += 1
    print()