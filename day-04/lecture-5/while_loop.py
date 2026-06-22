#video link: https://youtu.be/S73thl0AyFU?si=4MD0SGMhpLfXWnRe

#Print 1 to 100
# count = 1
# while count <= 100:
#     print("Hello", count)
#     count += 1

#Print from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("Loop Ended")


#Print multiplication table of 5
# i = 1
# n = int(input("Enter a number: "))
# while i<=10:
#     print(n,"*", i, "=", n*i)
#     i += 1
# print("Loop Ended")

#Printing a list
# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1



#search an element in the list
list = [1,4,9,16,25,36,49,64,81,100]
j =  int(input("Enter a number: "))
i = 0
while i < len(list):
    if j == list[i]:
        print("Element is at index",i)
        break
    i += 1
else:
    print("Element is not present in the list")