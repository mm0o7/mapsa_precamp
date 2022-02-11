def even_finder() ->list:
    i = 1
    evens = []
    while i <= 100:
        if i % 2 == 0:
            evens.append(i)
        i += 1    
    return evens


if __name__ == "__main__":
    print (even_finder())        