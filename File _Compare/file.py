with open('1.txt', 'r') as file1:
    with open('2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('soutput.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)