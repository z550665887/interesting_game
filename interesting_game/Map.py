import Buff
import Map
import Person

class Map(object):
    def __init__(self,range_start=[0,0],range_end=[0,0]):
        self.range_start = range_start
        self.range_end = range_end

    def 


class area(Map):

    def __init__(self,range_start=[0,0],range_end=[0,0],times = 0):
        self.range_start = range_start
        self.range_end = range_end
        self.times = times

    # def Local_range(self,change_type,change_num,times = 0):
    #     if self.range_end and self.range_start:
    #         for x in range(self.range_start[0],self.range_end[0]):
    #             for y in range(self.range_start[1],self.range_end[1]):
    #                 if Map_Exist(x,y):
    #                     person = Map_Retrunslef(x,y)
    #                     Num_Change(person,change_num,change_type)
    #     else:
    #         pass
    #     times -= 1