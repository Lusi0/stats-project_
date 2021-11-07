f = open("my.txt", "r")
h = f.read().split()
f.close()

mydict = {}

for line in h:
    (x,y) = line.split(",")
    if y not in mydict:
        mydict.update({y:(0,0)})
    if x == '1':
        i = mydict[y]
        mydict.update({y:(i[0]+1,i[1]+1)})
    else:
        i = mydict[y]
        mydict.update({y:(i[0],i[1]+1)})

newdict = {}
highest = None
lowest = None
for key in mydict:
    if lowest == None:
        lowest = int(key)
    if highest == None:
        highest = int(key)
    if int(key) > highest:
        highest = int(key)
    if int(key) < lowest:
        lowest = int(key)

for i in range(lowest,highest+1,20):
    newdict.update({i:(0,0)})

def myround(x, base=5):
    return base * round(x/base)

for key in mydict:
    i = newdict[str(myround(float(key),20))]
    newdict.update({myround(float(key),20):(i[0]+mydict[key][0],i[1]+mydict[key][1])})
print(newdict)
    
# for key in mydict:
#     i = mydict[key]
#     mydict.update({key:(i[0]/i[1])})
# print(mydict)

# f = open("new.txt","w")
# for key in mydict:
#     f.write("{},{}\n".format(key,mydict[key]))
    
    
