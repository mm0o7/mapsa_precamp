from numpy import char, character


def first_char(massage: str) ->character:
    return massage[0]
def k_char(massage: str, k: int) ->character:
    return massage[k+1]
def seprate_first_last(massage: str) ->list[str]:
    return massage.split(" ")
def speacial_print(massage: str):
    print (massage[: 13: 2])
def check_m(massage: str) ->bool:
    for i in massage:
        if i == "m":
            return True
            break
    return False


if __name__ == "__main__":
    massage = "Babak Khorramdin"
    print (first_char(massage))
    k = int(input("enter the k number: "))
    print (k_char(massage, k))
    print (seprate_first_last(massage))
    print (speacial_print(massage))
    print (check_m(massage))