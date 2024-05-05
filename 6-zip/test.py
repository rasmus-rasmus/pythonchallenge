string = ""

def add_letter(letter):
    global string
    string += letter
    
letters = [x for x in "Rasmus"]

for letter in letters:
    add_letter(letter)

print(string)