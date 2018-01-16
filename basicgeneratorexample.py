def charcount(filename):
    """ Generator function that reads lines and  yields the line and characters in each line """
    print('Open  textfile')
    with open(filename) as fin:
        for linenumber, line in enumerate(fin):
            print(f'Reading line {linenumber}')
            yield line, len(line)
            print('After yield1')


def countwords(linearray):
    for lines, ccount in linearray:
        print('Get number of words')
        yield ccount, len(lines.split())
        print('After yield2')


r = charcount(filename='sometextIwrote.txt')
for l in r:
    print('Caller control')
    print(f'> {l[0][:-1]}, char count: {l[1]}')

# for i, l in enumerate(countwords(charcount(filename='sometextIwrote.txt'))):
#     print('Caller Control')
#     print(f'> line number:{i} char count: {l[0]}, number of words: {l[1]}')
