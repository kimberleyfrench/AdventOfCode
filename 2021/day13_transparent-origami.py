from file_io import read_file

def parse_instruction(instr):
    axis = instr.split(' ')[-1].split('=')[0]
    dir = 0 if axis == 'x' else 1
    pos = instr.split(' ')[-1].split('=')[1]
    return {'dir': dir, 'pos': int(pos)}

def fold_sheet(sheet, instr):
    folded_sheet = []
    for coord in sheet:
        if coord[instr['dir']] > instr['pos']:
            coord[instr['dir']] = instr['pos'] * 2 - coord[instr['dir']]
        if coord not in folded_sheet:
            folded_sheet.append(coord)
    # print('folded', folded_sheet)
    print('# of dots', len(folded_sheet))
    return folded_sheet

def max_pos(sheet, dir):
    max = -1
    for coord in sheet:
        max = coord[dir] if coord[dir] > max else max
    return max

def max_x_pos(sheet):
    return max_pos(sheet, 0)

def max_y_pos(sheet):
    return max_pos(sheet, 1)

def print_sheet(sheet):
    row = '.' * (max_x_pos(sheet) + 1)
    sheet_rows = []
    for _ in range(max_y_pos(sheet) + 1):
        sheet_rows.append(row)
    
    for coord in sheet:
        # print('coord', coord)
        x = coord[0]
        row = sheet_rows[coord[1]]
        sheet_rows[coord[1]] = row[0:x] + '#' + row[x+1:]

    for r in sheet_rows:
        print(r)

input = read_file('input/day13')
idx = len(input) - 1
while input[idx] != '':
    idx -= 1
dot_coords = input[0:idx]
instructions = input[idx+1:]
# print('dot coords', dot_coords)
print('# of dots', len(dot_coords))

sheet = []
for dot in dot_coords:
    coord = [int(dot.split(',')[0]), int(dot.split(',')[1])]
    sheet.append(coord)

for instruction in instructions:
    print(instruction)
    instr = parse_instruction(instruction)
    sheet = fold_sheet(sheet, instr)

print_sheet(sheet)