# video link: https://youtu.be/OvTH-7ESoRA?si=zcz9KMRrMtHDgLti

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("end")

# show(5)

#Factorial using recursion
def fact(num):
    if num ==1 or num == 0:
        return 1
    else:
        return num * fact(num-1)

#print(fact(5))

#Practice Question 1
#num = int(input("Enter a number: "))
def sum(num):
    if num == 0:
        return 0
    return num + sum(num-1)

# print(sum(num))

#Practice Question 2
collections = ["apple", "banana","cherry"]
def print_collection(list):
    print(print_collection(list[(list.length-1)]))

print_collection(collections)