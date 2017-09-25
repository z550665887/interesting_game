import Person
import Buff
import Result
import Map
import Action

PERSON = Person.Person(Name='zpc1',Position=[15,15])
PERSON2 = Person.Person(Name='zpc2',Position=[16,15])
PERSONS =[]
PERSONS.append(PERSON)
PERSONS.append(PERSON2)
MAP = Map.Map([0,0],[30,20])

Result.printmap(Result.showmap(MAP,PERSONS))
# for person in PERSONS:
#     print (person.Hp_now)
for person in PERSONS:
    Result.run_turn(person)
    Result.attact_turn(person,PERSONS)
Result.printmap(Result.showmap(MAP,PERSONS))
# for person in PERSONS:
#     print (person.Hp_now)