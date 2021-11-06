largestnum = 0
for i in range (4):
    userinput = input("Number please...")
    usernum = int(userinput)
    if (usernum > largestnum):
        largestnum = usernum
print(str(largestnum))
