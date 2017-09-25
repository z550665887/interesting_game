import Buff
import Action
import Result
import Map



class Person(object):
    def __init__(self,Id = '',Name = '',Hp_UpperLimit = 1,Mp_UpperLimit = 1,Attact_Num = 1,\
        Attact_Dis = 1,Run_Dis = 1,Defense_Num = 1,Status_Buff = [],AliveorDie = 1,\
        Move_Allow = 1,Magic_Allow = 1,Position=[0,0]):
        self.Id = Id
        self.Name = Name
        self.Hp_UpperLimit = Hp_UpperLimit
        self.Hp_now = Hp_UpperLimit
        self.Mp_UpperLimit = Mp_UpperLimit
        self.Mp_now = Mp_UpperLimit
        self.Attact_Num = Attact_Num
        self.Attact_Dis = Attact_Dis
        self.Run_Dis = Run_Dis
        self.Defense_Num = Defense_Num
        self.Status_Buff = Status_Buff
        self.Position = Position
        self.AliveorDie = AliveorDie
        self.Move_Allow = Move_Allow
        self.Magic_Allow = Magic_Allow

    def attact(self,x=0,y=0):
        if self.Attact_Dis >= (abs(x)+abs(y)):
            print("I attact position({0},{1})".format((self.Position[0]+x),(self.Position[1]+y)))

            area = Map.Area([self.Position[0]+x,self.Position[1]+y],[self.Position[0]+x,self.Position[1]+y],1)
            return area
        else:
            print("I can't attact their")
            return 0

    def defense(self,x=0,y=0):
        print("I Defense position({0},{1})".format((self.Position[0]+x),(self.Position[1]+y)))

    def run(self,x=0,y=0):
        if self.Run_Dis >= (abs(x)+abs(y)):
            print("I run to position({0},{1})".format((self.Position[0]+x),(self.Position[1]+y)))
            self.Position[0],self.Position[1] = self.Position[0]+x,self.Position[1]+y
            return 1
        else:
            print("I can't run to their")
            return 0 

    def magic(self):
        print ("I will use magic")



