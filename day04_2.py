from day04_data import data

def cross(grid, x, y):
  frag1, frag2 = grid[x-1][y-1] + 'A' + grid[x+1][y+1], grid[x-1][y+1] + 'A' + grid[x+1][y-1]
  if (frag1 == "MAS" or frag1=="SAM") and (frag2 == "MAS" or frag2=="SAM"):
    return True
  return False

xmases = 0
grid = [[c for c in row] for row in data.split('\n')]
for x in range(1, len(grid)-1):
  for y in range(1, len(grid[0])-1):
    if grid[x][y] == "A":
      if cross(grid, x, y):
        xmases += 1

print(xmases)
# 1998
