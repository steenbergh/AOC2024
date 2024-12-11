from day05_data import data

def diagnose(d_restrict, guide):
  for ix, nr in enumerate(guide):
    if nr not in d_restrict.keys():
      continue
    for y in range(ix):
      if guide[y] in d_restrict[nr]:
        #print(f'cant have {guide[y]} before {nr}, {guide} is invalid!')
        return (y, ix)
  return [-1]

data = data.split('\n')
data_restrict = [d for d in data if '|' in d]
data_pages = [d for d in data if ',' in d]

dict_restrict = {}
for dr in data_restrict:
  pcs = [int(z) for z in dr.split('|')]
  if pcs[0] not in dict_restrict:
    dict_restrict[pcs[0]] = [pcs[1]]
  else:
    dict_restrict[pcs[0]].append(pcs[1])

middle_sums = 0
safety_guides = [[int(nr) for nr in page.split(',')] for page in data_pages]
for g in safety_guides:
  diag = diagnose(dict_restrict, g)
  if diag[0] == -1: continue
  while diag[0] != -1:
    tmp = g[diag[0]]
    g[diag[0]] = g[diag[1]]
    g[diag[1]] = tmp
    diag = diagnose(dict_restrict, g)  
    
  middle_sums += g[len(g)//2]

print(middle_sums)
