f = open('./sample', "r")

sum = 0

wordNums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for x in f:
    nums = []
    total = 0
    current = ''

    for i in range(len(x)):
        current += x[i]
        for w in wordNums:
            if w in current:
                nums.append(str(wordNums.index(w) + 1))
                current = x[i]
        if x[i].isdigit():
            nums.append(x[i])

    if (len(nums) == 1):
        total = nums[0] + nums[0]
    else: 
        total = nums[0] + nums[len(nums) - 1]

    sum += int(total)

print(sum)
        
