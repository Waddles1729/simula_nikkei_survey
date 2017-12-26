f = open('length_list.txt', 'r')
line = f.readline()
length_list = []
while line:
    new_line = line.replace('\n', '')
    length_list.append(int(new_line))
    line = f.readline()
f.close()

from statistics import mean, median, variance, stdev

m = mean(length_list)
median = median(length_list)
variance = variance(length_list)
stdev = stdev(length_list)

print(m, median, variance, stdev)
