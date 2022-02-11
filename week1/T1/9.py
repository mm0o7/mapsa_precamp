def len_hei_getter():
    length = int(input("length: "))
    height = int(input("height: "))
    return length,height

def parall_draw(l: int, h: int):
    for i in range(h, 0, -1):
        for j in range(0, i):
            print(end=" ")
        if i == h or i == 1:
            print("*"*l)
        else:
            print("*", " "*(l-3), "*")    
             

if __name__ == "__main__":
    length,heigth = len_hei_getter()
    parall_draw(length, heigth)                   