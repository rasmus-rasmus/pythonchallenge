string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

print(string)
print("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

    

new_string = ""

for ch in string:
    i = alphabet.find(ch)
    if i < 0:
        new_string += ch
    else:
        new_string += alphabet[(i + 2) % len(alphabet)]
print(new_string)