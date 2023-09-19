# # aribitary  arugument function
#
# def class_10(*students):
#     print(students)
#     for user in students:
#         print(user)
#
#
# class_10("ram","sam","jana")


# keyword arugument function

# def message(name,age):
#     print(name,"age is",age)
#
# message(age=35,name="vignesh")


# ARIBITARY keywords function

# def biodata(**data):
#     print(data)
#
#
# biodata(name="vignesh", age=25, gender="male")


# default parameters  function

# def user(name,city="nammakal"):
#     print(name,"is from",city)
#
# user("ram","salem")
# user("vignesh")

# passing list as an arugument in function

# def total(marks):
#     return sum(marks)
#
# print("total:",total([56,67,89,23]))

# recursive function
# 1*2*3*4*5

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x* factorial(x-1))
#
# print("factorial:",factorial(5))

# lambada function
# c = lambda a: a + 50
# print(c(5)

# c = lambda a, b: a * b
# print(c(2, 2))

# date time in python

import datetime as dt
current_date=dt.date.today()
print("current date:",current_date)