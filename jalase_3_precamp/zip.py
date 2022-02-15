def zip(*iterator: list) ->tuple:
    len_min_iterator = len(iterator[0])
    for i in iterator:
        if len(i) < len_min_iterator:
            len_min_iterator = len(i)
    i = 0        
    while i < len_min_iterator:
        temp = []
        for j in iterator:
            temp.append(j[i])
        yield tuple(temp)
        i += 1
        
