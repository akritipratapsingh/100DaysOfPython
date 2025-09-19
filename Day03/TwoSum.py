nums = [2,4,3,5,6,7]
seen = {}
target = 9

def TwoSum():
    for i , num in enumerate(nums):
        compliment = target-num
        if compliment in seen:
            print([seen[compliment],i])
        seen[num]=i
    
TwoSum()