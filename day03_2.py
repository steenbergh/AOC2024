import re
from day03_data import data

mode = "DO"

total = 0
modeblocks = re.split("don\'t\(\)", data, maxsplit=1)

while len(modeblocks) == 2:
  if mode == "DO":
    print('\t==> doing mults for ' + modeblocks[0])
    muls = re.findall('mul\((\d+,\d+)\)', modeblocks[0])
    for mul in muls:
      pcs = mul.split(',')
      total += int(pcs[0]) * int(pcs[1])
    mode = "DONT"
    modeblocks= re.split("do\(\)", modeblocks[1], maxsplit=1)
  else:
    mode = "DO"
    print('\t==> skipping mults for ' + modeblocks[0])
    modeblocks= re.split("don\'t\(\)", modeblocks[1], maxsplit=1)

print(mode)
print(len(modeblocks))

print(total)
