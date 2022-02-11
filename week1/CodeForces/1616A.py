def diversity(seq: list) ->int:
    extended_list = list(map(abs, seq))
    converted_dic = {}
    ans = 0
    for i in range(len(extended_list)):
        converted_dic[extended_list[i]] = extended_list.count(extended_list[i])
    for key, value in converted_dic.items():
        if key == 0 or value == 1:
            ans += 1
        else:
            ans += 2
    return ans        
    

    
def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        a = int(input())
        input_seq = [int(x) for x in input().split(" ")]
        ans = diversity(input_seq)
        print (ans)

if __name__ == "__main__":
    main()                 