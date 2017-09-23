import Buff
import Map
import Person
import Action

def Account_buff(buff,person):      ##buff结算
    Action.Num_Change(person,buff.Effect,buff.Type)
    buff.Continuous_Round -=1


def Exist_Person(x,y,persons=[]):   ##区域内人物判断
    for person in Persons:
        if person.position[0] == x and person.position[1] ==y:
            return person 
        else:
            return 0


def Local_Range(Area,change_num,change_type):      ##区域生成
    if Area.range_end and Area.range_start:
        for x in range(Area.range_start[0],Area.range_end[0]):
            for y in range(Area.range_start[1],Area.range_end[1]):
                person = Exist_Person(x,y)
                if person:
                    Action.Num_Change(person,change_num,change_type)
    else:
        pass


def showmap(MAP,PERSONS = []):
    allmap = MAP.returnmap()
    if PERSONS:
        for PERSON in PERSONS:
            allmap[PERSON.Position[1]][PERSON.Position[0]] = "@"
    return allmap

def printmap(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            print (map[y][x],end='')
        print("")
