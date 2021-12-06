from file_io import read_file

# Part 1
commands = read_file('input/day2')
position = {}
for cmd in commands:
    dir, dist = cmd.split(' ')
    dist = int(dist)
    if dir not in position:
        position[dir] = 0
    position[dir] += dist

print(position)
hz_pos = position['forward']
depth = position['down'] - position['up']
print('HZ', hz_pos, 'depth', depth)
print('The multiplied final position is', hz_pos * depth)


# Part 2
commands = read_file('input/day2')
position = {'hz_pos' : 0, 'depth': 0, 'aim': 0}
for cmd in commands:
    dir, dist = cmd.split(' ')
    dist = int(dist)
    if (dir == 'down'):
        position['aim'] += dist
    elif (dir == 'up'):
        position['aim'] -= dist
    elif (dir == 'forward'):
        position['hz_pos'] += dist
        position['depth'] += position['aim'] * dist
    else:
        print('Unknown command:', cmd)

print(position)
hz_pos = position['hz_pos']
depth = position['depth']
print('HZ', hz_pos, 'depth', depth)
print('The multiplied final position is', hz_pos * depth)