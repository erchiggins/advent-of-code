
directions = [(-1, )]
# NORTH = (-1,  0)
# SOUTH = ( 1   0)
# EAST  = ( 0,  1)
# WEST  = ( 0, -1)

def get_neighbor(pos, direction, height, width):
    r = pos[0]
    c = pos[1]
    if direction == "NORTH" and r > 0:
        return (r -1 , c)
    if direction == "SOUTH" and r < height -1:
        return (r+1 , c)
    if direction == "EAST" and c < width -1:
        return (r, c+1)
    if direction == "WEST" and c > 0:
        return (r, c-1)
    return None

def is_valid(value):
    return value != '#'

def build_distances():
    """
    should take
    * the map
    * current position
    * visited

    returns
    a tree
    """
    pass

def flood_from(map, starting_pos):
    """
    takes a starting position, and returns
    a dictionary of of the distances to all the
    other values (keys and doors) in the maze.
    eg
    {"A": 12, "a": 3, ...}
    we can have
    keys
    doors
    empty
    wall
    """
    to_visit = [(starting_pos, 0)]
    visited = set()
    distances = {}
    height = len(map)
    width = len(map[0])
    while to_visit:
        (position, distance_travelled) = to_visit.pop()
        for direction in ["NORTH", "SOUTH", "EAST", "WEST"]:
           neigh = get_neighbor(position, direction, height, width)
           if neigh and (neigh not in visited):
               val = map[neigh[0]][neigh[1]]
               if is_key_or_door(val):
                   distances[val] = distance_travelled + 1
               if is_not_wall(val):
                   to_visit.append((neigh, distance_travelled + 1,))
        visited.add(position)
    return distances

def is_not_wall(val):
    return val != '#'

def is_key_or_door(val):
    return val == '@' or val.isalpha()

def find_doors_and_keys(map):
    """returns a dictionary of {'A': (r,c), ...} indexes
    of all the places in the map that are
    a door or a key.
    """
    results = {}
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            val = map[row_idx][col_idx]
            if is_key_or_door(val):
                results[val] = (row_idx, col_idx)
    return results

# map_strings = """#########
# #b.A.@.a#
# #########""".split('\n')
map_strings = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""".split('\n')
map = [list(s) for s in map_strings]

height = len(map)
width = len(map[0])

for row_idx, row in enumerate(map):
    if '@' in row:
        col_idx = row.index('@')
        starting_pos = (row_idx, col_idx)
        # map[row_idx][col_idx] = '.'
print(f'Starting position is {starting_pos}')
daks = find_doors_and_keys(map)
distances = {'@': flood_from(map, starting_pos)}
for dak, position in daks.items():
    print(f"{dak} is at position {position}")
    distances[dak] = flood_from(map, position)
print(distances)