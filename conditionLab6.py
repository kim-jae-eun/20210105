import random
score = random.randint(0, 100)
if score>=90:
    a='A'
elif 80<=score<90:
    a='B'
elif 70 <= score < 80:
    a='C'
elif 60 <= score < 70:
    a='D'
else:
    a='F'
print(str(score)+'점은 '+a+'등급입니다.')
