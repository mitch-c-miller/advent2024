def read_array_from_file(filepath, delimiter):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield [int(elem) for elem in line.split(delimiter)]
