import random


# 세번째 게임은 '참참참!' 입니다!
# 게임이 시작되면 코드가 오른쪽, 왼쪽, 가운데 중 하나를 무작위로 선택하게 됩니다.
# 동시에 유저도 '오른쪽', '왼쪽', '가운데' 중 하나를 입력해야 합니다.
# 만약 두번 연속 코드가 정한 값을 피하시면 게임을 이깁니다 (+3칸 이동) 리턴값은 1이 됩니다.
# 만약 한번이라도 코드가 정한 값과 동일하다면 게임을 집니다 (-3칸 이동) 리턴값은 0이 됩니다.



def game3():
    
    """
    왼쪽 = 0
    가운데 = 1
    오른쪽 = 2
    """
    
    print("참참참 게임!")
    print("두번 연속 피하시면 게임을 이깁니다")
    
    
    ### Try 1
    print("Try 1")
    print("")
    p1 = -1
    while (1):
        x = int(input("왼쪽: 0, 가운데: 1, 오른쪽: 2 중 선택하시오"))
        
        # Checkes whether input is valid
        if (x != 0 and x != 1 and x != 2):
            print("Error: Invalid input")
            print("왼쪽, 가운데, 오른쪽 중에서 다시 골라주세요")
        else:
            p1 = x
            break
    
    print("")
    print("")
    print("참")
    time.sleep(1)
    print("참")
    time.sleep(1)
    print("참!")
    
    
    # Game Checker
    c1 = random.randint(0, 2)
    
    cc1 = ""
    if (c1 == 0):
        cc1 = "왼쪽"
    elif (c1 == 1):
        cc1 = "가운데"
    else:
        cc1 = "오른쪽"
        
    pp1 = ""
    if (p1 == 0):
        pp1 = "왼쪽"
    elif (p1 == 1):
        pp1 = "가운데"
    else:
        pp1 = "오른쪽"
    
    print("")
    print("")
    print("술래: " + cc1 + "   당신: " + pp1)
    print("")
    print("")
    
    if c1 == p1:
        print("패배하셨습니다")
        return 0
    
    time.sleep(0.5)
    
    
    ### Try 2
    print("Try 2")
    print("")
    p2 = -1
    while (1):
        x = int(input("왼쪽: 0, 가운데: 1, 오른쪽: 2 중 선택하시오"))
        
        # Checkes whether input is valid
        if (x != 0 and x != 1 and x != 2):
            print("Error: Invalid input")
            print("왼쪽, 가운데, 오른쪽 중에서 다시 골라주세요")
        else:
            p2 = x
            break
    
    print("")
    print("")
    print("참")
    time.sleep(1)
    print("참")
    time.sleep(1)
    print("참!")
    
    
    # Game Checker
    c2 = random.randint(0, 2)
    
    cc2 = ""
    if (c2 == 0):
        cc2 = "왼쪽"
    elif (c2 == 1):
        cc2 = "가운데"
    else:
        cc2 = "오른쪽"
        
    pp2 = ""
    if (p2 == 0):
        pp2 = "왼쪽"
    elif (p2 == 1):
        pp2 = "가운데"
    else:
        pp2 = "오른쪽"
    
    print("")
    print("")
    print("술래: " + cc2 + "   당신: " + pp2)
    print("")
    print("")
    
    if c2 == p2:
        print("패배하셨습니다")
        return 0
    
    time.sleep(0.5)
    print("")
    print("")
    print("축하합니다! 이기셨습니다")
    return 1