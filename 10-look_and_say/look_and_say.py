def compute_next_number(prev):
    next = ""
    counter = 1
    for i in range(len(prev)-1):
        if prev[i] != prev[i+1]:
            next += f"{counter}{prev[i]}"
            counter = 1
            continue
        counter += 1
    
    if prev[len(prev)-1] == prev[len(prev)-2]:
        next += f"{counter}{prev[len(prev)-1]}"
    else:
        next += f"1{prev[len(prev)-1]}"

    return next

def look_and_say_first_n(n):
    seq = ["1"]
    for i in range(n-1):
        seq += [compute_next_number(seq[-1])]
    return seq

print(len(look_and_say_first_n(31)[-1]))
