import pickle

with open("5-pickle/banner.p", "rb") as f:
    data = pickle.load(f)

for i in range(len(data)):
    line = ""
    for tup in data[i]:
        for dummyVar in range(tup[1]):
            line += tup[0]
    print(line)
    # print(data[i])
    # print(" ")
