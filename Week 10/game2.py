import random
import time

# 두번째 게임은 '구구단을 외자!'입니다!
# 게임이 시작되면 무작위로 1-9 사이의 숫자가 두번 정해집니다.
# 두개의 숫자가 정해지면, "(숫자1), (숫자2)?" 형태로 출력이 됩니다. 예를 들어 숫자가 6과 4가 나왔다면, "육, 사?"가 출력되어야합니다
# 유저가 한번이라도 3초안에 대답을 못한다면, 게임을 집니다. (이동 -3) 리턴값은 0이 됩니다.
# 유저가 3번 연속으로 대답하는데 성공하면, 게임을 이깁니다. (이동 +3) 리턴값은 1이 됩니다.



def game2():
    
    number_strings = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

    trial = 0
    final_value = 0
    while trial < 3:
        options = [np.random.randint(1, 10)]
        options2 = [np.random.randint(1,10)]

        print(number_strings[options[0]-1]+',',number_strings[options2[0]-1]+"?")
        start = time.time()
        answer = input()
        end = time.time()
        time_e = end - start
        if time_e < 3:
            if int(answer) == options[0] * options2[0]:
                print("정답입니다!")
                trial +=1
            else:
                print("틀렸습니다!")
                trial = 0
        else:
            print("늦었습니다!")
            break

    if trial == 3:
        print("Win!")
        final_value = 1
    else:
        print("Lose!")

    return final_value