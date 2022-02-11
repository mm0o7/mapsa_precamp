def make_ap(seq: list) ->list:
    d1 = seq[1] - seq[0]
    d2 = seq[2] - seq[1]
    d3 = seq[2] - seq[0]
    if d1 == d2 == d3 // 2:
        return True
    elif (abs(d3) % seq[1] == 0 and abs(d3) // seq[1] != 1) or (abs(d2) % seq[0] == 0 and abs(d2) // seq[0] != 1) or (abs(d1) % seq[2] == 0 and abs(d1) // seq[2] != 1):
        return True
    else: 
        return False

def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        input_seq = [int(x) for x in input().split(" ")]
        if make_ap(input_seq):
            print("YES")
        else:
            print("NO")    
        
if __name__ == "__main__":
    main()              