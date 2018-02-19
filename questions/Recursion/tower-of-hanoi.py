""" Author - Sidharth Satapathy """

# Tower of Hanoi

# Move from tower to helper
# Move last to end pole
# do again for the stack in helper

def towerOfHanoi(disks,start,end,helper):
    if disks >= 1:
        towerOfHanoi(disks-1,start,helper,end)
        print (f"Moving from {start} to {end}")
        towerOfHanoi(disks-1,helper,end,start)

towerOfHanoi(3,"A","B","C")        
