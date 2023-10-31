#!/usr/bin/env python3


# Compare 2 objects in python
# Adapt it according to your object.


class Pokemon:
    def __init__(self, name: str, health: int, attack: int, defense: int, speed: int) -> None:
        self.name = name
        self.hp = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Pokemon):
            for attr in vars(self):
                if getattr(self, attr) != getattr(__value, attr):
                    return False
            return True
        return False
