import re

with open("3-bodyguard/bodyguards.txt") as f:
    lines = f.readlines()

text = ""
for line in lines:
    text += line

# text = "BAAABAAA"
pattern = "[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"
x = re.findall(pattern, text)
# x = re.findall("[A-Z]{3}[a-z][A-Z]{3}", text)
# regex = "([A-Z])\\1\\1([a-z])([A-Z])\\3\\3"
# p = re.compile(regex)
# x = re.search(p, text)

solution = ""
for string in x:
    solution += string[4]
print(solution)