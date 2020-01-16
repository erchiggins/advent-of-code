def calc_fuel(mass):
    fuel = mass//3 - 2
    print(f'initial fuel: {fuel}')
    to_offset = fuel
    while True:
        offset = to_offset//3 - 2
        print(f'calculated offset: {offset}')
        if offset <= 0:
            break
        else:
            fuel += offset
            to_offset = offset
    return fuel

if __name__ == '__main__':
    with open('day1input.txt') as f:
        raw_input = f.read()
    module_mass_str = raw_input.split('\n')
    for mms in module_mass_str:
        if mms == '':
            module_mass_str.remove('')
    module_mass_num = [int(module) for module in module_mass_str]
    fuel_sum = 0
    for mass in module_mass_num:
        fuel_sum += calc_fuel(mass)
    print(fuel_sum)


