
directions = [(-1, )]
# NORTH = (-1,  0)
# SOUTH = ( 1   0)
# EAST  = ( 0,  1)
# WEST  = ( 0, -1)

def get_neighbor(pos, direction):
    if direction == "NORTH":
        return (pos[0] -1 , pos[1])
    if direction == "SOUTH":
        return (pos[0] +1 , pos[1])
    if direction == "EAST":
        return (pos[0], pos[1] + 1)
    if direction == "WEST":
        return (pos[0], pos[1] - 1)

def find_options(map, pos, keys, steps):
    to_visit = [(pos, 0)]
    visited = set()
    options = []

    while to_visit:
        (position, distance_travelled) = to_visit.pop()
        (r,c) = position

        if r < height - 1:
            neigh = get_neighbor(position, "SOUTH")
            if neigh is valid: 
                to_visit.apepnd(neigh)

        if r > 0:
            neigh = get_neighbor(position, "NORTH")
            if neigh is valid: 
                to_visit.apepnd(neigh)

        if c < width - 1:
            neigh = get_neighbor(position, "EAST")
            if neigh is valid: 
                to_visit.apepnd(neigh)

        if c > 0:
            neigh = get_neighbor(position, "SOUTH")
            if neigh is valid: 
                to_visit.apepnd(neigh)






map_strings = """#########
#b.A.@.a#
#########""".split('\n')
map = [list(s) for s in map_strings]

height = len(map)
width = len(map[0])

for row_idx, row in enumerate(map):
    if '@' in row:
        col_idx = row.index('@')
        starting_pos = (row_idx, col_idx)
        map[row_idx][col_idx] = '.'
print(f'Starting position is {starting_pos}')
print(map)
find_options(map, starting_pos, [], 0)