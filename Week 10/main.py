from board.py import board
from dice.py import roll_dice
from game1.py import game1
from game2.py import game2
from game3.py import game3
import random


# 게임은 다음과 같이 이루어집니다!

# 1. 주사위를 굴립니다
# 2. 주사위에 나오는 숫자만큼 말을 이동합니다.
# 3. 보드에 나오는 대로 (이동, 게임)을 합니다.
# 4. 이동 칸이 나오면 보드에 나오는 숫자만큼 이동을 합니다.
# 5. 게임 칸이 나오면 3개의 게임 중 무작위로 하나를 합니다. 게임의 결과에 따라 말이 이동하게 됩니다.
# 6. 말이 도착 지점에 도착하면 게임이 종료됩니다.

# 전체적인 게임을 돌아가게 만드는 함수입니다.
# 게임의 규칙에 알맞게 함수를 집어 넣으십시요!
def play_game():
    
    # 보드를 만들어야 함
    
    while(1):
        player = 0
        # 주사위를 돌린다
        
        
        # 말이 그만큼 움직여야 한다
        
        
        
        # 나오는 경우1 : 이동칸
        # 말이 다시 이동
        
        # 나오는 경우2 : 게임칸
        gametype = random.randint(1,4)
        if gametype == 1:
            result = game1()
        elif gametype == 2:
            result = game2()
        else
            result = game3()
            
        if result == 0:
            player -= 3
        else:
            player += 3
            
            
        # 말이 끝에 도달?
        if player == 39:
            break

# 메인 함수
# 안건드리셔도 됩니다.
if __name__ == '__main__':
    play_game()
    