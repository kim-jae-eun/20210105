import random
grade = random.randint(1, 6)
if not grade==4 and not grade==5 and not grade==6:
    print(str(grade)+'학년은 저학년입니다.')
else:
    print(str(grade) + '학년은 고학년입니다.')