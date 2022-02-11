def get_string() ->str:
    binary_string = input()
    return binary_string       

def minority(string: str) ->int:
    zeros = string.count("0")
    ones = string.count("1")
    if zeros == ones:
        return len(string)//2-1
    else:
        if zeros > ones:
            return ones
        else:
            return zeros
        
def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        print(minority(get_string()))
 
if __name__ == "__main__":
    main()             