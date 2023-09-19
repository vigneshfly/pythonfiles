# #  oops class
# # class student:
# #     def __init__(self):
# #         self.name = "ram"
# #         self.age = 30
# #         self.marks = 80
# #
# #     def talk(self):
# #         print("hello i am:", self.name)
# #         print("my age is:", self.age)
# #         print("marks:", self.marks)
# #
# # s= student()
# # #s.talk()
#
#
# class student:
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
#     def talk(self):
#         print("hello my name:", self.name)
#         print("my roll no:", self.rollno)
#         print("my marks:", self.marks)
#
#
# s1 = student("vignesh", 1101, 89)
# s1.talk()
#
#

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#
#     def display_info(self):
#         print(f"this is car is a{self,brand} {self,model}")
#
#
# car1: object=car()
# car2=display_info()


# class myclass:
#     def __init__(self,name):
#         self.name=name
#
#     def __del__(self):
#         print(f"{self.name} is being destroyed")
#
#
# obj1= myclass("object 1")
# obj2= myclass("object 2")


# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count +1
#
#     @ classmethod
#     def noofobjects(cls):
#        print('no of objects cream:',cls.count)
# t1= Test()
# t2= Test()
# Test.noofobjects()
# t3=Test()
# Test.noofobjects()


# class Engine:
#     a = 10
#
#     def __init__(self):
#         self.b = 20
#
#     def m1(self):
#         print("engine specification")
#
#
# class Car:
#     def __init__(self):
#         self.Engine = Engine()
#
#     def m2(self):
#         print("car using engine function:")
#         print(self.Engine.a)
#         print(self.Engine.b)
#         self.Engine.m1()
#
#
# c = Car()
# c.m2()


# class College:
#
#     a="BSC"
#     def __init__(self):
#         self.b="SURESH"
#
#     def m1(self):
#         print("MUTHAYAMMAL MEMORIAL COLLEGE")
#
#
#
# class Dep:
#     def __init__(self):
#         self.College = College()
#
#     def m2(self):
#         print("MUTHAYAMMAL MEMORIAL COLLEGE:")
#         print("department:",self.College.a)
#         print("HOD NAME:",self.College.b)
#         self.College.m1()
#
#
# c = Dep()
# c.m2()


# n = int(input("enter no of name:"))
# d = {}
# for i in range(n):
#     name = input("enter the name:")
#     marks = int(input("enter the marks:"))
#     d[name] = marks
#
# while True:
#     name = input("enter student name to get marks:")
#     marks = d.get(name, -1)
#
#     if marks == -1:
#         print("student not found:")
#
#     else:
#         print("marks of", name, "are", marks)
#
#     option = input("do you want to find another student mark[yes/no]")
#     if option == "no":
#         print("thanks for using our application:")
#         break






