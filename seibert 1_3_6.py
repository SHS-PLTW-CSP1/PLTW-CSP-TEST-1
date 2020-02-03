import random
def roll_two_dice():
    die1 = random.choice([1,2,3,4,5,6])
    die2 = random.randint(1,6)
    print( die1)
    print ( die2)
    return die1 + die2
    
def pick_letter():
    return random.choice('seibert is awesome')
    print ('test')
    print('test2')