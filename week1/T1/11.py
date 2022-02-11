import random


def make_num():
    num = random.randint(1, 20)
    return num

def chance_game(num: int) ->bool:
    for i in range(1, 6):
        number = int(input(f'enter your {i} chance: '))
        if number == num:
            return True
            break
    return False

def output(ans: bool, num: int):
    if ans == True:
        print("You Win")
    else:
        print(f'Game Over {num}')     
        

if __name__ == "__main__":
    random_number = make_num()
    output(chance_game(random_number), random_number)