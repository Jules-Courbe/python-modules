#!/usr/bin/env python3

class plante:

    def __init__(self, name, height, age):
        self.name = name.capitalize()
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
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def __str__(self):
        return f"Current state: {self.name}: {self.height:.1f}cm,{self.age} days old"


class flower(plante):
    def __init__(self, name, age, height, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, height, age, color):
        self.height = height
        self.age = age
        print("[asking the rose to bloom]")
        super().show()
        print("Rose has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {self.color} Rose has not bloomed yet")


class tree(plante):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, height, trunk_diameter):
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self.height} long and {self.trunk_diameter}cm wide.")

    def show(self,):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class vegetable(plante):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0

    def grow(self, age, height, nutritional_value):
        self.age = age
        self.height = height
        self.nutritional_value = nutritional_value
        print(f"[make tomato grow and age for {self.age} days]")
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def show(self, nutritional_value):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main(name_flower: str, name_tree: str, name_vegetable: str):
    print("=== Garden Plant Types ===")
    Rose = flower(name_flower, 15, 10, "red")
    Rose.show()
    Rose.bloom(15, 10, "red")
    Oak = tree(name_tree, 15000, 150, 25)
    Oak.show()
    Oak.produce_shade(50, 60)
    tomato = vegetable(name_vegetable, 5, 10, "april")
    tomato.show(0)
    tomato.grow(30, 47, 20)


if __name__ == "__main__":
    main("rose", "oak", "tomato")
