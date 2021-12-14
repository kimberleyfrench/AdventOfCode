from file_io import read_file

def print_paths(paths):
    print('Paths:', paths[0])
    for p in paths[1:]:
        print('      ', p)

def add_connection(a, b, connections):
    if a not in connections:
        connections[a] = [b]
    else:
        connections[a].append(b)


# Part 1
def is_visit_allowed(node: str, paths):
    if node.isupper():
        return True
    return node not in paths

def find_paths(origin, connections, path, complete_paths):
    path.append(origin)
    if origin == 'end':
        complete_paths.append(path)
        return
    for node in connections[origin]:
        if is_visit_allowed(node, path):
            find_paths(node, connections, path.copy(), complete_paths)
    return complete_paths


connection_list = read_file('input/day12')
connections = {}

for connection in connection_list:
    [a, b] = connection.split('-')
    add_connection(a, b, connections)
    add_connection(b, a, connections)
print('Connections: ', connections)

paths = find_paths('start', connections, [], [])
# print_paths(paths)
print('Total number of paths:', len(paths))


# Part 2
def is_visit_allowed_2(node: str, path, double_visit):
    if node.isupper():
        return True, double_visit
    if node in path:
        if double_visit or node in ['start', 'end']:
            return False, double_visit
        if node not in ['start', 'end']:
            double_visit = True
    return True, double_visit

def find_paths_2(origin, connections, path, complete_paths, double_visit):
    path.append(origin)
    if origin == 'end':
        complete_paths.append(path)
        return
    for node in connections[origin]:
        allowed, double = is_visit_allowed_2(node, path, double_visit)
        if allowed:
            find_paths_2(node, connections, path.copy(), complete_paths, double)
    return complete_paths

paths = find_paths_2('start', connections, [], [], False)
# print_paths(paths)
print('Total number of paths:', len(paths))
