def min_max(numbers: list) ->list:
    min,max = numbers[0],numbers[0]
    for num in numbers[1:]:
        if num <= min:
            min = num
        if num >= max:
            max = num
    return min,max

def get_nums():
    nums = []
    for i in range (3):
        num = int(input("inter a number : "))
        nums.append(num)
    return nums


if __name__ == "__main__":
    numbers = get_nums()
    min,max = min_max(numbers)
    print(f'max is:{max}')
    print(f'min is:{min}')                        