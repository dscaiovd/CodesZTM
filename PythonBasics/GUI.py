picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

tree = '*'
empty = ' '
for line in picture:
    for pixel in line:
        if pixel:
            print(tree, end = '')
        else:
            print(empty, end = '')
    print(empty)