class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        for i in range(self.numberOfFloors):
            if i < self.numberOfFloors:
                print('numberOfFloors', i + 1)

house = House()
house.setNewNumberOfFloors(10)