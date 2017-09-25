import Buff
import Map
import Person
import Action

def Account_buff(buff,person):      ##buff结算
    Action.Num_Change(person,buff.Effect,buff.Type)
    buff.Continuous_Round -=1


def Exist_Person(x,y,persons=[]):   ##区域内人物判断
    for person in persons:
        if person.Position[0] == x and person.Position[1] ==y:
            return person 
    else:
        return 0


def Local_Range(Area,change_num,change_type,PERSONS):      ##区域结算
    if Area.range_end and Area.range_start:
        for x in range(Area.range_start[0],Area.range_end[0]+1):
            for y in range(Area.range_start[1],Area.range_end[1]+1):
                person = Exist_Person(x,y,PERSONS)
                if person:
                    Action.Action().Num_Change(person,change_num,change_type)
    else:
        pass
    Area.times -=1
    if Area.times <=0:
        Area = []


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

def run_turn(person):
    while True:
        x,y =  map(int,input().split())
        if person.run(x,y):
            break

def attact_turn(person,PERSONS):
    while True:
        x,y = map(int,input().split())
        area = person.attact(x,y)
        if area:
            Local_Range(area,-person.Attact_Num,'Hp_Change',PERSONS)
            break
