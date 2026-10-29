s = input("Enter a roman number: ")
s = list(s)
num = 0
previous = 0
values = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }
for i in s:
    num+=values[i]
    if values[i]>previous:
        num-=previous*2
    previous = values[i]
return num
