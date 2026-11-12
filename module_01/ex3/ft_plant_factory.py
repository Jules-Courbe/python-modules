#!/usr/bin/env	python3

class plante:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8
        self.age += 1

    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} old")


if __name__ == "__main__":
    Rose = plante("Rose", 25, 30)
    Tulipe = plante("Tulipe", 36, 45)
    Oak = plante("Oak", 1500, 14600)
    Fern = plante("Ferne", 20, 23)
    Sunflower = plante("Sunflower", 75, 36)
    Rose.show()
    Tulipe.show()
    Oak.show()
    Fern.show()
    Sunflower.show()
