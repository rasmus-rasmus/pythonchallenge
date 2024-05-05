import urllib.request as req
import re

nothings = []
nothing = '12345'
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
request_url = req.urlopen(base_url+nothing)
source_code = str(request_url.read())

counter = 0
while(len(source_code) < 200 and counter <= 400):
    print(counter)
    nothing = re.findall("[0-9]+", source_code)
    if (len(nothing) == 1):
        last_nothing = nothing
        request_url = req.urlopen(base_url+nothing[0])
        source_code = str(request_url.read())
    else:
        print("\nCan't find the next nothing.")
        print("Counter is: ", counter)
        print("Nothing is: ", nothing)
        print("Source code is: ", source_code)
        print("Last nothing is: ", last_nothing)
        nothing = input("Enter next nothing or enter 'abort' to stop the program: ")
        if (nothing == "abort"):
            break
        last_nothing = [nothing]
        request_url = req.urlopen(base_url+nothing)
        source_code = str(request_url.read())
    counter +=1
