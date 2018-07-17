import random  # random.randint(1,3)


class Player:


    def __init__(self, id):
        self.HP = 100
        self.MP = 100
        self.STEMINA = 0
        self.attackPower = 0

    def normalAttack(self):
        self.attackPower = random.randint(5, 10)
        self.STEMINA += 20
        return self.attackPower

    def smash(self):
        self.MP -= 20
        self.attackPower = random.randint(5, 10) * 3
        self.STEMINA += 10
        return self.attackPower

    def heal(self):
        self.MP -= 10
        self.HP += 40
        self.STEMINA += 10

    def imitation(self):
        self.MP += 30
        self.STEMINA += 10

    def maxPower(self):
        self.STEMINA -= 100
        self.attackPower = random.randint(5, 10) * 6
        return self.attackPower


class Monster:
    def __init__(self):
        self.HP = 500
        self.MP = 200
        self.attackPower = 0

    def normalAttack(self):
        self.attackPower = random.randint(10, 20)
        return self.attackPower

    def punch(self):
        self.MP -= 40
        self.attackPower = random.randint(10, 20) * 2
        return self.attackPower

    def rest(self):
        self.MP -= 20
        self.HP += 50


class GameManager:
    def __init__(self):
        self.n = random.randint(0,2)

        self.Players = []
        for i in range(self.n):
            self.Players.append(Player(i))

        self.Monster = Monster()

    def run(self):

        while (1):

            for i, j in self.n, self.Players:
                if
                print("Player %d HP : %d Player %d MP : %d Player %d STEMINA : %d\n" % (i+1, self.Players[i].HP, i+1, self.Players[i].MP, i+1, self.Players[i].STEMINA))

            print("Monster HP : %d Monster MP : %d\n" % (self.Monster.HP, self.Monster.MP))
            print("1.normal attack 2.smash 3.heal 4.imitation 5.maxPower")

            for i in self.Players:

                if self.Players[i].HP <=0: continue

                print("플레이어 %d 의 행동을 정하시오 :"%(i+1),end= " ")
                num1 = int(input())

                if (num1 == 1):
                    self.Monster.HP -= self.Players[i].normalAttack()

                elif (num1 == 2 and self.Players[i].MP >= 20):
                    self.Monster.HP -= self.Players[i].smash()

                elif (num1 == 3 and self.Players[i].MP >= 10):
                    self.Players[i].heal()

                elif (num1 == 2 and self.Players[i].MP >= 30):
                    self.Players[i].imitation()

                elif (num1 == 2 and self.Players[i].STEMINA >= 100):
                    self.Players[i].maxPower()
                else:
                    print("실행 할 수 없는 명령")


            if (self.Monster.HP <= 0):
                print("플레이어들의 승리\n")
                break

            a = random.randint(1, 6)

            i=0
            if self.Players[i].HP == 0:
                i+=1

            if (1 <= a <= 3):
                self.Players[i].HP -= self.Monster.normalAttack()
            elif (4 <= a <= 5):
                self.Players[i].HP -= self.Monster.punch()
            else :
                self.Monster.rest()

            cnt = 0

            for i in self.Players:
                if (i.HP <= 0):

                    print("플레이어[%d]는 쓰러졌다!\n"%(i+1))
                    self.Players.pop(i)

            if (cnt == 3):
                print("플레이어들의 전멸!\n")
                break

            print("================================================================\n")


simulator = GameManager()
simulator.run()
