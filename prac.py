""" import turtle

t=turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.shape("turtle")

t.circle(100) """

""" import random
time = random.randint(1,24)
time = random.randrange(24) +1

print(time)"""

""" for i in range(5):
    print("welcome")
for i in [1,2,3,4,5]:
    print(i)
for i in range(1,6,2):
    print("again")"""

""" response ="아니"
while response == "아니":
    response = input("엄마, 밥 다 됐어?")
print("먹자")"""


n = int(input("값을 입력하시오 :"))
sum=1

while(1):
    sum*=n
    if(n==1):
        break
    n-=1

print(sum)

n = int(input("값을 입력하시오 :"))
fact=1
for i in range(1,n+1):
    fact=fact*1
print(fact)


