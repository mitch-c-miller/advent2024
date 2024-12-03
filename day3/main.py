import re


def solution1(program):
    heap_dump = ''
    for p in program: heap_dump += p

    # find all mul(a,b)
    regex_pattern = 'mul\(\d{1,3},\d{1,3}\)'
    mul_list = re.findall(regex_pattern, heap_dump)
    mul_list = [i.replace('mul(', '').replace(')', '').split(',') for i in mul_list]
    return sum([int(i[0]) * int(i[1]) for i in mul_list])


def solution2(program):
    heap_dump = ''
    for p in program: heap_dump += p

    # find all mul(a,b), do(), don't()
    regex_pattern = 'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'    
    instruction_list = re.findall(regex_pattern, heap_dump)

    results = 0
    enabled = True
    for inst in instruction_list:
        if inst == 'do()': enabled = True
        elif inst == 'don\'t()': enabled = False

        if inst.startswith('mul') and enabled:
            mul = inst.replace('mul(', '').replace(')', '').split(',')
            results += int(mul[0]) * int(mul[1])

    return results


def main():
    with open('day3/test_1.txt') as f: print(solution1(f))
    with open('day3/test_1.txt') as f: print(solution2(f))


if __name__ == '__main__':
    main()
