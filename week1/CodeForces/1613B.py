def absent_reminder(seq: list, len:int):
    pairs = []
    for i in range(len):
        for j in range(i+1, len):
            x = [seq[i], seq[j]]
            y = x[::-1]
            pairs.append(x)
            pairs.append(y)
    for x, y in pairs:
        if x != y and x % y not in seq:
            print(f'{x} {y}')

         
if __name__ == "__main__":
    testcase_number = int(input())
    for i in range(testcase_number):
        a = int(input())
        input_seq = [int(x) for x in input().split(" ")]
        absent_reminder(input_seq, a)   