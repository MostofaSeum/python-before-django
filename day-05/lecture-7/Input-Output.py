#video link: https://youtu.be/jU0cndZziO0?si=wfpDzbgUoAK1s0dS

# File Reading
# f = open("demo.txt", "r") 
# # print(f.read()) 
# line1 = f.readline()
# print(line1,end="")

# line2 = f.readline()
# print(line2,end="")
# f.close()

#File Writing
# f = open("demo.txt", "a")
# f.write("\nJust trying to add another appended line")
# f.close()

#Trying r+
f = open("demo.txt", "r+")
f.write("Overwriting")
print(f.read())
f.close()

#Trying w+
f = open("demo.txt", "w+")
f.write("Overwriting the file with another line")
f.close()