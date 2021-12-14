from file_io import read_file

syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
closing_char_scores = {')': 1, ']': 2, '}': 3, '>': 4}

chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
nav_subsystem = read_file('input/day10')

def find_first_illegal_char(line, opening_chars):
    for char in line:
        if char in chunks.keys():
            opening_chars.append(char)
            continue
        last_chunk = opening_chars.pop(-1)
        if char != chunks[last_chunk]:
            return char

def calc_closing_char_score(closing_chars):
    score = 0
    for char in closing_chars:
        score = score * 5 + closing_char_scores[char]
    return score

# Part 1 && Part 2
syntax_error_score = 0
completion_scores = []

for line in nav_subsystem:
    opening_chars = []
    illegal_char = find_first_illegal_char(line, opening_chars)
    if illegal_char:
        syntax_error_score += syntax_error_scores[illegal_char]
    else:
        closing_chars = list(chunks[char] for char in reversed(opening_chars))
        line_score = calc_closing_char_score(closing_chars)
        completion_scores.append(line_score)

completion_scores.sort()
median_idx = int((len(completion_scores)-1)/2)
completion_score_median = completion_scores[median_idx]
# print('median index:', median_idx, 'scores:', completion_scores)

print('Total syntax error score:', syntax_error_score)
print('Middle score for completion strings:', completion_score_median)