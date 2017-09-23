import Person
import Buff
import Result
import Map
import Action

PERSON = Person.Person(Position=[15,12])
PERSON2 = Person.Person(Position=[12,5])
PERSONS =[]
PERSONS.append(PERSON)
PERSONS.append(PERSON2)
MAP = Map.Map([0,0],[30,20])
BUFF =Buff.Buff()
# showmap(MAP,PERSONS)
# print(Result.showmap(MAP,PERSONS))
Result.printmap(Result.showmap(MAP,PERSONS))