a = []
for x in range(20):
    a.append([])
    for y in range(20):
        a[x].append('1')

st = ""
for x in range(20):
    for y in range(20):
       st+=a[x][y]
    st+='\n'
