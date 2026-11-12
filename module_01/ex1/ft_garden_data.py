class plante:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8
        self.age += 1

    def __str__(self):
        return f"{self.name}: {self.height:.1f}cm, {self.age} days"


if __name__ == "__main__":
    Rose = plante("Rose", 25, 30)
    grow_initial = Rose.height

    for i in range(8):
        print(Rose)
        if i < 7:
            Rose.grow()

    grow_final = Rose.height
    grow = round(grow_final - grow_initial, 1)
    print(f"Growth this week: {grow:.1f}")