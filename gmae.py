import random  # random.randint(1,3)

class Player:
    def __init__(self):
        self.HP=100
        self.MP=100
        self.STEMINA=0

    def normalAttack(self):
        self.attackPower = random.randint(5,10)
        self.STEMINA+=20
        return self.attackPower

    def smash(self):
        self.MP -= 20
        self.attackPower = random.randint(5, 10) * 3
        self.STEMINA += 10
        return self.attackPower

    def heal(self):
         self.MP -= 10
         self.HP += 40

    def imitation(self):
         self.MP += 30
         self.STEMINA+=10

    def maxPower(self):
            self.STEMINA -= 100
            self.attackPower = random.randint(5, 10)*6
            return self.attackPower




class Monster:
    def __init__(self):
        self.HP=500
        self.MP=200

    def normalAttack(self):
        self.attackPower = random.randint(10, 20)
        return self.attackPower

    def punch(self):

        self.MP-=40
        self.attackPower = random.randint(10, 20)*2
        return self.attackPower


    def rest(self):
        self.MP -= 20
        self.HP += 50

class GameManager:
    def __init__(self):
        self.Player= Player()
        self.Monster=Monster()

    def run(self):
        print("Player HP : %d Player MP : %d Player STEMINA : %s\n"%(self.Player.HP,self.Player.MP,self.Player.STEMINA))
        print("1.normal attack 2.smash 3.heal 4.imitation 5.maxPower\n")
        num1 = input("원하는 명령어를 입력하시오 :")

        while(1):
            if (num1 == 1):
                self.Monster.HP -= self.Player.attackPower
                break
            if (num == 2 and MP >= 20):
                self.Monster.HP -= self.Player.smash
                break
            if (num == 3 and MP >= 10):
                self.Player.heal
                break
            if (num == 2 and MP >= 30):
                self.Player.imitation
                break
            if (num == 2 and STEMINA >= 30):
                self.Player.maxPower
                break
            else:
                print("실행 할 수 없는 명령")





simulator = GameManager()
simulator.run(100)

print(simulator.result)