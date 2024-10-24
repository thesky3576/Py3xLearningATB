#By using != operator :
'''for x in range(6):
    x += 1
    if x != 3 and x != 6 :
        print(x)'''
#By using Continue operator :
for i in range(6):
    if (i == 3 or i == 6):
        continue
    print(i)
