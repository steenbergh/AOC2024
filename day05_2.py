#from day05_data import data

data = data.split('\n')
data_restrict = [d for d in data if '|' in d]
data_pages = [d for d in data if ',' in d]

d_beforeme = {}
for dr in data_restrict:
  pcs = [int(x) for x in dr.split('|')]

  if pcs[1] in d_beforeme:
    d_beforeme[pcs[1]].append(pcs[0])
  else:
    d_beforeme[pcs[1]] = [pcs[0]]

# Acceptable Order
ao = []
while len(d_beforeme) > 0:
  for x in range(10, 100):
    if x in ao: continue         # already accepted
    if x in d_beforeme: continue # we still have reservations about this number
    for bm in d_beforeme.keys():
      for ix, page in enumerate(d_beforeme[bm]):
        if page==x:
          del(d_beforeme[bm][ix])
          break
        if len(d_beforeme[bm]) == 0:
          del(d_beforeme[bm])
    ao.append(x)
    print(ao)
