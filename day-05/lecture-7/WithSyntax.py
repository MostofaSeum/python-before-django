#video link: https://youtu.be/jU0cndZziO0?si=wfpDzbgUoAK1s0dS

with open("demo.txt", "r") as f:
    print(f.read())


with open("demo.txt", "a") as f:
    f.write("new line")

with open("demo.txt", "w") as f:
    f.write("new line with W mode")