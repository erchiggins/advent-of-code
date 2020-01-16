# read in from file
# process each path as a set of tuples with coordinates
#   (model steps RLUD as individual segments)
# find intersect of sets of tuples 
# minimum value in intersection


if __name__ == "__main__":
    with open('day3input.txt') as f:
        raw_input = f.readlines()
    wire_0 = raw_input[0].split(',')
    wire_1 = raw_input[1].split(',')
    
