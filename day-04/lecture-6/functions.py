# video link: https://youtu.be/OvTH-7ESoRA?si=zcz9KMRrMtHDgLti

def cal_sum(a,b):
    sum = a+b
    print(sum)
# cal_sum(10,20)

def cal_sum(a,b):
    return a+b
# print(cal_sum(10,20))

#average of 3 numbers
# def avg(a,b,c):
#     print((a+b+c)/3)

# avg(10,20,30)


hero = ["thor", "ironman", "hulk"]
cities =["dhaka", "chittagong","sylhet","barishal","khulna"]
def length(l):
    return(len(l))

# print(length(hero))
# print(length(cities))

def print_list(l):
    for i in l:
        print(i,end=" ")

# print_list(hero)
# print()
# print_list(cities)

#Function for factorial

def factorial(i):
    f=1
    for j in range(1,i+1, 1):
        f = f * j
    return f

# print(factorial(5))

#Even Odd function

def check(num):
    if(num%2) == 0:
        return "Even"
    else:
        return "Odd"
           
# print(check(11))



