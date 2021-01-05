import random
oper_num = random.randint(1, 10)
print(oper_num)
if oper_num==1 or oper_num==6:
    a=300+50
if oper_num == 2 or oper_num == 7:
    a = 300 - 50
if oper_num == 3 or oper_num == 8:
    a = 300 * 50
if oper_num==4 or oper_num==9:
    a=300/50
if oper_num==5 or oper_num==10:
    a=300%50
print('결과값 :',str(a))