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