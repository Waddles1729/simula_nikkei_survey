import re
f = open('p_data.txt')
line = f.readline()
length_list = []
while line:
    new_line = line.replace('\n', '')
    p_list = re.findall('([^。]+。)', new_line)
    for p in p_list:
        p_length = len(p)
        length_list.append(p_length)
    line = f.readline()
f.close()
with open('length_list.txt', 'w') as a:
    for length in length_list:
        a.write(str(length) + '\n')
a.close()
