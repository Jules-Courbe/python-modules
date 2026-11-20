#!/usr/bin/env python3

class plante:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def set_height(self, height):
        self.height = height.round()
        if height < 0:
            self.height = 0
            print("{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Height updated: {self.height}")

    def set_age(self, age):
        self.age = age
        if self.age < 0:
            self.age = 0
            print(f"{self.name}: Error, height can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {self.age}")

    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} old")

    def __str__(self):
        return f"Current state: {self.name}: {self.height:.1f}cm,{self.age} old"


class flower(plante):
    def __init__(self, name, age, height, color):
        super().__init__(name, height, age)
        self.color = color


    def bloom(self, height, age):
        self.height = height
        self.age = age
        print("[asking the rose to bloom]")
        super().show()
        print("Rose has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {self.color} Rose has not bloomed yet")


class tree(plante):
    def __init__(self, name, height, age, trunk_diameter, long_shade, wide_shade):
        super().__init__(name, height, age)
        self.wide_shade = long_shade
        self.long_shade = wide_shade
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, trunk_diameter, long_shade, wide_shade):
        #faire un calcul plus le tronc est gros plus l ombre devient grosse. 
        self.long_shade = long_shade
        self.wide_shade = wide_shade
        print("[asking the oak to produce shade]")

    def show(self,):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        print(f"Tree Oak now produces a shade of {self.long_shade} long and {self.wide_shade}cm wide.")


class vegetable(plante):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(self)
        self.harvest_season = harvest_season

    def nutritional_value(self, height, age,):
        self.height = height
        self.age = age
        print(f"[make tomato grow and age for {self.age} days]")
        super().show()

    def show(self):
        super().show()
        print("Color: red Rose has not bloomed yet")
        print(f"Harvest season: {self.harvest_season}")
        print("Nutritional value: 0")


if __name__ == "__main__":
    Rose = flower("Rose", 15, 10, "red")
    Rose.show()
    Oak = tree("Oak", 15000, 150, 25, 0, 0)
    Oak.show()
    Oak.produce_shade(50, 60)