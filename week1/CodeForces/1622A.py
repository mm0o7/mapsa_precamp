def construct_rec(seq: list) ->bool:
    if (seq[0] == seq[1] and seq[2] % 2 == 0) or (seq[0] == seq[2] and seq[1] % 2 == 0) or (seq[1] == seq[2] and seq[0] % 2 == 0) or seq[0] + seq[1] == seq[2] or seq[0] + seq[2] == seq[1] or seq[1] + seq[2] == seq[0]:
        return True
    else:
        return False

def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        input_seq = [int(x) for x in input().split(" ")]
        if construct_rec(input_seq):
            print("YES")
        else:
            print("NO")    
        
if __name__ == "__main__":
    main()              