import random

# 게임 보드를 이루는 부분입니다.
# 보드(Board)는 하나의 Class입니다.
class Board():
    
    # Board의 특성으로는 보드 자체 [List]와 말의 위치 [Int]를 가져야 합니다.
    # init 했을 때 보드는 40칸 중 19칸을 이동칸, 19칸을 게임 칸으로 무작위로 채워주시기 바랍니다. (처음과 끝은 각각 '시작'과 '끝' 칸입니다)
    # init 했을 때 말의 위치는 보드의 첫칸에 배치 해주시기 바랍니다.
    # 이동칸은 -3 부터 3까지의 무작위 숫자이며 (0은 제외), 해당 칸에 도착할 경우 나오는 숫자만큼 이동을 하시면 됩니다.
    # 게임칸은 'GAME'이라는 string으로 채우시면 되며, 도착할 경우 메인 함수에서 무작위 게임 하나를 할 것입니다.
    def __init__(self):
        self.gameboard = [0]*40
        self.gameboard[0] = 'Start'
        self.gameboard[39] = 'End'
        moveindex = random.sample(range(1, 38), 19)
        move = [-3, -2, -1, 1, 2, 3]
        for i in range(1, 39):
            if(i in moveindex):
                self.gameboard[i] = move[random.randint(0, 5)]
            else: 
                self.gameboard[i] = 'GAME'      
        
        self.piece = 0
    
    # Board의 메소드 함수 show_board는 현재 보드의 상태와 말의 현재 위치를 출력(print)해서 보여주어야 합니다.
    def show_board(self):
        self.gameboard[self.piece] = 'Player'
        print("현재 보드 상태: ")
        print(self.gameboard)
        print("말의 현재 위치: " + str(self.piece))