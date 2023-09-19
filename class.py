# class cars:
#     def __init__(self, name, colour, cost):
#         self.name = name
#         self.colour = colour
#         self.cost = cost
#
#     def talk(self):
#         print("car name:", self.name)
#         print("car colour:", self.colour)
#         print("car cost:", self.cost)
#
#
# s = cars("BMW", "red", 10)
# s.talk()


class Cars:
    showroom="Cars"
    def __init__(self,name,cost,color,millage):
        self.name=name
        self.cost=cost
        self.color=color
        self.millage=millage

    def talk(self):
        print("car name:",self.name)
        print("car cost:",self.cost)
        print("car colour:",self.color)
        print("car millage:",self.millage)

@class method:
    def getshowroom(cls):
        return cls.showroom

@static method:
    def info():
        print("")


