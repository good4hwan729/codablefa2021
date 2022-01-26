import random


# 주사위를 굴리는 함수입니다.
# 두 개의 주사위를 굴리십시요!
# 나오는 주사위의 값을 출력(print)도 해주십시요!
def roll_dice():
    
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    dice = d1 + d2
    while d1 == d2:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        dice += d1
        dice += d2
    return dice