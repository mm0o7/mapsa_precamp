def my_multiple(x: int,y: int) ->int:
    i = 1
    ans = 0
    while i <= y:
        ans += x
        i += 1
    return ans


if __name__ == "__main__":
    x = int(input("enter the x: "))
    y = int(input("enter the y: "))
    print (my_multiple(x,y))         