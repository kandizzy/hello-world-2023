global x
x = 0

def increaseCount(x):
    cat = 5
    while x < 10:
        cat = cat + 1

        if cat > 5:
            increaseCount()
            print(x)
            global x
            x += 1

while x < 10:
    increaseCount()
    print(x)



# print("range 1 to 10")

# def countNumber(theNumber):
#     print("count: " + str(theNumber))

# numberOfTimes = 10
# for value in range(1,numberOfTimes):
#     countNumber(value)


# items = ["item1", "item2", "item3"]
# print("item in items")
# for x in items:
#     print(x)


# numberOfDots = 360
# for x in range(0,numberOfDots):
#     #print(items[x])
#     moveDotToPosition(x)

# for x in range(len(items)):
#     print(items[x])


# print("using the length of the array")
# for x in range(len(items)):
#     print("x is" + str(x))
#     print("item is " + items[x])
