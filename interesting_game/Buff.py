import Person
import Action


class Buff(object):

    def __init__(self,Type = 0,Effect = [],Continuous_Round = 0):
        self.Type = Type
        self.Effect = Effect
        self.Continuous_Round = Continuous_Round

    