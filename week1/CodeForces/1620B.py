def triangle_on_rectangle():
    w, h = map(int, input().split())
    ans = 0
    for i in range(4):
        a = [int(x) for x in input().split()][1:]
        t = a[-1] - a[0]
        if i < 2:
            ans = max(ans , t*h)
        else:
            ans = max(ans, t*w)    
    return ans
    
def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        ans = triangle_on_rectangle()
        print(ans)
       
if __name__ == "__main__":
    main()         