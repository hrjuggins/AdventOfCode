f = open('./sample', "r")

passPowers = []

for line in f:
    rolls = line.split(':')[1].split(';')
    totals = {
    'red': 0,
    'green': 0,
    'blue': 0,
    }
    for roll in rolls:
        roll = roll.split(',')
        for r in roll:
            r = r.strip().split(' ')
            colour = r[1]
            value = int(r[0])
            if totals[colour] < value:
                totals[colour] = value

    passPowers.append(totals['red'] * totals['green'] * totals['blue'])

print(sum(passPowers))


            
