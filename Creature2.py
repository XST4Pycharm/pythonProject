from mongoengine import *


class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField

    description = StringField

    meta ={'strict':False}


class Creatures(Document):
    name = DynamicField()

    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    lore = StringField()

    meta = {'strict':False}

    def __repr__(self):
        ability_name = self.ability.name if self.ability else "No ability yet"
        return f"<Creature {self.name} - Attack {self.attack}: {ability_name}>"

    connect("Creature2")

pass