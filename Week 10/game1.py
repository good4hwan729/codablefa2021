import random


# 첫번째 게임은 UP or DOWN 입니다!
# 1부터 50 무작위의 숫자가 정해집니다.
# 여러분은 총 5번의 기회를 이용하여 숫자를 맞추셔야 합니다
# 정해진 숫자보다 높은 숫자를 입력할 경우 DOWN이 출력되며, 낮을 경우 UP이 출력됩니다
# 모든 기회안에 못맞추시면 게임을 지고, -3칸 이동하시게 됩니다. 이 때 리턴값은 0이 됩니다
# 이기시면 +3 칸 이동하시게 됩니다. 이 때 리턴값은 1이 됩니다


def game1():
    
    number = random.randint(1, 51)
    
    life = 5
    
    while(life > 0):
        x = input("숫자를 입력하세요: ")
        if int(x) > number:
            print("DOWN")
            life -= 1
        elif int(x) < number:
            print("UP")
            life -= 1
        else:
            print("CORRECT")
            break
           
    if life > 0:
        return 1
    else:
        return 0
    
game1()