import Person
import Buff
import Result
import Map


class Action(object):
    def __init__(self):
        pass

    def Num_Change(self,person,change_num,change_type):
        if change_type == "Hp_Change":
            self.Hp_Change(change_num,person)
        elif change_type == "Mp_Change":
            self.Mp_Change(change_num,person)
        elif change_type == "Status_Buff":
            self.Status_Change(change_num,person)
        elif change_type == "Move_Allow_Change":
            self.Move_Allow_Change(change_num,person)
        elif change_type == "Magic_Allow_Change":
            self.Magic_Allow_Change(change_num,person)
        elif change_type == "Hp_UpperLimit_Change":
            self.Hp_UpperLimit_Change(change_num,person)
        elif change_type == "Mp_UpperLimit_Change":
            self.Mp_UpperLimit_Change(change_num,person)
        elif change_type == "Attact_Num_Change":
            self.Attact_Num_Change(change_num,person)
        elif change_type == "Attact_Dis_Change":
            self.Attact_Dis_Change(change_num,person)
        elif change_type == "Run_Dis_Change":
            self.Run_Dis_Change(change_num,person)
        elif change_type == "Defense_Num_Change":
            self.Defense_Num_Change(change_num,person)
        elif change_type == "AliveorDie_Change":
            self.AliveorDie_Change(change_num,person)

    def Hp_Change(self,change_num,person):  
        person.Hp_now += change_num
        print (person.Hp_now)
        if person.Hp_now <= 0:
            print("%s is die" %person.Name)
            self.Num_Change(person,0,"AliveorDie_Change")

    def Mp_Change(self,change_num,person):   
        person.Mp_now += change_num

    def Status_Change(self,person,change_num):
        person.Status_Buff.append(change_num)

    def Move_Allow_Change(self,change_num,person):
        person.Move_Allow = change_num

    def Magic_Allow_Change(self,change_num,person):
        person.Magic_Allow = change_num

    def Hp_UpperLimit_Change(self,change_num,person):
        person.Hp_UpperLimit += change_num

    def Mp_UpperLimit_Change(self,change_num,person):
        person.Mp_UpperLimit += change_num

    def Attact_Num_Change(self,change_num,person):
        person.Attact_Num += change_num

    def Attact_Dis_Change(self,change_num,person):
        person.Attact_Dis += change_num

    def Run_Dis_Change(self,change_num,person):
        person.Run_Dis += change_num

    def Defense_Num_Change(self,change_num,person):
        person.Defense_Num += change_num

    def AliveorDie_Change(self,change_num,person):
        person.AliveorDie = change_num