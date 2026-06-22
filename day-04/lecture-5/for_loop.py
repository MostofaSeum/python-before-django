#video link: https://youtu.be/S73thl0AyFU?si=4MD0SGMhpLfXWnRe

#printing a list elements
# list = [1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)

#searching an element in list
# list = [1,4,9,16,25,36,49,64,81,100]
# x = int(input("Enter a number to search: "))

# for i in list:
#     if i == x:
#         print("Index of ", x , "is", list.index(x))
#         break
# else:
#     print("Element is not present in the list")

# for i in range(5):
#     print(i)

# for i in range(0,10,2):
#     print(i)

#practice question 1
# for i in range(101):
#     print(i)

#practice question 2
# for i in range(100,0,-1):
#     print(i)

#practice question 3
# n = int(input("Enter a number: "))
# for i in range (1,11,1):
#     print(n,"*",i,"=",n*i)


n = int(input("Enter a number: "))
m =  1
for i in range(1,n+1,1):
    m = m * i
print(m)
    