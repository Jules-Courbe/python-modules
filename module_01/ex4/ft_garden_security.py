#!/usr/bin/env python3

class plante:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} old")

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

    def grow(self):
        self.height += 0.8
        self.age += 1

    def __str__(self):
        return f"Current state: {self.name}: {self.height:.1f}cm, {self.age} old"


if __name__ == "__main__":
    Rose = plante("Rose", 15, 10)

    Rose.set_height(25)
    Rose.set_age(-96)
    print(Rose)
