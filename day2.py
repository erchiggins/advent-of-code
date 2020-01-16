        
def computer(tape):
    index = 0
    while True:
        instruction = tape[index]
        if instruction == 1:
            tape[tape[index+3]] = tape[tape[index+1]]+tape[tape[index+2]]
        elif instruction == 2:
            tape[tape[index+3]] = tape[tape[index+1]]*tape[tape[index+2]]
        elif instruction == 99:
            # print('Opcode 99, program complete')
            break
        else:
            raise Exception(f'Unknown opcode {instruction}!')
        index += 4
    return tape

def find_result(input_strings):
    noun = 0
    while noun <= 99:
        verb = 0
        while verb <= 99:
            # (re)set input ints
            input_ints = [int(input) for input in input_strings]
            input_ints[1] = noun
            input_ints[2] = verb
            # check combination
            result = computer(input_ints)[0]
            print(result)
            if result == 19690720:
                print('result found!')
                print(result)
                print(f'noun = {noun}, verb = {verb}')
                return (noun, verb)
            verb += 1
        noun += 1

# this is like the main method!
if __name__ == "__main__":
    with open('day2input.txt') as f:
        raw_input = f.read()
    input_strings = raw_input.split(',')
    # part 1
    # input_ints[1] = 12
    # input_ints[2] = 2
    # print(computer(input_ints))

    # part 2
    print(find_result(input_strings))
   
