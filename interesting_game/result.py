import Buff
import Map
import Person
import Action

def Account_buff(buff,person):

    if buff.type == 'fly'：
    elif buff.type == 'dizzy':
    elif buff.type == 'silent':
    elif buff.type == 'Persistent HP':
    elif buff.type == 'Persistent MP':

def Exist_Person(x,y,persons=[]):
    for person in Persons:
        if person.position[0] == x and person.position[1] ==y:
            return person 
        else:
            return 0



def Local_Range(area,change_num,change_type):
    if area.range_end and area.range_start:
        for x in range(area.range_start[0],area.range_end[0]):
            for y in range(area.range_start[1],area.range_end[1]):
                person = Exist_Person(x,y)
                if person:
                    Action.Num_Change(person,change_num,change_type)
    else:
        pass
