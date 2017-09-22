import Buff
import Action
import Result
import Map



class Person(object):
    def __init__(self,Id = '',Name = '',Hp_UpperLimit = 1,Mp_UpperLimit = 1,Attact_num = 1,\
        Attact_dis = 1,Run_dis = 1,Defense_num = 1,Status_Buff = [],AliveorDie = 1,\
        Move_Allow = 1,Magic_Allow = 1):
        self.Id = Id
        self.Name = Name
        self.Hp_UpperLimit = Hp_UpperLimit
        self.Hp_now = Hp_UpperLimit
        self.Mp_UpperLimit = Mp_UpperLimit
        self.Mp_now = Mp_UpperLimit
        self.Attact_num = Attact_num
        self.Attact_dis = Attact_dis
        self.Run_dis = Run_dis
        self.Defense_num = Defense_num
        self.Status_Buff = Status_Buff
        self.Position = [0,0]
        self.AliveorDie = AliveorDie
        self.Move_Allow = Move_Allow
        self.Magic_Allow = Magic_Allow

    def attact(self,x=0,y=0):
        if self.Attact_dis >= (abs(x)+abs(y)):
            print("I attact position({0},{1})".format((self.Position[0]+x),(slef.Position[1]+y)))
        else:
            print("I can't attact their")

    def defense(self,x=0,y=0):
        print("I Defense position({0},{1})".format((self.Position[0]+x),(slef.Position[1]+y)))

    def run(self,x=0,y=0):
        if self.Run_dis >= (abs(x)+abs(y)):
            print("I run to position({0},{1})".format((self.Position[0]+x),(slef.Position[1]+y)))
        else:
            print("I can't run to their")

    def magic(self):
        print ("I will use magic")

    def die(self):
        if self.Hp_now <= 0:
            self.AliveorDie = 0
            print("I am die")


