def fruits(fruits: tuple) ->dict:
    ans = dict()
    good_fruits = []
    for x in fruits:
        if (x['shape'] == 'sphere') and (300 <= x['mass'] <= 600) and (100 <= x['volume'] <= 500):
            good_fruits.append(x['name'])
    for x in good_fruits:
        counter = good_fruits.count(x)
        ans.update({x: counter})
        for i in range(len(good_fruits)-1):
            if good_fruits[i] == x:
                good_fruits[i] == ""
    return ans   


output = fruits((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})) 
print (output)          