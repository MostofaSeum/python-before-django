#video link: https://youtu.be/jU0cndZziO0?si=wfpDzbgUoAK1s0dS

# Question 1
# with open("practice.txt", "a") as f:
#     f.write("Hi Everyone, \nWe are learning I/O \nUsing Java \nI like programming is Java")

#Question 2
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# print(data)


#Question 3
# def check_for_word():
#     word =  "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#     if data.find(word) != -1:
#         print("Found")
#     else:
#         print("Not Found")

# check_for_word()


# Question 4 

# def check_line():
#     word =  "learning"
#     data = True
#     line_count = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             w =  f.readline()
#             if (word in w):
#                 print("Found in this line : ", line_count)
#                 return
#             line_count += 1
            

# check_line()

#Question 5 
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
nums  = data.split(",")
for i in range(len(nums)):
    if(int(nums[i])%2 == 0):
        print(f"{nums[i]} is even")
    else:
        print(f"{nums[i]} is odd")


