with open("2-mess/mess.txt") as f:
    mess = f.readlines()


characters = []
frequency = []
for line in mess:
    for ch in line:
        if ch in characters:
            frequency[characters.index(ch)] += 1
        else:
            characters.append(ch)
            frequency.append(1)

answer = ""
for idx in range(0, len(characters)):
    if frequency[idx] < 10:
        answer += characters[idx]
print(characters)
print(frequency)
print(answer)
