from day01_data import data

lst1 = []
lst2 = []

for row in data.split('\n'):
    pcs = row.split('   ')
    lst1.append(int(pcs[0]))
    lst2.append(int(pcs[1]))

lst1.sort()
lst2.sort()

simscore = 0
for x in range(len(lst1)):
    simscore += (lst1[x] * lst2.count(lst1[x]))

print(simscore)
# 26407426
