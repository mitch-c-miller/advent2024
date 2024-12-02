from collections import Counter

def solution1(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    result = sum(abs(sorted_list_1[i] - sorted_list_2[i]) for i in range(len(sorted_list_1)))
    return result


def solution2(list_1, list_2):
    list_2_counts = Counter(list_2)

    result = sum(list_1[i] * list_2_counts[list_1[i]] for i in range(len(list_1)))
    return result


def main():
    list_1, list_2 = [], []

    with open('./test_1.txt', 'r') as file_input:
        for line in file_input:
            line_content = line.strip().split('   ')
            list_1.append(int(line_content[0]))
            list_2.append(int(line_content[1]))

    # test 1
    print(solution1(list_1, list_2))

    # test 2
    print(solution2(list_1, list_2))

if __name__ == '__main__':
    main()
