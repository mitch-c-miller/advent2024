from sys import path
path.append('../advent2024')

from utils.file import read_array_from_file


def solution1(data):
    return sum(is_valid_report(report) for report in data)


def solution2(data):
    passing_reports = 0
    for report in data:
        if is_valid_report(report):
            passing_reports += 1
        else:
            for i in range(len(report)):
                if is_valid_report(report[:i] + report[i+1:]):
                    passing_reports += 1
                    break
    return passing_reports


def is_valid_report(levels):
    deltas = [a - b for a, b in zip(levels, levels[1:])]
    sign_check = all(d > 0 for d in deltas) or all(d < 0 for d in deltas)
    range_check = all(-3 <= d <= 3 for d in deltas)
    return sign_check and range_check


def main():
    print(solution1(read_array_from_file('day2/test_1.txt', ' ')))
    print(solution2(read_array_from_file('day2/test_1.txt', ' ')))


if __name__ == '__main__':
    main()
