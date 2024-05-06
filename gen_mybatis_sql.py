fi = open("./temp", "r")
ls = fi.readline().split(', ')
print(ls)
for i in ls:
    print("#{Article." + f"{i}" + "}", end=', ')