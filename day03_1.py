import re
from day03_data import data

total = 0
muls = re.findall('mul\((\d+,\d+)\)', data)
for mul in muls:
  pcs = mul.split(',')
  total += int(pcs[0]) * int(pcs[1])

print(total)
