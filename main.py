def getinput():
   v1 = int(input("Please enter an integer: "))
   v2 = int(input("Please enter a second integer: "))


def getsum(v1, v2):
    total = v1 + v2


def printval(v1, v2, total):
    print(v1, v2, total)


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
