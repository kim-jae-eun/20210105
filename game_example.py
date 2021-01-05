a=int(input("1부터 32까지 중에서 아무 숫자나 생각해 보세요. 생각하셨으면 여기에 입력해주세요: "))
print("\n")
print('흠...')
print("\n")
if a%2==0:
    print('당신의 수는 짝수였네요?')
elif a % 2 == 1:
    print('당신의 수는 홀수였네요?')
else:
    print('뭐하냐')

import random
c = random.randint(1, 32)
print("\n")
b=input('어때요, 저와 게임을 해보시겠어요? 대답은 네/아니오 로 해주세요. ')
if b=="네":
    if a<c:
        print("\n",'좋아요. 제가 생각한 숫자를 맞혀보세요. 제 수는 당신의 수보다 큽니다.')
        d=int(input("다시 추측해주세요: "))
        if d<c:
            print("\n",'제 수는 당신의 수보다 큽니다.')
            e=int(input("다시 추측해주세요. "))
            if e<c:
                print("\n",'제 수는 당신의 수보다 큽니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

            elif e>c:
                print("\n",'제 수는 당신의 수보다 작습니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
            else:
                print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
        elif d>c:
            print("\n",'제 수는 당신의 수보다 작습니다.')
            e = int(input("다시 추측해주세요. "))
            if e<c:
                print("\n",'제 수는 당신의 수보다 큽니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

            elif e>c:
                print("\n",'제 수는 당신의 수보다 작습니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
            else:
                print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
        else:
            print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

    elif a>c:
        print("\n",'좋아요. 제가 생각한 숫자를 맞혀보세요. 제 수는 당신의 수보다 작습니다.')
        d=int(input("다시 추측해주세요: "))
        if d<c:
            print("\n",'제 수는 당신의 수보다 큽니다.')
            e=int(input("다시 추측해주세요. "))
            if e<c:
                print("\n",'제 수는 당신의 수보다 큽니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

            elif e>c:
                print("\n",'제 수는 당신의 수보다 작습니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
            else:
                print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
        elif d>c:
            print("\n",'제 수는 당신의 수보다 작습니다.')
            e = int(input("다시 추측해주세요. "))
            if e<c:
                print("\n",'제 수는 당신의 수보다 큽니다.')
                f = int(input("다시 추측해주세요. "))
                if f<c or f>c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

            elif e>c:
                print("\n",'제 수는 당신의 수보다 작습니다.')
                f = int(input("다시 추측해주세요. "))
                if f < c or f > c:
                    print("\n",'틀렸습니다. 실패입니다! 다시 도전하세요.')
                else:
                    print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
            else:
                print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
        else:
            print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')

    else:
        print("\n",'좋아요! 제가 생각한 숫자를 맞추셨어요!')
    print("\n", "\n", "정답은", str(c), "였습니다!")
else:
    print("\n",'유감입니다. 다음에 만나요.')
