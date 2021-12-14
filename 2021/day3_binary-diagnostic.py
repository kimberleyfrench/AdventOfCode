from file_io import read_file

def bin_to_dec(binary):
    decimal = 0
    max_i = len(binary) - 1
    for i in range(0, len(binary)):
        bit = max_i - i
        decimal += int(binary[i]) * (2**bit)
    return decimal

# Part 1
report = read_file('input/day3')
diagnosis = {}

for row in report:
    for i in range(len(row)):
        if i not in diagnosis:
            diagnosis[i] = {'0': 0, '1': 0}
        diagnosis[i][row[i]] += 1

gamma_rate_bin = list(
    0 if diagnosis[i]['0'] > diagnosis[i]['1'] else 1
    for i in range(len(report[0]))
    )
gamma_rate_dec = bin_to_dec(gamma_rate_bin)
print('Gamma rate:', gamma_rate_bin, '=>', gamma_rate_dec)

epsilon_rate_bin = list(
    0 if diagnosis[i]['0'] < diagnosis[i]['1'] else 1
    for i in range(len(report[0]))
    )
epsilon_rate_dec = bin_to_dec(epsilon_rate_bin)
print('Epsilon rate:', epsilon_rate_bin, '=>', epsilon_rate_dec)

print('Total power consumption:', gamma_rate_dec * epsilon_rate_dec)


# Part 2
def determine_rate_value(numbers, op):
    for i in range(len(numbers[0])):
        occurrances = {'0': 0, '1': 0}
        for num in numbers:
            occurrances[num[i]] += 1
        bit_selection = op(occurrances['0'], occurrances['1'])
        numbers = list(filter(lambda num: num[i] == bit_selection, numbers))
        if len(numbers) == 1:
            break
    return numbers[0]

oxygen_op = lambda zeros, ones: '0' if zeros > ones else '1'
oxygen_rate_bin = determine_rate_value(report.copy(), oxygen_op)
oxygen_rate_dec = bin_to_dec(oxygen_rate_bin)
print('Oxygen rate:', oxygen_rate_bin, '=>', oxygen_rate_dec)

co2_op = lambda zeros, ones: '0' if zeros <= ones else '1'
co2_rate_bin = determine_rate_value(report.copy(), co2_op)
co2_rate_dec = bin_to_dec(co2_rate_bin)
print('CO2 rate:', co2_rate_bin, '=>', co2_rate_dec)

print('Total life support rating:', oxygen_rate_dec * co2_rate_dec)