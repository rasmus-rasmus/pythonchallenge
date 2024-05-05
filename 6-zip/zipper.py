import re
import zipfile

comments = b""
def get_nothing(nothing):
    next_nothing = []
    global comments
    basedir = '6-zip/channel/'
    with open(basedir + nothing + '.txt', "r") as file:
        data = file.read()
        next_nothing.append(data)
        next_nothing += re.findall("[0-9]+", data)
    with zipfile.ZipFile('6-zip/channel.zip', 'r') as archive:
        comments += archive.getinfo(nothing + '.txt').comment
    return next_nothing

nothing = get_nothing('90052')

counter = 0
while(counter <= 1000):
    if (len(nothing) == 2):
        last_nothing = nothing
        nothing = get_nothing(nothing[1])
        print(nothing)
    else:
        print("\nCan't find the next nothing.")
        print("Counter is: ", counter)
        print("Nothing is: ", nothing)
        print("File content is: ", nothing[0])
        print("Last nothing is: ", last_nothing)
        nothing = input("Enter next nothing or enter 'abort' to stop the program: ")
        if (nothing == "abort"):
            break
        last_nothing = [nothing]
        nothing = get_nothing(nothing)
    counter +=1
    
hint = ""
for ch in comments:
    hint += chr(ch)
    
print(hint)