from day05_data import data

data = data.split('\n')
data_restrict = [d for d in data if '|' in d]
data_pages = [d for d in data if ',' in d]

d_beforeme = {}
for dr in data_restrict:
  pcs = dr.split('|')
  if pcs[1] in d_beforeme:
    d_beforeme[pcs[1]].append(pcs[0])
  else:
    d_beforeme[pcs[1]] = [pcs[0]]

print(d_beforeme)
