from file_io import read_file
values = read_file('input/day1', type=int)

# Part A
counter = 0
prev_value = values[0]
for value in values:
    if value > prev_value:
        counter += 1
    prev_value = value

print(
    'Number of measurements larger than the previous measurement:', 
    counter
    )

# Part B
measurement_window = 3
sum_counter = 0
prev_sum = sum(values[0: measurement_window])
for i in range(len(values)-measurement_window+1):
    curr_sum = sum(values[i: i+measurement_window])
    if curr_sum > prev_sum:
        sum_counter += 1
    prev_sum = curr_sum

print(
    'Number of sums larger than the previous sum:',
    sum_counter
    )