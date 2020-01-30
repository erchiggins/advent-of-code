# directions key for neighbor discovery
# NORTH = (-1,  0)
# SOUTH = ( 1   0)
# EAST  = ( 0,  1)
# WEST  = ( 0, -1)

# returns tuple of N/S/E/W neighbor if it exists


def get_neighbor(pos, direction, height, width):
    r = pos[0]
    c = pos[1]
    if direction == "NORTH" and r > 0:
        return (r - 1, c)
    if direction == "SOUTH" and r < height - 1:
        return (r+1, c)
    if direction == "EAST" and c < width - 1:
        return (r, c+1)
    if direction == "WEST" and c > 0:
        return (r, c-1)
    return None


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
    {"a": (3,'ADF'), {dist:3, keys:'} ...}
    we can have
    keys
    doors
    empty
    wall
    """
    to_visit = [(starting_pos, 0, "")]
    visited = set()
    distances = {}
    height = len(map)
    width = len(map[0])
    while to_visit:
        # grab next space to visit
        (position, distance_travelled, doors) = to_visit.pop()
        # check all its neighbors
        for direction in ["NORTH", "SOUTH", "EAST", "WEST"]:
            neigh = get_neighbor(position, direction, height, width)
            if neigh and (neigh not in visited):
                # neighbor exists and has not been explored
                val = map[neigh[0]][neigh[1]]
                if is_key(val):
                    # found a key to add to the distances dict
                    distances[val] = {'dist':distance_travelled + 1, 'behind': doors}
                if is_not_wall(val):
                    if is_door(val):
                        to_visit.append((neigh, distance_travelled + 1, doors+val,))
                    else:
                        to_visit.append((neigh, distance_travelled + 1, doors,))
        visited.add(position)
    return distances

def is_not_wall(val):
    return val != '#'

def is_key(val):
    return val.isalpha() and val.islower()

def is_door(val):
    return val.isalpha() and val.isupper()

def find_doors_and_keys(map):
    """returns a dictionary of {'A': (r,c), ...} indexes
    of all the places in the map that are
    a door or a key.
    """
    results = {}
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if is_key(col) or is_door(col):
                results[col] = (row_idx, col_idx)
    return results

def is_accessible(behind, keys):
    """ returns whether all keys to open doors in 'behind' string
    have been obtained 
    keys is a list representing keys obtained so far
    """
    return all([door.lower() in keys for door in behind])

# keys is which keys have been obtains so far
def find_accessible(distances, current_pos, keys):
    options = distances[current_pos]
    # filter out options which are behind no doors, or doors for which we have keys
    # accessible = []
    # for key, details in options.items():
    #     if is_accessible(details['behind'], keys):
    #         accessible.append(key)
    return [key for key,details in options.items() 
                   if is_accessible(details['behind'], keys)]

def find_shortest_path(distances, num_keys):
    best_distance =10000000000000
    best_path = []
    paths_to_explore = [('@', [], 0)]
    while paths_to_explore:
        current_pos, keys_collected, distance_travelled = paths_to_explore.pop()
        print(f"got all the keys with travelled {distance_travelled}, path was {keys_collected}. We have {len(keys_collected)} keys and want {num_keys} keys.")
        if len(keys_collected) == num_keys:
            if distance_travelled < best_distance:
                best_distance = distance_travelled
                best_path = keys_collected
        options = [option for option in find_accessible(distances, current_pos, keys_collected) if option not in keys_collected]
        for option in options:
            # look up distance to key which is option
            # print(distances[current_pos])
            dist_to_key = distances[current_pos][option]['dist']
            paths_to_explore.append((option, keys_collected+[option], distance_travelled+dist_to_key))
    return best_path


# create map and find starting position
# map_strings = """#########
# #b.A.@.a#
# #########""".split('\n')
input = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""
map_strings = input.split('\n')
print(input)
map = [list(s) for s in map_strings]
height = len(map)
width = len(map[0])
for row_idx, row in enumerate(map):
    if '@' in row:
        col_idx = row.index('@')
        starting_pos = (row_idx, col_idx)
print(f'Starting position is {starting_pos}')

daks = find_doors_and_keys(map)

# create dict of distances from every key/door to every other key/door
# first entry is starting position @
distances = {'@': flood_from(map, starting_pos)}
# add all other keys and doors' data to distances
for dak, position in daks.items():
    # print(f"{dak} is at position {position}")
    distances[dak] = flood_from(map, position)
# print(distances)
print(distances.keys())
num_keys = len([key for key in distances.keys() if is_key(key)])
print(num_keys)
# print(find_accessible(distances, 'f', ''))
print(find_shortest_path(distances, num_keys))


