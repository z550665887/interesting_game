import Buff
import Action
import Person
import Result

class Map(object):
    def __init__(self,range_start=[0,0],range_end=[0,0]):
        self.range_start = range_start
        self.range_end = range_end

    def returnmap(self):
        return [[" " for x in range(self.range_end[0]-self.range_start[0])]for y in range(self.range_end[1] - self.range_start[1])]



class Area(Map):

    def __init__(self,range_start=[0,0],range_end=[0,0],times = 1):
        self.range_start = range_start
        self.range_end = range_end
        self.times = times

