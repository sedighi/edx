#
# users_response=input("please enter celcios :")
# celcios=float(users_response)
# farenhite=(((celcios*9)/5)+32)
# print (farenhite)

# radius=user_input=input("please enter the value of radius :")
# radius=int(radius)
# area=(radius*radius)*3.14
# perimeter=(radius*2)*3.14
# print (area)
# print (perimeter)

# user_age_response=input("please enter your age :")
# user_age_response=int(user_age_response)
# age_per_day=user_age_response*365
# print ("You are" ,age_per_day ,"days old")

# users_int=int(input("please enter an integer number :"))
# y = ((users_int*users_int)-(12*users_int)+11)
# print(y)

# users_input=int(input("please enter the number day of week :"))
# week_days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
# print(week_days[users_input-1])



# sample_list = [2, 10, 3, 5]
# avg=((sample_list[0]+sample_list[1]+sample_list[2]+sample_list[3])/4)
# print(avg)

# user_input=input("please enter a text:")
# if  "dog" in user_input:
#     print("Yes")
# else:
#     print("No")

# user_input=int(input("please enter a number:"))
# if user_input%3==0:
#     print("Yes")
# else:
#     print("No")

# x = 100
# if x > 10 :
#     x = x + 10
# elif x > 20 :
#     x = x + 50
# else:
#     x = x + 70
# print(x)

# user_input=input("please enter a text:")
# if "cat" in user_input and "dog" in user_input:
#     print("Dog2")
# elif  "dog" in user_input:
#     print("Dog")
# elif "cat" in user_input:
#     print("Cat")
#
# else:
#     print("None")


# user_input=int(input("please enter a number:"))
# if user_input==2:
#     print("two")
# elif user_input==3:
#     print("three")
# elif user_input==5:
#     print("five")
# else :
#     print("other")

# user_age_response=int(input("please enter your age :"))
# if user_age_response <= 0 :
#     print ("UNBORN")
# elif user_age_response >0 and user_age_response <= 150:
#     print("ALIVE")
# elif user_age_response>150:
#     print("VAMPIRE")

# user_response=int(input("please enter your number :"))
# if user_response % 2 ==0 and user_response%3==0:
#     print("BOTH")
# elif user_response%2==0 or user_response%3==0:
#     print("ONE")
# else :
#     print ("NEITHER")

# user_response=int(input("please enter work hours :"))
# if user_response <0 or user_response>168 :
#     print ("INVALID")
# elif user_response <=40:
#     print("YOU MADE", user_response*8, "DOLLARS THIS WEEK")
# elif user_response <=41 or user_response <=50:
#     y = user_response - 40
#     print("YOU MADE", 40*8+y*9, "DOLLARS THIS WEEK")
# elif user_response >50:
#     z=user_response - 50
#     print("YOU MADE", 40*8+10*9+z*10, "DOLLARS THIS WEEK")

# x=int(input("please enter integer as seconds :"))
# d=0
# h=0
# m=0
# s=0
# d=x//86400
# x1=x%86400
# h=x1//3600
# x2=x1%3600
# m=x2//60
# x3=x2%60
# s=x3
# if x <=0 :
#     print (d,"days",h,"hours",m,"minutes",s,"seconds")
# else :
#     print (d,"days",h,"hours",m,"minutes",s,"seconds")



# Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)

# sum_of_number=0
# a=1
# while a<=101:
#    print (a)
#    if a%5==0 or a==1 or a==101:
#        sum_of_number += a
#        a=a+1
#        print ("sum of",sum_of_number)
#
#    else :
#        a = a+1
#
# print ("sum_total :",sum_of_number)


# x=0
# count=0
# while x <= 101:
#     if x%5==0:
#         count = count+x
#     x=x+1
# print(count)

# Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n. A factorial is defined as the
# product of all the numbers from 1 to n (1 and n inclusive). For example factorial of 4 is equal to 24. (because 1*2*3*4=24)

# user_input=int(input("please enter the n argument of factorial:"))
# f=1
# d=1
# while user_input >= f:
#    d *= f
#    f= f+1
# print (d)

# Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)

# (1 + 4 + 7 + 10 + ....)
#
# f=1
# d=0
# while 1001 > f:
#     d += f
#     f= f+3
#
#     print (f)
#
# print (d)


# x = 1
# count = 0
# while x < 1001:
#     count = count +x
#     x = x + 3
#     print (x)
# print(count)

# Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.

# x=0
# sum=0
# for x in range(1,101):
#     if x % 2 == 0:
#         sum+=x
# print (sum)

# Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all numbers from 1 to n (including both 1 and n).

# user_int = int(input("Please enter an integer number:"))
# s=0
# for x in range(1,user_int+1):
#    #print ("first x is :",x)
#    s += x
#
#    #print("step is :",x)
# print(s)

# Using a for loop, write a program which asks the user to type a positive integer, n, and then prints
# the sum of the square of all numbers form 1 to n (including both 1 and n).
# For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14

# user_input = int(input("please Enter an positive integer number :"))
# s=0
# for x in range(1,user_input+1):
#     s+=x**2
# print (s)

# Write a program that asks the user for an input 'n' (assume that the user enters a positive integer)
# and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. For example if 'n'
# is equal to 4 then the output should look like the following:

# input_user=int(input("please enter an integer :"))
#
# for x in range(0,input_user+1):
#     x= 10**x
#     print(x)

# def calc_list (in_list):
#     s = 0
#     for a in in_list:
#         s += a
#     return s
# calc_list([1,2,3,4,5])

#
#
# def min_list(in_list):
#     s=0
#     min_n=in_list[0]
#     for a in in_list:
#         if a < min_n:
#             min_n=a
#     return min_n

# def vector_x(lv):
#     x=lv[0]
#     y=lv[1]
#     z=lv[2]
#     m=(x**2+y**2+z**2)**0.5
#     a=x/m
#     b=y/m
#     c=z/m
#     return ([a,b,c])
# vector_x([2,3,-4])

# def payment_month (principal,annual_interest_rate,duration_year):
#     monthly_payment=0
#     if annual_interest_rate >= 1:
#         r = ((annual_interest_rate/100)/12)
#         n = duration_year*12
#     else:
#         n = duration_year*12
#         r = principal / n
#     monthly_payment=principal * ((r * (1 + r) ** n)/((1 + r)**n - 1))
#     return monthly_payment
# print (payment_month(1000.0,10.0,5))
#
# def _calculate_payment(principle, interest_rate_per_year, duration):
#     if interest_rate_per_year==0:
#         return principle/(duration*12)
#     r=interest_rate_per_year/100/12
#     n=duration*12
#     montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
#     return montly_payment
# print (_calculate_payment(1000.0,10.0,5))
#
# def reamining_loan_balance (principal,annual_interest_rate,duration_year,number_of_payments):
#     if annual_interest_rate >= 1:
#         r = ((annual_interest_rate/100)/12)
#         n = duration_year*12
#         p = number_of_payments
#     else:
#         n = duration_year*12
#         p = number_of_payments
#         r = principal * (1 - p / n)
#     reamining_loan_balance=(principal * (((1 + r) ** n) - ((1 + r) ** p)) / ((1 + r) ** n - 1))
#     return reamining_loan_balance
# print (reamining_loan_balance(1000.0,10,4,21))
#
#
# def _calculate_balance(principal, interest_rate_per_year, duration, number_of_payments):
#     if interest_rate_per_year==0:
#         return principal-number_of_payments*(principal/(duration*12.0) )
#     r=interest_rate_per_year/100/12.0
#     n=duration*12
#     balance=principal*((1.0+r)**n - (1.0+r)**number_of_payments) / (((1.0+r)**n)-1)
#     return balance
# print (_calculate_balance(1000.0,10,4,21))




# Your function for calculating payment goes here



# def payment_month(principal, annual_interest_rate, duration_year):
#     monthly_payment = 0
#     if annual_interest_rate >= 1:
#         r = ((annual_interest_rate / 100) / 12)
#         n = duration_year * 12
#     else:
#         n = duration_year * 12
#         r = principal / n
#     monthly_payment = principal * ((r * (1 + r) ** n) / ((1 + r) ** n - 1))
#     return monthly_payment
#
#
# # Your function for calculating remaining balance goes here
#
# def reamining_loan_balance(principal, annual_interest_rate, duration_year, number_of_payments):
#     if annual_interest_rate >= 1:
#         r = ((annual_interest_rate / 100) / 12)
#         n = duration_year * 12
#         p = number_of_payments
#     else:
#         n = duration_year * 12
#         p = number_of_payments
#         r = principal * (1 - p / n)
#     reamining_loan_balance = (principal * (((1 + r) ** n) - ((1 + r) ** p)) / ((1 + r) ** n - 1))
#     return reamining_loan_balance
#
#
# # Your main program goes here
#
# principal = float(input("Enter loan amount: "))
# annual_interest_rate = float(input("Enter annual interest rate (percent): "))
# duration = int(input("Enter loan duration in years: "))
# print("LOAN AMOUNT:", principal, "INTEREST RATE (PERCENT):", annual_interest_rate)
# m_p = payment_month(principal, annual_interest_rate, duration)
# print("DURATION (YEARS):", duration, "MONTHLY PAYMENT:", int(m_p))
# i = 0
# while duration:
#     i = i + 1
#     print("YEAR:", i, "BALANCE:", int(reamining_loan_balance(principal, annual_interest_rate, duration, i*12)),
#           "TOTAL PAYMENT ",int(m_p*i*12) )
#
#     if i == duration:
#         break

# principal=float(input("Enter loan amount: "))
# annual_interest_rate=float(input("Enter annual interest rate (percent): "))
# duration=int(input("Enter loan duration in years: "))
# monthly_payment=_calculate_payment(principal, annual_interest_rate, duration)
# print('LOAN AMOUNT:',int(principal),'INTEREST RATE (PERCENT):', int(annual_interest_rate))
# print('DURATION (YEARS):',duration,'MONTHLY PAYMENT:',int(monthly_payment))
# for year_number in range(1,1+duration):
#     y=_calculate_balance(principal, annual_interest_rate, duration, year_number*12)
#     print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment*year_number*12))

# from math import sin,cos
# def _calc_y(x):
#     y = sin(x) - cos(x) + sin(x)*cos(x)
#     return y
# print (_calc_y(270))


# from math import cos,sqrt
# def _calc_y(x):
#     y = abs(x**3)+cos(sqrt(3 * x))
#     return y
# print (_calc_y(270))

# from math import *
# def _calc_distance(a,b):
#     x1=a[0]
#     y1=a[1]
#     z1=a[2]
#     x2=b[0]
#     y2=b[1]
#     z2=b[2]
#     d = sqrt((x2 - x1)**2 + (y2-y1)**2+(z2-z1)**2)
#     return d
# print(_calc_distance([2,3,-5],[4,-3,12]))

# def _calc_area(h,w):
#     _area = (h+w)*2
#     _perimeter = h*w
#     return [_area,_perimeter]
# print (_calc_area(2,3))

# def _average(_l_a):
#     _av=0
#     _cn=0
#     for _a in _l_a :
#         _av += _a
#         _cn =_cn + 1
#     return _av/_cn
# print(_average([1,2,3,4,5,0]))

# def _max_calc (list_input):
#     max_a=list_input[0]
#     for a in list_input:
#         if a > max_a:
#            max_a = a
#     return max_a
# print(_max_calc([1,0,2,11,4,10,7,8,9]))

# def embedded_function(a, b):
#     # first find the sum of the two numbers
#     my_sum = a + b
#
#     # write a function that accepts a number as parameter and
#     # returns True or False
#     def lets_test_for_even(n):
#         if n % 2 == 0:
#             return True
#         else:
#             return False
#
#     # Now here is the important part!
#     # you need to call your inner function from within the outer function
#     my_result = lets_test_for_even(my_sum)
#     # Now return the result
#     return my_result
#
# print (


def astrerisks_show (int_number):
    if int_number >= 3:
        s = '*'
        c=0
        for d in range(1,(int_number*2)-1):
            print (s)
            s += '*'
            c += 1
            if int_number == c:

                print (s)

    else:
        return False

astrerisks_show(3)