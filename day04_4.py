from day_04_data import data

def row(grid):
  ret = 0
  l = len(grid[0])
  for row in grid:
    for x in range(l-3):
      frag = ''.join(row[x:x+4:])
      if frag == 'XMAS' or frag == 'SAMX':
        ret += 1
  return ret


def col(grid):
  ret = 0
  l = len(grid)
  for cix in range(len(grid[0])):
    for x in range(l-3):
      frag = grid[x][cix] + grid[x+1][cix] + grid[x+2][cix] + grid[x+3][cix]
      if frag == 'XMAS' or frag == 'SAMX':
        ret += 1
  return ret


def diag_pos(grid):
  ret = 0
  for rix in range(len(grid[0])-3):
    for cix in range(len(grid)-3):
      frag = grid[rix][cix] + grid[rix+1][cix+1] + grid[rix+2][cix+2] + grid[rix+3][cix+3]
      if frag == 'XMAS' or frag == 'SAMX':
        ret += 1
  return ret


def diag_neg(grid):
  ret = 0
  for rix in range(len(grid[0])-3):
    for cix in range(3, len(grid)):
      frag = grid[rix][cix] + grid[rix+1][cix-1] + grid[rix+2][cix-2] + grid[rix+3][cix-3]
      if frag == 'XMAS' or frag == 'SAMX':
        ret += 1
  return ret


grid = [[c for c in row] for row in data.split('\n')]
print( row(grid) + col(grid) + diag_pos(grid) + diag_neg(grid) )
