import Person
import Buff
import Result
import Map


class Action(object):
    def __init__(self):
        pass

    def Num_Change(self,person,change_num,change_type):
        if change_type == "Hp_Change":
            Hp_Change(person,change_num)
        elif change_type == "Mp_Change":
            Mp_Change(person,change_num)
        elif change_type == "Status_Buff":
            Status_Change(person,change_num)

    def Hp_Change(self,change_num,person):
        person.Hp_now += change_num

    def Mp_Change(self,change_num,range_start=[0,0],range_end=[0,0]):
        person.Mp_now += change_num

    def Status_Change(self,person,change_num):
        person.Status_Buff.append(change_num)

