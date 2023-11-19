f = open("suallar_copy.txt", "r")
print(f.read())  # returns the entire contents of a file as one string


for a in f:
    print(a)
# f.write("pineapples")
# f.write("kiwis")

# for a in f:   
#     print(a,end="")

f.close()