def odd_even(number: int) -> str:
    if number % 2 == 0:
        return ("even")
    else:
        return ("odd")
    
    
if __name__ == "__main__":
    num = int(input("type your number: "))
    print (odd_even(num))     