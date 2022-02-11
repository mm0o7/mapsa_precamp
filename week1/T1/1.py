import math


def butter_volum(radius: int) -> int:
    return (4/3)*(math.pi)*(pow(radius,3))

if __name__ == "__main__":
    r = 5.3
    b = butter_volum(r)
    print(b)
