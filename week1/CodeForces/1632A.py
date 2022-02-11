def get_string() ->str:
    length = int(input())
    binary_string = input()
    if len(binary_string) == length:
        return binary_string       
    
def check_algorithm(string: str) ->bool:
    if string.count("0") <= 1 and string.count("1") <= 1:
        return True
    else:
        return False
    
def main():
    testcase_number = int(input())
    for i in range(testcase_number):
        ans = check_algorithm(get_string())
        if ans == True:
            print("YES")
        else:
            print("NO")        
            
if __name__ == "__main__":
    main()            