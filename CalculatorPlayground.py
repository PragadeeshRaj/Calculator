def mean(List):
    total = 0
    for x in List:
        total += x
    mean = total / len(List)
    return mean

Number_List = []

while(True):
    ask = input('enter a number and say "stop" to end: ')

    if ask == 'stop':
        break
    Number_List.append(int(ask))

mean = str(mean(Number_List))

print("mean:"+mean)
