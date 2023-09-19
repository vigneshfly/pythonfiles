# a = int(input("enter the age:"))
#
# if (a>=18):
#     print("you are eligible for vote")
# if (a < 18):
#     print("you are not eligible")

# a=int(input("enter the no:"))
#
# if(a>=0):
#     print("postive no")
# if(a<0):
#     print("nagative no")

# a= int(input("enter the no:"))
#
# if(a%2==0):
#     print("even no")
# if(a%2!=0):
#     print("odd no")


# a=int(input("enter the no:"))
# b=int(input("enter the no:"))
# c=int(input("enter the no:"))
#
# if(a+b+c==180):
#     print("triangle")
# if(a+b+c!=180):
#     print("not triangle")


# cp=int(input("enter the cost price:"))
# sp=int(input("enter the selling price:"))
#
# if (cp<sp):
#   l=sp-cp
#   print("profit",l)
#
# if (cp>sp):
#   s=sp-cp
#   print("loss",s)

# grade= int(input("enter the grade:"))
#
# if (90 <= grade <=100):
#     print("a grade")
# if (80 <= grade <= 89):
#     print("b grade")

# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# c=int(input("enter the value:"))
#
# p=(a+b+c)/2
# print("total",p)


# a=int(input("enter the no:"))
# # b=int(input("enter the no:"))
#
# p=(a**(1/2)**(1/3))
#
# print("total",p)


# a = int(input("enter the no:"))
# b = int(input("enter the no:"))
# c = int(input("enter the no:"))
#
# if a >= b and a > c:
#   print(" a is big number")
# if b >= a and b > c:
#   print(" b is big number")
# elif c >= a and c > b:
#   print(" c is big number")
# else:
#   print("all values are equal")

# a = int(input("enter the no:"))
# b = int(input("enter the no:"))
# c = int(input("enter the no:"))
# d = int(input("enter the no:"))
#
# if a <= b and a < c and a < d:
#     print("a is smaller number")
# elif b <= a and b < c and b < d:
#     print("b is smaller number")
# elif c <= a and c < b and c < d:
#     print("c is smaller number")
# elif d <= a and d < b and d < c:
#     print("d is smaller number")
#
# else:
#     print("all number is equal")

# a = input("enter the name:")
# b = int(input("tamil:"))
# c = int(input("english:"))
# d = int(input("maths:"))
# e = int(input("science:"))
# f= int(input("social science:"))
#
# s = b + c + d + e + f
# print("total", s)
#
# k=s/5
# print("average marks",k)


# s = input("enter the words:")
#
# if (s == "a" or s == "e"or s == "i"or s == "o"or s == "u"):
#     print("vowels")
# else:
#     print("constant")


# grade =int(input("enter the mark:"))
#
# if(90<= grade <=100):
#     print("a grade")
# elif(80<= grade <=89):
#     print("b grade")
# elif(70<= grade <=79):
#     print("c grade")
# elif(60<= grade <=69):
#     print("d grade")
#
# else:
#     print("fail")



#a=input("customer name:")
# b=int(input("customer id:"))
c=int(input("enter unit:"))

if(0<= c <=199):
    d=c*1.20
    print("bill:",d)
elif(200<= c <= 400):
    d=c*1.50*1.20
    print("bill:",d)
elif(401<= c <= 800):
    h=c*1.80*1.50*1.20
    print("bill:",h)
elif(d>=h):
    e=h**(15/100)
    print(e)

